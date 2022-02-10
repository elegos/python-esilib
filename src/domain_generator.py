from dataclasses import dataclass
import json
from pathlib import Path
import re
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
    'string': 'str',
}


@dataclass
class OpMeta:
    domain: str
    name: str
    type: str
    path: str


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

    return ', '.join(result)


def get_function_generator(
    function_name: str,
    description: str,
    func_params: str,
    header_params: str,
    query_params: str,
    path_params: str,
    path: str,
) -> str:
    return f'''

    def {function_name}({func_params}) -> ESIResponse: # return type WIP
        \'\'\'
        {description}
        \'\'\'

        headers = {{{header_params}}}
        query_params = {{{query_params}}}
        path_params = {{{path_params}}}

        url = f'{{self.BASE_URI}}{path}'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=headers)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)'''


def generate_get_function(
    path: str,
    function_name: str,
    description: str,
    header_parameters: List[OpParam],
    path_parameters: List[OpParam],
    query_parameters: List[OpParam],
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
        f':param {param.get_name()} {param.get_type()}: DESCRIPTION' for param in description_params]

    description += '\n\n' + '\n'.join(description_params)
    description = description.replace('\n', '\n        ')

    return f'''

    def {function_name}({func_params}) -> ESIResponse: # return type WIP
        \'\'\'
        {description}
        \'\'\'

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


def generate_domain(domain: str, ops: List[OpMeta], spec_parser: SwaggerParser, raw_spec: dict):
    file_path = Path(__file__).parent.joinpath(
        'esilib', 'domain', f'gen_{domain.lower().replace(" ", "_")}.py')

    class_name = ''.join([part[0].capitalize() + part[1:].lower() for part in domain.split(' ')])

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
    BASE_PATH = '{spec_parser.base_path}'
'''

    functions: List[str] = []

    for op in ops:
        op_spec: Dict[str, dict] = spec_parser.paths[spec_parser.base_path + op.path][op.type]
        description: str = raw_spec['paths'][op.path][op.type]['description']
        path = op.path

        path_parameters = [OpParam(param_name, param_spec) for param_name,
                           param_spec in op_spec['parameters'].items() if param_spec['in'] == 'path']
        query_parameters = [OpParam(param_name, param_spec) for param_name,
                            param_spec in op_spec['parameters'].items() if param_spec['in'] == 'query']
        header_parameters = [OpParam(param_name, param_spec) for param_name,
                             param_spec in op_spec['parameters'].items() if param_spec['in'] == 'header']
        # cookie_parameters = [OpRawParam(param_name, param_spec) for param_name,
        #                      param_spec in op_spec['parameters'].items() if param_spec['in'] == 'cookie']
        body_parameters = [OpParam(param_name, param_spec) for param_name,
                           param_spec in op_spec['parameters'].items() if param_spec['in'] == 'body']

        if op.type == 'get':
            functions.append(generate_get_function(
                path, op.name, description, header_parameters, path_parameters, query_parameters))
        if op.type == 'post':
            pass
        if op.type == 'put':
            pass
        if op.type == 'delete':
            pass
        pass

    file_path = Path(__file__).parent.joinpath(
        'esilib', 'domain', f'gen_{domain.lower().replace(" ", "_")}.py')

    file_path.write_text(file_content + '\n'.join(functions))


def generate_domains(swagger_url: str = 'https://esi.evetech.net/latest/swagger.json'):
    spec_response = requests.get(swagger_url)
    spec_data = json.loads(spec_response.content)

    spec_parser = SwaggerParser(swagger_dict=spec_data)
    operations = [OpMeta(domain=spec[2], name=name, type=spec[1], path=spec[0][len(spec_parser.base_path):])
                  for name, spec in spec_parser.operation.items()]

    domains: Dict[str, List[OpMeta]] = {}
    for op in operations:
        if op.domain not in domains:
            domains[op.domain] = []

        domains[op.domain].append(op)

    for domain, ops in domains.items():
        generate_domain(domain, ops, spec_parser, spec_data)

    return

    spec_params = spec_data['parameters']
    paths = {key: value for key, value in spec['paths'].items() if key.startswith(base_path)}

    if len(paths) == 0:
        raise Exception(
            'Base path should represent at least one path in the swagger paths definition')

    class_name = domain.lower().split(' ')
    class_name = ''.join([string[0].upper() + string[1:].lower() for string in class_name])
    base_uri = base_path

    if base_uri.endswith('/'):
        base_uri = base_uri[0:-1]

    file = f'''import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


\'\'\'
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
\'\'\'

class {class_name}(BaseDomain):
    BASE_URI = '{base_uri}'
'''

    for path, path_spec in paths.items():
        for method, op_spec in path_spec.items():
            # TODO support other verbs
            if method != 'get':
                continue

            description: str = op_spec['description']
            function_name: str = op_spec['operationId']

            description = description.replace('\n', '\n        ')
            func_params: List[str] = ['self']
            func_params_opt: List[str] = []

            header_params = {}
            query_params = {}
            path_params = {}

            desc_params: List[str] = []
            for param in op_spec['parameters']:
                if '$ref' in param:
                    ref = param['$ref']
                    param_name = ref[ref.rindex('/') + 1:]
                    param_spec = spec_params[param_name]
                else:
                    ref = param['name']
                    param_name = ref
                    param_spec = param
                remapped_name = params_map[ref] if ref in params_map else param_name
                remapped_type = get_type(param_spec)

                desc_params.append(
                    f':param {remapped_name}'
                    + f' {remapped_type}:'
                    + f' {param_spec["description"]}'
                )

                if param_spec['in'] == 'path':
                    path_params[param_name] = remapped_name
                elif param_spec['in'] == 'query':
                    query_params[param_name] = remapped_name
                elif param_spec['in'] == 'header':
                    header_params[param_name] = remapped_name
                else:
                    raise Exception(f'Unhandled parameter location: {param_spec["in"]}')

                if param_spec['in'] == 'path':
                    func_params.append(f'{remapped_name}: {remapped_type}')
                else:
                    default_value = param_spec['default'] if 'default' in param_spec else 'None'
                    if remapped_type == 'str' and default_value != 'None':
                        default_value = f"'{default_value}'"
                    func_params_opt.append(f'{remapped_name}: {remapped_type} = {default_value}')

            description += '\n\n        ' + '\n        '.join(desc_params)

            func_params.extend(func_params_opt)
            func_params = ', '.join(func_params)

            header_params = ', '.join([f"'{param}': {remapped_param}" for param,
                                       remapped_param in header_params.items()])
            query_params = ', '.join([f"'{param}': {remapped_param}" for param,
                                      remapped_param in query_params.items()])
            path_params = ', '.join([f"'{param}': {remapped_param}" for param,
                                     remapped_param in path_params.items()])

            path = path[len(base_uri):]

            file += get_function_generator(
                function_name=function_name,
                description=description,
                func_params=func_params,
                header_params=header_params,
                query_params=query_params,
                path_params=path_params,
                path=path
            )

    out_path = Path(__file__).parent.joinpath('esilib', 'domain', f'gen_{class_name.lower()}.py')
    out_path.write_text(file)


if __name__ == '__main__':
    generate_domains()
