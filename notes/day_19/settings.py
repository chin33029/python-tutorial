""" Application Settings """
import os

# Flask settings
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)

# Database settings
DB_PORT = os.environ.get('DB_PORT', 27017)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
