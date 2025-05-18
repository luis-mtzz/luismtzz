import os
import httpx

from sqlalchemy.orm import Session
from app.models.steam import SteamUser, SteamApp

STEAM_API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")
STEAM_BASE_URL = "https://api.steampowered.com"
STEAM_PLAYER_SUMMARIES = f"{STEAM_BASE_URL}/ISteamUser/GetPlayerSummaries/v2/"
STEAM_OWNED_GAMES = f"{STEAM_BASE_URL}/IPlayerService/GetOwnedGames/v1/"

async def fetch_steam_user_summary(db: Session) -> SteamUser | None:
    """
    Fetches user summary from Steam API, updates DB, and returns user.
    """
    if not STEAM_API_KEY or not STEAM_ID:
        print("Steam API or User ID is not configured")
        return None
    
    params = {
        "key": STEAM_API_KEY,
        "steamids": STEAM_ID
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(STEAM_PLAYER_SUMMARIES, params=params)
            response.raise_for_status()
        
        data = response.json()
        player_data = data.get("response", {}).get("players", [])[0]
        if not player_data:
            return None
        steam_user = db.query(SteamUser).filter(SteamUser.steamid == int(player_data["steamid"])).first()
        user_details = {
            "steamid": int(player_data["steamid"]),
            "personaName": player_data["personaname"],
            "profileURL": player_data["profileurl"],
            "avatar": player_data["avatarfull"],
            "timeCreated": player_data.get("timecreated", 0)
        }
        if steam_user:
            for key, value in user_details.items():
                setattr(steam_user, key, value)
        else:
            steam_user = SteamUser(**user_details)
            db.add(steam_user)

        db.commit()
        db.refresh(steam_user)
        return steam_user

    except httpx.HTTPStatusError as err:
        print(f"HTTP error fetching user summary: {err.response.status_code} - {err.response.text}")
        return None
    except Exception as exc:
        print(f"An unknown error occured: {exc}")
        db.rollback()
        return None
    
async def fetch_steam_owned_games(db: Session) -> list[SteamApp]:
    """
    Fetches owned games from SteamAPI, updates DB, and returns list of apps.
    """
    if not STEAM_API_KEY or not STEAM_ID:
        print("Steam API or User ID is not configured")
        return []
    params = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID,
        "include_appinfo": True,
        "skip_unvetted_apps": True,
        "include_extended_appinfo": False
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(STEAM_OWNED_GAMES, params=params)
            response.raise_for_status()
        data = response.json()
        games_data = data.get("response", {}).get("games", [])
        updated_apps = []
        for game_data in games_data:
            app_details = {
                "appid": game_data["appid"],
                "appName": game_data.get("name", f"AppID {game_data['appid']}"),
                "playtime": game_data.get("playtime_forever", 0),
                "lastPlayed": game_data.get("rtime_last_played", 0)
            }
            steam_app = db.query(SteamApp).filter(SteamApp.appid == app_details["appid"]).first()
            if steam_app:
                steam_app.appName = app_details["appName"]
                steam_app.playtime = app_details["playtime"]
                steam_app.lastPlayed = app_details["lastPlayed"]
            else:
                steam_app = SteamApp(**app_details)
                db.add(steam_app)
            updated_apps.append(steam_app)
        db.commit()
        for app in updated_apps:
            db.refresh(app)
        return updated_apps
    except httpx.HTTPStatusError as err:
        print(f"HTTP error fetching owned Steam games: {err.response.status_code} - {err.response.text}")
        return []
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}")
        db.rollback()
        return []

def steam_user_from_db(db: Session) -> SteamUser | None:
    """Retrieve Steam user from DB."""
    return db.query(SteamUser).filter(SteamUser.steamid == int(STEAM_ID)).first() if STEAM_ID else None

def get_steam_apps_from_db(db: Session) -> list[SteamApp]:
    """Retrieve all steam apps from DB."""
    return db.query(SteamApp).order_by(SteamApp.lastPlayed.desc()).all()