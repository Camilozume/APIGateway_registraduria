from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

votos_blueprints = Blueprint("votos_blueprints",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/voto"

@votos_blueprints.route("/votos/all", methods=["GET"])
def get_all_votos() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@votos_blueprints.route("/votos/<string:id_>", methods=["GET"])
def get_voto_by_id(id_ : str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@votos_blueprints.route("/votos/create", methods=["POST"])
def create_voto() -> dict:
    voto = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=voto)
    return response.json()

@votos_blueprints.route("/votos/update/<string:id_>", methods=["PATCH"])
def update_voto(id_ : str) -> dict:
    voto = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=voto)
    return response.json()

@votos_blueprints.route("/votos/delete/<string:id_>", methods=["DELETE"])
def delete_voto( id_ : str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()