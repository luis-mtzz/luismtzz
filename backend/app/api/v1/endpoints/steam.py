from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.steam import SteamAppSchema, SteamUserSchema
from app.services import steam_service
from app.db.session import get_db

router = APIRouter()

@router.get("/steam/user", response_model=SteamUserSchema)
async def read_steam_user(db: Session = Depends(get_db)):
    user = steam_service.get_steam_apps_from_db(db)
    if not user:
        user = await steam_service.fetch_steam_user_summary(db)
    if not user:
        raise HTTPException(status_code=404, detail="Steam user not found or API error.")
    return user

@router.get("/steam/apps", response_model=List[SteamAppSchema])
async def read_steam_apps(db: Session = Depends(get_db)):
    apps = steam_service.get_steam_apps_from_db(db)
    if not apps:
        apps = await steam_service.fetch_steam_owned_games(db)
    if not apps:
        raise HTTPException(status_code=404, detail="Steam apps not found or API error.")
    return apps

@router.post("/steam/refresh", summary="Refresh Steam data from API.")
async def refresh_steam_data(db: Session = Depends(get_db)):
    user = await steam_service.fetch_steam_user_summary(db)
    apps = await steam_service.fetch_steam_owned_games(db)
    if not user or not apps:
        raise HTTPException(status_code=500, detail="Failed to refresh Steam data.")
    return {
        "message": "Steam data refreshed.",
        "user": user.personaName,
        "app_count": len(apps)
    }
