from src.models.repository.check_ins_repository import CheckInsRepository
from src.http_types.http_request import HTTPResquest
from src.http_types.http_response import HTTPResponse

class CheckinsHandler:
    def __init__(self) -> None:
        self._checkin_repository = CheckInsRepository()

    def registry(self, http_request: HTTPResquest) -> HTTPResponse:
        check_ins_info = http_request.param["attendee_id"]
        self._checkin_repository._insert_check_ins(check_ins_info)

        return HTTPResponse(
            body=None,
            status_code=201
        )