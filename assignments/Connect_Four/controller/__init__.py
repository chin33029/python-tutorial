""" Controller __init__.py """
from flask_restx import Api

# Import namespaces from the controllers here below.
# Example: from .<file_name> import <namespace> as <namespace_ns>
from .games import NS as games_ns
from .players import NS as players_ns

API = Api(
    version='0.1.0',
    title='Connect Four',
    description='List of Games and Players'
    )

# Add the namespaces to the API below here
# Example: API.add_namespace(<namespace>)
API.add_namespace(games_ns)
API.add_namespace(players_ns)

