import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import requests
from swagger_parser import SwaggerParser

params_map = {
    '#/parameters/Accept-Language': 'accept_language',
    '#/parameters/If-None-Match': 'etag',
}

param_type = {
    'boolean': 'bool',
    'integer': 'int',
    'number': 'float',
    'object': 'dict',
    'string': 'str',
}


@dataclass
class OpMeta:
    domain: str
    name: str
    type: str
    path: str


@dataclass
class DomainClassMeta:
    module: str
    class_name: str

    @property
    def attr_name(self) -> str:
        return re.sub(r'(?!^)([A-Z]+)', r'_\1', self.class_name).lower()


@dataclass
class OpParam:
    name: str
    spec: Dict[str, Any]

    def get_name(self) -> str:
        name: str = self.spec['name']
        name = re.sub(r'(?<=\w)([A-Z])', r' \1', name)
        name = name.replace('-', ' ')
        name = re.sub(r' +', ' ', name)
        name = name.lower().replace(' ', '_')

        if name == 'if_none_match':
            name = 'etag'

        return name

    @staticmethod
    def get_spec_type(spec: dict):
        type = spec['type'] if 'type' in spec else None

        if type == 'string':
            return 'str'

        if type == 'integer':
            return 'int'

        if type == 'boolean':
            return 'bool'

        if type == 'array':
            return OpParam.get_array_type(spec['items'])

        raise Exception(f'Unknown type: {type}')

    @staticmethod
    def get_array_type(spec: dict):
        type = OpParam.get_spec_type(spec)

        return f'List[{type}]'

    def get_type(self) -> str:
        return self.get_spec_type(self.spec)


def param_to_dict_elem(param: OpParam) -> str:
    return f"'{param.spec['name']}': {param.get_name()}"


def resolve_param_spec(param_spec: dict, spec: dict) -> dict:
    if '$ref' in param_spec:
        path = param_spec['$ref'].split('/')[1:]
        found_spec = spec
        for part in path:
            found_spec = found_spec[part]

        return found_spec

    return param_spec


def get_type(param_spec: dict):
    if param_spec["type"] == 'array':
        sub_type = param_spec['items']['type']
        if sub_type == 'array':
            return f'List[{get_type(param_spec["items"])}]'
        array_type = param_type[param_spec['items']['type']]

        return f'List[{array_type}]'
    else:
        return param_type[param_spec["type"]]


def params_to_args(params: List[OpParam]) -> str:
    result = ['self']

    params.sort(key=lambda x: 0 if 'required' in x.spec and x.spec['required'] else 1)

    for param in params:
        default = param.spec['default'] if 'default' in param.spec else None
        if not default and ('required' not in param.spec or not param.spec['required']):
            default = 'None'
        param_str = f'{param.get_name()}: {param.get_type()}'
        if default is not None:
            param_str += ' = '
            p_type = param.get_type()
            if p_type == 'str' and default != 'None':
                param_str += f"'{default}'"
            else:
                param_str += f'{default}'

        result.append(param_str)

    return ',\n'.join(result)


def generate_get_function(
    path: str,
    function_name: str,
    description: str,
    header_parameters: List[OpParam],
    path_parameters: List[OpParam],
    query_parameters: List[OpParam],
    response_type: str,
    response_desc: str
):
    header_params = ', '.join([param_to_dict_elem(param) for param in header_parameters])
    query_params = ', '.join([param_to_dict_elem(param) for param in query_parameters])
    path_params = ', '.join([param_to_dict_elem(param) for param in path_parameters])

    func_params = params_to_args([*path_parameters, *query_parameters, *header_parameters])

    description_params: List[OpParam] = []
    description_params.extend(header_parameters)
    description_params.extend(query_parameters)
    description_params.extend(path_parameters)
    description_params = [
        f':param {param.get_name()} {param.get_type()}: DESCRIPTION'
        for param in description_params]

    if response_desc:
        description_params.append(f':returns: {response_desc}')

    description += '\n\n' + '\n'.join(description_params)
    description = description.replace('\n', '\n        ')
    description = '\n'.join(
        [re.sub(r'^ +$', '', desc) for desc in description.split('\n')]
    )

    return f'''
    def {function_name}(
        {func_params}
    ) -> ESIResponse[{response_type}]:
        \'\'\'
        {description}
        \'\'\' #nopep8

        header_params = {{{header_params}}}
        query_params = {{{query_params}}}
        path_params = {{{path_params}}}

        url = f'{{self.BASE_URI}}{path}'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)'''


def generate_domain(
    domain: str, ops: List[OpMeta], spec_parser: SwaggerParser, raw_spec: dict
) -> DomainClassMeta:
    file_path = Path(__file__).parent.joinpath(
        'esilib', 'domain', f'gen_{domain.lower().replace(" ", "_")}.py')

    class_name = ''.join([part[0].capitalize() + part[1:].lower() for part in domain.split(' ')])

    api_version = spec_parser.specification['info']['version']

    file_content = f'''import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


\'\'\'
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
\'\'\'


class {class_name}(BaseDomain):
    \'\'\'
    ESI API version {api_version}
    \'\'\'
    BASE_PATH = '{spec_parser.base_path}'
'''

    functions: List[str] = []

    for op in ops:
        op_spec: Dict[str, dict] = spec_parser.paths[spec_parser.base_path + op.path][op.type]
        description: str = raw_spec['paths'][op.path][op.type]['description']
        path = op.path

        path_parameters = [
            OpParam(param_name, param_spec) for param_name,
            param_spec in op_spec['parameters'].items() if param_spec['in'] == 'path']
        query_parameters = [
            OpParam(param_name, param_spec) for param_name,
            param_spec in op_spec['parameters'].items() if param_spec['in'] == 'query']
        header_parameters = [
            OpParam(param_name, param_spec) for param_name,
            param_spec in op_spec['parameters'].items() if param_spec['in'] == 'header']
        # cookie_parameters =
        #   OpRawParam(param_name, param_spec) for param_name,
        #   param_spec in op_spec['parameters'].items() if param_spec['in'] == 'cookie']
        body_parameters = [
            OpParam(param_name, param_spec) for param_name,
            param_spec in op_spec['parameters'].items() if param_spec['in'] == 'body']

        response = op_spec['responses']['200'] if '200' in op_spec['responses'] else None
        if response:
            spec = response['schema']
            response_type = get_type(spec)
            response_desc = spec['description'] if 'description' in spec else None
        else:
            response_type = 'None'
            response_desc = None

        if op.type == 'get':
            functions.append(generate_get_function(
                path, op.name, description, header_parameters, path_parameters,
                query_parameters, response_type, response_desc
            ))
        if op.type == 'post':
            pass
        if op.type == 'put':
            pass
        if op.type == 'delete':
            pass
        pass

    module_name = f'gen_{domain.lower().replace(" ", "_")}'

    file_path = Path(__file__).parent.joinpath('esilib', 'domain', f'{module_name}.py')
    file_path.write_text(file_content + '\n'.join(functions) + '\n')

    return DomainClassMeta(module=module_name, class_name=class_name)


def write_client_class(domains: List[DomainClassMeta]):
    template = Path(__file__).parent.joinpath('esilib', 'templates', 'client.py').read_text()
    imports: List[str] = []
    props: List[str] = []
    for domain in domains:
        imports.append(f'from esilib.domain.{domain.module} import {domain.class_name}')
        props.append(f'''
    @property
    def {domain.attr_name}(self) -> {domain.class_name}:
        return self._get_domain('{domain.attr_name}', {domain.class_name})''')

    file_content = template.replace('~~IMPORTS~~', '\n'.join(imports))
    file_content += '\n'.join(props)
    if file_content[-1] != '\n':
        file_content += '\n'

    Path(__file__).parent.joinpath('esilib', 'client.py').write_text(file_content)


def generate_domains(swagger_url: str = 'https://esi.evetech.net/latest/swagger.json'):
    spec_response = requests.get(swagger_url)
    spec_data = json.loads(spec_response.content)

    spec_parser = SwaggerParser(swagger_dict=spec_data)
    operations = [
        OpMeta(domain=spec[2], name=name, type=spec[1], path=spec[0][len(spec_parser.base_path):])
        for name, spec in spec_parser.operation.items()]

    domains: Dict[str, List[OpMeta]] = {}
    for op in operations:
        if op.domain not in domains:
            domains[op.domain] = []

        domains[op.domain].append(op)

    domains_meta: List[DomainClassMeta] = []
    for domain, ops in domains.items():
        domains_meta.append(generate_domain(domain, ops, spec_parser, spec_data))

    write_client_class(domains_meta)
    subprocess.run('autopep8 --in-place esilib/domain/gen_*.py',
                   shell=True, cwd=Path(__file__).parent)


if __name__ == '__main__':
    generate_domains()
