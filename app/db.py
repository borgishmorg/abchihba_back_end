from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .settings import settings


engine = create_engine(
    settings.DB_DSN,
    echo=True
)
session_factory = sessionmaker(
    bind=engine,
    autoflush=True
)


def session_scope():
    session: Session = session_factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
