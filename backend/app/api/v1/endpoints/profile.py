import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.schemas.profile import Profile as ProfileSchema
from app.schemas.profile import ProfileUpdate
from app.services.profile_service import get_profile, update_profile
from app.db.session import get_db

router = APIRouter()
security = HTTPBearer()

def verify_admin_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> None:
    admin_token = os.getenv("ADMIN_TOKEN")
    if not admin_token or credentials.credentials != admin_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing admin token."
        )

@router.get("/profile", response_model=ProfileSchema)
def read_profile(db: Session = Depends(get_db)):
    """
    Public: Fetch profile info
    """
    profile = get_profile(db)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found.")

@router.put("/profile", response_model=ProfileUpdate, dependencies=[Depends(verify_admin_token)])
def update_profile_endpoint(profile_in: ProfileUpdate, db: Session = Depends(get_db)):
    """
    Protected: Update profile info. Requires Bearer token in Auth header.
    """
    updated = update_profile(db, profile_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Profile not found.")
    return updated