"""
Reusable FastAPI dependencies for authentication & authorization.

`get_current_user` is the workhorse: any protected route just adds
`current_user: User = Depends(get_current_user)` to its signature and
FastAPI + Swagger UI automatically wire up the "Authorize" button.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_token
from app.database import get_db
from app.models.user import User
from app.models.token_blacklist import BlacklistedToken

# tokenUrl is only used by Swagger UI to know where to POST for a token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    # Reject tokens that were explicitly logged out (bonus: blacklist)
    if db.query(BlacklistedToken).filter(BlacklistedToken.token == token).first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been revoked, please log in again",
        )

    payload = decode_token(token)
    if payload is None or payload.get("type") != "access":
        raise CREDENTIALS_EXCEPTION

    user_id: str | None = payload.get("sub")
    if user_id is None:
        raise CREDENTIALS_EXCEPTION

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise CREDENTIALS_EXCEPTION
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")

    return user


def get_current_active_admin(current_user: User = Depends(get_current_user)) -> User:
    """Guard for admin-only routes (bonus: RBAC)."""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions - admin role required",
        )
    return current_user
