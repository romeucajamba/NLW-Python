### Testes de integração ###
from .event_repository import EventRepository
from src.models.settings.connection import db_connection_handler

## Testando a integração com meu banco

db_connection_handler.connector_db()

def test_insert_event():
    event = {
        "uuid": "943558106",
        "title": "TesteTitle",
        "detail": "TesteDetail",
        "slug": "testeSlug",
        "maximum_attendees": 10
    }
    events_repository = EventRepository()
    events_repository.insert_event() 