from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    location = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    github_url = Column(String(256), nullable=True)
    linkedin_url = Column(String(256), nullable=True)
    resume_url = Column(String(256), nullable=True)

    def __repr__(self):
        return f"<Profile(id={self.id!r}, name={self.name!r}, github_url={self.github_url!r})"