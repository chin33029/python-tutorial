''' Application Entrypoint '''
from flask import Flask
from flask_cors import CORS

from controller import API
from settings import FLASK_DEBUG
from util import logging_setup  # pylint: disable=unused-import

if __name__ == "__main__":
    APP = Flask(__name__)
    CORS(APP)
    API.init_app(APP)
    APP.run(host='0.0.0.0', debug=FLASK_DEBUG)
