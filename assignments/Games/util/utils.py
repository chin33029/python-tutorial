"""
Common utility functions
"""
from os.path import join, dirname
import jsonref


def snake_case(string_to_convert):
    """ Returns snake_case representation of CamelCase string """
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in string_to_convert]).lstrip('_')


def dash_snake_case(string_to_convert):
    """ Returns dashed snake_case representation of CamelCase string """
    return ''.join(['-'+i.lower() if i.isupper()
                    else i for i in string_to_convert]).lstrip('-')


def rev_dash_snake_case(string_to_convert):
    """ Returns CamelCase version of dash-snake-case """
    return ''.join(i.capitalize() for i in string_to_convert.split('-'))


def load_json_schema(filename):
    """ Loads the given json schema file """
    relative_path = join('../schema', filename)
    absolute_path = join(dirname(__file__), relative_path)

    base_path = dirname(absolute_path)
    base_uri = 'file://{}/'.format(base_path)

    with open(absolute_path) as schema_file:
        return jsonref.loads(
            schema_file.read(), base_uri=base_uri, jsonschema=True)
