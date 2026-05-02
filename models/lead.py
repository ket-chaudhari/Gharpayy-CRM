from sqlalchemy import Column, Integer, String
from database.db import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone = Column(String, unique=True)
    email = Column(String, unique=True)
    preferred_location = Column(String)
    budget = Column(String)
    status = Column(String, default="New")
    source = Column(String)
    assigned_agent = Column(String)
    notes = Column(String)