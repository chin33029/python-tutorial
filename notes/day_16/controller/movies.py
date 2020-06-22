""" Movies Endpoint """
from flask import request
from flask_restx import Namespace, Resource

from service.items import Items

NS = Namespace(
    'movies',
    description='Operations related to movies'
)


@NS.route("")
class MoviesCollection(Resource):
    """ Items Collection methods """

    def get(self):
        """ Returns list of movies """
        return Items().get_all()

    def post(self):
        """ Adds a new movie """
        return {'message': 'Created movie'}, 201


@NS.route("/<string:name>")
class Movie(Resource):
    """ Item methods """

    def get(self, name):
        """ Returns a movie with name """
        return Items().get_one(name)

    def put(self, name):
        """ Updates a movie with name """
        return Items().update_one(name, request.json)

    def delete(self, name):
        """ Deletes a movie with name """
        return Items().delete_one(name)
