from pydantic import BaseModel, HttpUrl
from typing import Optional

class SteamUserSchema(BaseModel):
    steamid: int
    personaName: str
    profileURL: Optional[HttpUrl] = None
    avatar: Optional[HttpUrl]
    timeCreated: int

    class Config:
        from_attributes = True

class SteamAppSchema(BaseModel):
    appid: int
    appName: str
    playtime: int
    lastPlayed: int

    class Config:
        from_attributes = True