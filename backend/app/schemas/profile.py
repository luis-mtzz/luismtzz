from pydantic import BaseModel, HttpUrl
from typing import Optional

class Profile(BaseModel):
    id: int
    name: str
    location: Optional[str] = None
    bio: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None
    resume_url: Optional[str] = None

    class Config:
        from_attributes = True

class ProfileUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None
    resume_url: Optional[str] = None

    class Config:
        from_attributes = True