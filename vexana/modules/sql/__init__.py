import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from vexana import DB_URI, LOGGER


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    LOGGER.info("PostgreSQL Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
try:
    SESSION: scoped_session = start()
except Exception as e:
    LOGGER.exception(f"PostgreSQL Failed to connect due to {e}")
    sys.exit()

LOGGER.info("PostgreSQL Connection successful, session started.")
