"""
database.py — SQLAlchemy engine, session factory, and dependency.

Why: We create the engine once from the .env settings, then produce
short-lived sessions per request using a dependency (get_db). This
prevents connection leaks — the session is always closed in the
finally block even if an error occurs mid-request.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings

# Build the MySQL connection URL from .env values.
# PyMySQL is the pure-Python driver (no C extension needed on Windows).
DATABASE_URL = (
    f"mysql+pymysql://{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    f"?charset=utf8mb4"
)

# pool_pre_ping=True re-checks connections that have been idle,
# avoiding "MySQL has gone away" errors after long inactivity.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800,   # recycle connections after 30 minutes
    echo=False,          # set True temporarily to log all SQL
)

# SessionLocal is a factory: each call creates a new session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Base class that all ORM models will inherit from."""
    pass


def get_db():
    """
    FastAPI dependency that yields a database session.
    Usage in a router:  db: Session = Depends(get_db)
    The session is closed automatically after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
