from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IdentifierError
from sqlalchemy.orm.exc import NoResultFound

class EventRepository():
    def insert_event(self, eventinfo: Dict) -> Dict:
        with db_connection_handler as database:
           try:
                event = Events(
                id=eventinfo.get("uuid"),
                title=eventinfo.get("title"),
                details=eventinfo.get("details"),
                slug=eventinfo.get("slug"),
                maximum_attendees= eventinfo.get("maximum_attendees")
                )

                database.session.add(event)
                database.session.commit()
            
                return eventinfo
           except IdentifierError:
               raise Exception("Evento já cadastrado")
           
           except Exception as exception:
               database.session.rollback()
               raise exception
    
    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
           try:
                event = (
                database.session
                .query(Events)
                .filter(Events.id==event_id)
                .one()
                 )
                return event
           except NoResultFound:
               return None
               