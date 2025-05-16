from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import Profile as ProfileSchema
from app.schemas.profile import ProfileUpdate

def get_profile(db: Session) -> Profile | None:
    """Retrieve the single profile (returns first row or None)."""
    return db.query(Profile).first()

def create_profile(db: Session, profile_in: ProfileSchema) -> Profile:
    """Create profile row. Should only be used once."""
    db_profile = Profile(
        name=profile_in.name,
        bio=profile_in.bio,
        location=profile_in.location if profile_in.location else None,
        github_url=str(profile_in.github_url) if profile_in.github_url else None,
        linkedin_url=str(profile_in.linkedin_url) if profile_in.linkedin_url else None,
        resume_url=str(profile_in.resume_url) if profile_in.resume_url else None
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile_in: ProfileUpdate) -> Profile | None:
    """Updates existing profile with new data."""
    db_profile = db.query(Profile).filter(Profile.id == profile_in.id).first()
    if db_profile is None:
        return None
    if profile_in.name is not None:
        setattr(db_profile, "name", profile_in.name)
    if profile_in.bio is not None:
        setattr(db_profile, "bio", profile_in.bio)
    if profile_in.location is not None:
        setattr(db_profile, "location", profile_in.location)
    if profile_in.github_url is not None:
        setattr(db_profile, "github_url", str(profile_in.github_url))
    if profile_in.linkedin_url is not None:
        setattr(db_profile, "linkedin_url", str(profile_in.linkedin_url))
    if profile_in.resume_url is not None:
        setattr(db_profile, "resume_url", str(profile_in.resume_url))
    db.commit()
    db.refresh(db_profile)
    return db_profile