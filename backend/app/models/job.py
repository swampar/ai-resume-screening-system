from sqlalchemy import Column, Integer, String, Text
from app.database.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    company = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    skills = Column(Text)