from src.models.settings.base import Base
from sqlalchemy import ForeignKey, Integer, Column, DATETIME, String
from sqlalchemy.sql import func

## Criação da tabela events com as respectivas colunas

class Check_ins(Base):
    __tablename__ = "check_ins"
    id = Column(Integer, primary_key=True),
    created_at = Column(DATETIME, nullable=False, default=func.now()),
    attendeeId = Column(String, ForeignKey=("attendees.id"))

    def __repr__(self):
        return f"check_ins [attendeeId='{self.attendeeId}']"