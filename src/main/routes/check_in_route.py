from flask import Blueprint
from flask import jsonify
from flask import request
from src.http_types.http_request import HTTPResquest
from src.data.checkins_handle import CheckinsHandler


check_in_route_bp = Blueprint("check_in_route", __name__)


@check_in_route_bp.route("attendees/<attendee_id>/check_in", methods=["POST"])
def create_check_in(attendee_id):
    check_in_handler = CheckinsHandler()
    http_request = HTTPResquest(param={"attendee_id": attendee_id})
    http_response = check_in_handler.registry(http_request)

    return jsonify(http_response.body), http_response.status_code
