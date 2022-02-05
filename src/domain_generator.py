import json
import re
from typing import List

import requests

params_map = {
    '#/parameters/Accept-Language': 'accept_language',
    '#/parameters/If-None-Match': 'etag',
}

param_type = {
    'string': 'str',
    'integer': 'int'
}


def generate_domain(domain: str, base_path: str, swagger_url: str = 'https://esi.evetech.net/latest/swagger.json'):
    spec_response = requests.get(swagger_url)
    spec = json.loads(spec_response.content)

    spec_params = spec['parameters']

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
                ref = param['$ref']
                param_name = ref[ref.rindex('/') + 1:]
                param_spec = spec_params[param_name]
                remapped_name = params_map[ref] if ref in params_map else param_name
                remapped_type = param_type[param_spec["type"]]

                desc_params.append(
                    f':param {remapped_name}'
                    + f' {remapped_type}:'
                    + f' {param_spec["description"]}'
                )

                if param_spec['in'] == 'path':
                    path_params[param_name] = remapped_name
                if param_spec['in'] == 'query':
                    query_params[param_name] = remapped_name
                if param_spec['in'] == 'header':
                    header_params[param_name] = remapped_name

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

            file += f'''

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

    print(file)


if __name__ == '__main__':
    generate_domain('Alliances', '/alliances/')
