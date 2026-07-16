"""
SQLAlchemy engine + session management.

Using SQLite by default (file-based, zero setup) but since we only
talk to the DB through SQLAlchemy's ORM layer, swapping DATABASE_URL
for Postgres/MySQL later requires no code changes elsewhere.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    # Needed only for SQLite to allow usage across FastAPI's threadpool
    connect_args = {"check_same_thread": False}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a DB session and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
