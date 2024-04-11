from src.models.repository.attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest


db_connection_handler.connector_db()


@pytest.mark.skip(reason="Já foi testado")
def test__insert_attendee():
    event_id = "943558106"
    attendees_info = {
        "uuid": "uuid attendees",
        "name": "romeu_attendees",
        "email": "romeucajamba@gmail",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.__insert_attendees(attendees_info)
    print(response)


def tes_get_attendee_badge_by_id():
    attendde_id = "meu_uuid_attendees"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)
   
    print(attendee)
    print(attendee.title)
