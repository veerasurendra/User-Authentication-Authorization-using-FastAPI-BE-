from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime

from app.database import Base


class BlacklistedToken(Base):
    """
    Stores JTIs (or raw tokens, for simplicity here) that have been
    explicitly logged out / revoked before their natural expiry.
    """
    __tablename__ = "blacklisted_tokens"

    token = Column(String, primary_key=True, index=True)
    blacklisted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
