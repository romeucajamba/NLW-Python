from flask import Blueprint
from flask import jsonify, request
from src.http_types.http_request import HTTPResquest
from src.data.attendees_handler import AttendeesHandler




attendees_route_bp = Blueprint("attendees_route", __name__)

@attendees_route_bp.route('/events/<event_id>/register', methods=["POST"])
def create_attendees(event_id):
    attendees_handle = AttendeesHandler()
    http_request =  HTTPResquest(param={"event_id": event_id}, body=request.json)
    
    http_response = attendees_handle.registery(http_request)
    return jsonify(http_response.body), http_response.status_code


@attendees_route_bp.route('/attendee/<attendee_id>/badge', methods=["GET"])
def get_attendees_badge(attendee_id):
    attendees_handle = AttendeesHandler()
    http_request =  HTTPResquest(param={"attendee_id": attendee_id})
    
    http_response = attendees_handle.find_attendee_badge(http_request)
    return jsonify(http_response.body), http_response.status_code


@attendees_route_bp.route('/events/<event_id>/attendees', methods=["GET"])
def get_attendees(event_id):
    attendees_handle = AttendeesHandler()
    http_request =  HTTPResquest(param={"event_id": event_id})
    
    http_response = attendees_handle.find_attendees_from_event(http_request)
    return jsonify(http_response.body), http_response.status_code