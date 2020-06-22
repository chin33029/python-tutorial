""" Movies Endpoint """
from flask import request
from flask_restx import Namespace, Resource, fields

from service.movies import Movies

NS = Namespace(
    'movies',
    description='Operations related to movies'
)

MOVIE = NS.model(
    "Movies", {
        "name": fields.String(
            required=True,
            description="Movie name",
            example="The Goods"
        ),
        "genre": fields.String(
            required=True,
            description="Movie genre",
            example="Comedy"
        )
    }
)


@NS.route("")
class MoviesCollection(Resource):
    """ Movies Collection methods """

    def get(self):
        """ Returns list of movies """
        return Movies().get_all()

    @NS.expect(MOVIE)
    def post(self):
        """ Adds a new movie """
        return Movies().create_one(request.get_json())


@NS.route("/<string:name>")
class Movie(Resource):
    """ Item methods """

    def get(self, name):
        """ Returns a movie with name """
        return Movies().get_one(name)

    def put(self, name):
        """ Updates a movie with name """
        return Movies().update_one(name, request.json)

    def delete(self, name):
        """ Deletes a movie with name """
        return Movies().delete_one(name)
