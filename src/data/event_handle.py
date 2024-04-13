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
    
    def find_by_id(self, http_request: HTTPResquest) -> HTTPResponse:
        event_id = http_request.param["event_id"]
        event = self.__event_repository.get_event_by_id(event_id)
        if not event: raise Exception("Evento não encontrado")
        event_attendees_count = self.__event_repository.count_event_attendees(event_id)
        return HTTPResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code=200 
        )