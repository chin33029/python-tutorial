# Day 18 Notes

## Discussion points

* Flask RestX schema validation
* Different validation entry points
* Search with different fields <-- Need to discuss in Day 19 (multiple search params with query params)

## Flask RestX schema validation

### Fields
Different Flask RestX fields: https://flask-restx.readthedocs.io/en/latest/_modules/flask_restx/fields.html

Regular Expressions:
https://regex101.com/
^[A-Z]{1}[a-z]+$

Key characters:
^ = beginning of line
$ = end of line
[] = list of valid expressions
{} = number of positions with the previous expression in brackets
*  = 0 or more
+  = one or more