from flask import Blueprint, jsonify

# criando um agregador de rotas, rotas relacionadas a eventos estarão aqui

event_route_bp = Blueprint('event_route', __name__) 

from src.http_types.http_response import HttpResponse
@event_route_bp.route("/event", methods=["POST"])
def create_new_event():

    http_reponse = HttpResponse(body={"estou" : "aqui"}, status_code = 201)
    return jsonify(http_reponse.body), http_reponse.status_code
