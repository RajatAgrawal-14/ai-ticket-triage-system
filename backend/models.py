from sqlalchemy import Column, Integer, String, Float
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    category = Column(String)
    priority = Column(String)
    confidence = Column(Float)
