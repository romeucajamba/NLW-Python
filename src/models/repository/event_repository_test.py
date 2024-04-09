### Testes de integração ###
from .event_repository import EventRepository
from src.models.settings.connection import db_connection_handler
import pytest

## Testando a integração com meu banco

db_connection_handler.connector_db()

@pytest.mark.skip(reason="Não quero inserir outros dados no banco")
def test_insert_event():
    event = {
        "uuid": "943558106",
        "title": "TesteTitle",
        "details": "TesteDetails",
        "slug": "testeSlug",
        "maximum_attendees": 10
    }
    events_repository = EventRepository()
    response = events_repository.insert_event(event) 
    print(response)

#@pytest.mark.skip(reason="Não quero retornar os dados outra vez")
def test_get_event_by_id():
    event_id = "943558106"
    event_repository = EventRepository()
    response = event_repository.get_event_by_id(event_id)

    print(response)
    print(response.title)