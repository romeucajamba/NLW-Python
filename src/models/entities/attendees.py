from models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class Attendees(Base):
    __tableName__ = "attendees",

    id = Column(String, primary_key=True),
    name = Column(String, nullable=False),
    email = Column(String, nullable=False),
    event = Column(String, ForeignKey=("events.id")),
    created_at = Column(DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return f""" Attendees [
            nome = {self.name},
            email = {self.email},
            event = {self.event},
            created_at = {self.created_at},
        ]"""