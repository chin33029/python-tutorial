# Day 16 Notes

## Overview

Learning Rest API development with Flask RestX.
https://flask-restx.readthedocs.io/en/latest/

## Concepts

API = Application Programming Interface
https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/

REST API is a language or contract that peiple use on the World Wide Web (WWW) that allows services to communicate with each other

### HTTP Methods

GET - Get something from a service (ex. database)
POST - Create a new item and put it in the database.
PUT - Update an item in the database
DELETE - Remove an item from the database

## Resources

Think of resources like objects.
/fruits
    - `GET /fruits` Returns a list of fruits
    - `POST /fruits` Create a new fruit

/contacts
    - `GET /contacts` Returns a list of contacts
    - `GET /contacts/{id}` Returns the contact with id={id}
    - `GET /contacts/{id}?fields=[firstName,lastName,phoneNumber]` Returns the contact with id={id} on the feilds specified
/meats

def test(one, two):

Path Parameter:
Path Parameter: things that are on the URL.  `GET http://<servername>.com/<resource>/<path_parameter>`
test('foo','bar')  --> `GET /contacts/foo/bar`

Query Parameter:
test(one='foo', two='bar')  --> `GET /contacts?one=foo&two=bar`

### HTTP Response Codes

https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
2xx : Successful Response Codes
    - 200:  OK
    - 201: Created
    - 202: Accepted
4xx : Error Response Codes
    - 400: Bad Request
    - 404: Not Found
5xx : Uncaught Error Codes (Really Bad)

### Directory structure that I use when using Flask RestX for my API

```bash
├── app.py              <-- This is the entry point
├── controller          <-- This is the entrypoint for APIs and he directs it to the right service
│   ├── __init__.py
│   └── items.py
├── requirements.txt
├── service             <-- This is where all the real work happens
│   ├── __init__.py
│   └── items.py
├── settings.py
└── util
    ├── __init__.py
    └── logging_setup.py
```

### Code flow

* app.py
* controller/__init__.py <-- Namespace defined here
* controller/<resource.py>  <-- example controller/items.py
* service/<resource.py>  < Example: service/items.py
