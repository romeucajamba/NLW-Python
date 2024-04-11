from src.models.settings.connection import db_connection_handler
from src.models.entities.checki_ns import Check_ins
from sqlalchemy.exc import IntegrityError



class CheckInsRepository():
    def _insert_check_ins(self, attendee_id: str) -> str:
        with db_connection_handler as database:

            try: 
                checkins = ( 
                Check_ins(attendeeId=attendee_id)
                 )
                database.session.add(checkins)
                database.session.commit()

                return attendee_id
            except IntegrityError:
                raise Exception("Check já cadastrado")
            except Exception as exception:
                database.session.rollback()
                raise exception