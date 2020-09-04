"""Contact EndPoint"""
from flask import request
from flask_restx import Namespace, Resource, fields, reqparse

from service.contacts import Contacts

NS = Namespace(
    'contacts',
    description='Operations related to Contacts'
)


GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    "firstName", required=False,
    help='Optionally filter by first name type')
GET_PARSER.add_argument(
    "lastName", required=False,
    help='Optionally filter by last name type')
GET_PARSER.add_argument(
    "phonetypeOne", choices=['cellphone', 'homephone', 'workphone'], 
    required=False,
    help='Optionally filter by first number type')
GET_PARSER.add_argument(
    "phonetypeTwo", choices=['cellphone', 'homephone', 'workphone'], 
    required=False,
    help='Optionally filter by second number type')
GET_PARSER.add_argument(
    "phonetypeThree", choices=['cellphone', 'homephone', 'workphone'],
    required=False,
    help='Optionally filter by third number type')

CONTACT = NS.model(
    "Contact", {
        "firstName": fields.String(
            required=True,
            description="Contact First Name",
            example="First Name",
            pattern=r"^[A-Z]{1}[A-Z[a-z]+$"
        ),
        "lastName": fields.String(
            required=True,
            description="Contact Last Name",
            example="Last Name",
            pattern=r"^[A-Z]{1}[A-Z[a-z]+$"
        ),
        "phonetypeOne": fields.String(
            required=True,
            desciption="Phone Type",
            example="cellphone or homephone or workphone"
        ),

        "Phone_One": fields.String(
            required=True,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "phonetypeTwo": fields.String(
            required=False,
            desciption="Phone Type",
            example="homephone"
        ),
        "Phone_Two": fields.String(
            required=False,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "phonetypeThree": fields.String(
            required=False,
            desciption="Phone Type",
            example="workphone"
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
            example="5 digit zip"
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

PUT_CONTACT = NS.model(
    "PutContact", {
        "phonetypeOne": fields.String(
            required=True,
            desciption="Phone Type",
            example="cellphone or homephone or workphone"
        ),

        "Phone_One": fields.String(
            required=True,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "phonetypeTwo": fields.String(
            required=False,
            desciption="Phone Type",
            example="homephone"
        ),
        "Phone_Two": fields.String(
            required=False,
            description="Phone Number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "phonetypeThree": fields.String(
            required=False,
            desciption="Phone Type",
            example="workphone"
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
            example="5 digit zip"
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

        return Contacts().get_all(
                                  args["phonetypeOne"],
                                  args["phonetypeTwo"],
                                  args["phonetypeThree"],
                                  args["firstName"],
                                  args["lastName"],)

    @NS.expect(CONTACT, validate=True)
    def post(self):
        """ Adds a new contact """
        return Contacts().create_one(request.get_json())


@NS.route("/<string:id>")
class Contact(Resource):
    """ Contact methods """

    def get(self, id):
        """ Returns a contact via contact_id"""
        return Contacts().get_one(id)

    @NS.expect(CONTACT, validate=True)
    def put(self, id):
        """ Updates a contact with name """
        return Contacts().update_one(id, request.json)

    def delete(self, id):
        """ Deletes a Contact with name """
        return Contacts().delete_one(id)
