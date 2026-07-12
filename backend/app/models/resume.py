from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))
    filepath = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))