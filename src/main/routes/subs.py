from flask import Blueprint, jsonify, request
from src.validators.subscribers_creator_validator import subscribers_creator_validator
subs_route_bp = Blueprint("subs_route", __name__)
from src.http_types.http_request import HttpRequest
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_event():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body = request.json)

    subs_repo = SubscribersRepository()
    subs_creator = SubscribersCreator(subs_repo) #fazendo a injeção de dependência
    

    http_response = subs_creator.create_subscriber(http_request)

    return jsonify(http_response.body), http_response.status_code
