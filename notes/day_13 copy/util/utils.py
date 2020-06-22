"""
Common utility functions
"""


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
