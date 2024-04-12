from src.models.repository.event_repository import EventRepository
from src.http_types.http_request import HTTPResquest
from src.http_types.http_response import HTTPResponse
import uuid

class EventHandler:
    def __init__(self):
        self.__event_repository = EventRepository()

    def register(self, http_request: HTTPResquest) -> HTTPResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())

        self.__event_repository.insert_event(body)

        return HTTPResponse(
            body={"event": body["uuid"]},
            status_code=200
        )