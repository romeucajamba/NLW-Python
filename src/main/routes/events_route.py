from flask import Blueprint
from flask import jsonify, request
from src.http_types.http_request import HTTPResquest
from src.data.event_handle import EventHandler

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    http_request = HTTPResquest(body=request.json)
    eventHendler = EventHandler()

    http_response = eventHendler.register(http_request)
    return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/events/<event_id", methods=["GET"])
def get_elemnt_id(event_id):
    eventHendler = EventHandler()
    http_request = HTTPResquest(param={"event_id": event_id})
    http_response = eventHendler.find_by_id(http_request)

    return jsonify(http_response.body), http_response.status_code