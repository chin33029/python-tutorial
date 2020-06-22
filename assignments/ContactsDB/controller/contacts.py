"""Contact EndPoint"""
from flask import request
from flask_restx import Namespace, Resource, fields, inputs, reqparse

from service.contacts import Contacts

NS = Namespace(
    'Contacts',
    description='Operations related to Contacts'
)


GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    'Phonetype_one', required=False, default=None,
    help='Optionally filter by first number type')
GET_PARSER.add_argument(
    'Phonetype_two', required=False, default=None,
    help='Optionally filter by second number type')
GET_PARSER.add_argument(
    'Phonetype_three', required=False, default=None,
    help='Optionally filter by third number type')

CONTACT = NS.model(
    "Contact", {
        "Name": fields.String(
            required=True,
            description="Contact Name",
            example="First Last",
            pattern=r"^[A-Z][-'a-zA-Z]+,?\s[A-Z][-'a-zA-Z]{0,19}$"
        ),
        "phonetype_one": fields.String(
            required=True,
            desciption="Phone Type",
            example="cellphone, homephone, workphone"
        ),

        "Phone_One": fields.String(
            required=True,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "phonetype_two": fields.String(
            required=False,
            desciption="Phone Type",
            example="cellphone, homephone, workphone"
        ),
        "Phone_Two": fields.String(
            required=False,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "phonetype_three": fields.String(
            required=False,
            desciption="Phone Type",
            example="cellphone, homephone, workphone"
        ),
        "Phone_Three": fields.String(
            required=False,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "Home-Name": fields.String(
            required=False,
            description="Address Title",
            example="Undefined"
        ),
        "Home-Street_Number": fields.String(
            required=False,
            description="Home Street Number",
            example="Undefined"
        ),
        "Home-City": fields.String(
            required=False,
            description="Home City",
            example="Undefined"
        ),
        "Home-State": fields.String(
            required=False,
            description="Home State",
            example="Undefined"
        ),
        "Home-Zip": fields.String(
            required=False,
            description="Home Zip Code",
            example="10 digit"
        ),
        "Work-Name": fields.String(
            required=False,
            description="Company Name",
            example="Undefined"
        ),
        "Work-Street_Number": fields.String(
            required=False,
            description="Work Street Number",
            example="Undefined"
        ),
        "Work-City": fields.String(
            required=False,
            description="Work City",
            example="Undefined"
        ),
        "Work-State": fields.String(
            required=False,
            description="Work State",
            example="Undefined"
        ),
        "Work-Zip": fields.String(
            required=False,
            description="Work Zip Code",
            example="5 digit"
        ),

        

    }
)

@NS.route("")
class ContactsCollection(Resource):
    """ Contacts Collection methods """
    @NS.doc(parser=GET_PARSER)
    def get(self):
        """ Returns list of Contacts """
        args = GET_PARSER.parse_args()
        print(f'args={args}')

        return Contacts().get_all(args['Phonetype_one'], args['Phonetype_two'], args['Phonetype_three'])

    @NS.expect(CONTACT, validate=True)
    def post(self):
        """ Adds a new contact """
        return Contacts().create_one(request.get_json())


@NS.route("/<string:name>")
class Contact(Resource):
    """ Contact methods """

    def get(self, name):
        """ Returns a contact with name """
        return Contacts().get_one(name)

    @NS.expect(CONTACT, validate=True)
    def put(self, name):
        """ Updates a contact with name """
        return Contacts().update_one(name, request.json)

    def delete(self, name):
        """ Deletes a Contact with name """
        return Contacts().delete_one(name)
