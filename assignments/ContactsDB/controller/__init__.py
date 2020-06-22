""" Controller __init__.py """
from flask_restx import Api

# Import namespaces from the controllers here below.
# Example: from .<file_name> import <namespace> as <namespace_ns>
from .contacts import NS as contacts_ns


API = Api(
    version='0.1.0',
    title='Address Book',
    description='List of Contacts'
    )

# Add the namespaces to the API below here
# Example: API.add_namespace(<namespace>)
API.add_namespace(contacts_ns)

