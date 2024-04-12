from flask import Blueprint
from flask import jsonify, request
from src.http_types.http_request import HTTPResquest
from src.data.event_handle import EventHandler

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    http_request = HTTPResquest(request.json)
    eventHendler = EventHandler()

    http_response = eventHendler.register(http_request)
    return jsonify(http_response.body), http_response.status_code