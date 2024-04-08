from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events

class EventRepository():
    def insert_event(self, eventinfo: Dict) -> Dict:
        with db_connection_handler as database:
            event = Events(
                id=eventinfo.get("uuid"),
                title=eventinfo.get("title"),
                detail=eventinfo.get("detail"),
                slug=eventinfo.get("slug"),
                maximum_attendees= eventinfo.get("maximum_attendees")
            )

            database.session.add(event)
            database.session.commit()
            
            return eventinfo