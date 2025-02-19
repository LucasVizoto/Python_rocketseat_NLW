from flask import Blueprint, jsonify, request

# criando um agregador de rotas, rotas relacionadas a eventos estarão aqui

event_route_bp = Blueprint('event_route', __name__) 

from src.validators.events_creator_validator import events_creator_validator

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    events_creator_validator(request)
    http_request = HttpRequest(body = request.json)


    http_reponse = HttpResponse(body={"estou" : "aqui"}, status_code = 201)
    return jsonify(http_reponse.body), http_reponse.status_code
