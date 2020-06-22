""" Items Endpoint """
from flask import request
from flask_restx import Namespace, Resource, fields

from service.items import Items

NS = Namespace(
    'items',
    description='Operations related to items'
)

ITEM = NS.model(
    "Item", {
        "name": fields.String(
            required=True,
            description="Item name",
            example="Apple"
        ),
        "price": fields.String(
            required=True,
            description="Item price",
            example="1.25"
        )
    }
)


@NS.route("")
class ItemsCollection(Resource):
    """ Items Collection methods """

    def get(self):
        """ Returns list of items """
        return Items().get_all()

    @NS.expect(ITEM)
    def post(self):
        """ Creates a new item """
        return Items().create_one(request.get_json())


@NS.route("/<string:name>")
class Item(Resource):
    """ Item methods """

    def get(self, name):
        """ Returns a item with name """
        return Items().get_one(name)

    def put(self, name):
        """ updates a item with name """
        return Items().update_one(name, request.json)

    def delete(self, name):
        """ deletes a item with name """
        return Items().delete_one(name)
