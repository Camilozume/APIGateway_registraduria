from flask import Blueprint, request

import requests
from utils import load_file_config, HEADERS

mesas_blueprints = Blueprint('mesas_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registraduria') + "/mesas"


@mesas_blueprints.route("/mesas", methods=['GET'])
def get_all_students() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()
