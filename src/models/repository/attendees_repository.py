from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from typing import Dict
from src.models.entities.events import Events
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

class AttendeesRepository():
    def __insert_attendees(self, attenddInfo: Dict) -> Dict : 
        with db_connection_handler as database:
            try:
                attendee =  (Attendees(
                    id = attenddInfo.get("uuid"),
                    name = attenddInfo.get("name"),
                    email = attenddInfo.get("email"),
                    event_id = attenddInfo.get("event_id")

                )
                )
                database.session.add(attendee)
                database.session.commit()
                return attenddInfo
            
            except IntegrityError:
               raise Exception("participante já cadastrado já cadastrado")
            
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_attendee_badge_by_id(self, attendee_id: str):
        with db_connection_handler as database:
            try:
               attendee = (
                   database.session.query(Attendees)
                   .join(Events, Events.id == Attendees.event_id)
                   .filter(Attendees.id==attendee_id)
                   .with_entities(
                       Attendees.name,
                       Attendees.email,
                       Events.title
                   ).one()
               )

               return attendee
               
            except NoResultFound:
                return None