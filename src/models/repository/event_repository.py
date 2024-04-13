from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.models.entities.attendees import Attendees



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
           except IntegrityError:
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
    

    def  count_event_attendees(self, event_id) -> Dict:
        with db_connection_handler as database:

                event_count = (
                    database.session
                    .query(Events)
                    .join(Attendees, Events.id == Attendees.event_id)
                    .filter(Events.id==event_id)
                    .with_entities(
                        Events.maximum_attendees,
                        Attendees.id
                    )
                    .all()
                )

                if not len(event_count):
                    return {
                        "maximumAttendees": 0,
                        "AttendeesAmount": 0
                    }
                return {
                        "maximumAttendees": event_count[0].maximum_attendees,
                        "AttendeesAmount": len(event_count)
                    }