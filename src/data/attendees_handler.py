import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.http_types.http_request import HTTPResquest
from src.http_types.http_response import HTTPResponse
from src.models.repository.event_repository import EventRepository

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventRepository()

    def registery(self, http_request: HTTPResquest) -> HTTPResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]
        events_attendees_count = self.__events_repository.count_event_attendees(event_id)
        
        if(
            events_attendees_count["attendeesAmount"]
            and events_attendees_count["maximumAttendees"] <= events_attendees_count["attendeesAmount"]
        ): raise Exception("Evento lotado")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.__insert_attendees(body)

        return HTTPResponse(body=None, status_code=201)

    def find_attendee_badge(self, http_request: HTTPResquest) -> HTTPResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        if not badge: raise Exception("Participante não encontrado")

        return HTTPResponse(
            body={
                "badge":{
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title
                }
            },

            status_code=200
        )