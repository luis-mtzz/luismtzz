from sqlalchemy import Column, Integer, String, BigInteger
from app.db.base import Base

class SteamUser(Base):
    __tablename__ = "steamUser"
    steamid = Column(BigInteger, primary_key=True, index=True)
    personaName = Column(String(10), nullable=False)
    profileURL = Column(String(100), nullable=False)
    avatar = Column(String(200), nullable=True)
    timeCreated = Column(BigInteger, nullable=False)

    def __repr__(self):
        return f"<SteamUser(steamid={self.steamid!r}, personaName(personaName={self.personaName!r}))"
    
class SteamApp(Base):
    __tablename__ = "steamApp"
    appid = Column(BigInteger, primary_key=True, index=True)
    appName = Column(String(100), nullable=False)
    playtime = Column(Integer, default=0, nullable=False)
    lastPlayed = Column(BigInteger, default=0, nullable=False)

    def __repr__(self):
        hours = self.playtime // 60
        minutes = self.playtime % 60
        match (hours, minutes):
            case (0, m):
                playtime = f"{m}m"
            case (h, 0):
                playtime = f"{h}h"
            case (h, m):
                playtime = f"{h}h {m}m"
        return f"<SteamApp(appid={self.appid!r}, appName={self.appName!r}, playtime={playtime!r})"