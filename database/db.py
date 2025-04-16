import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

db = sa.create_engine(
    "sqlite:///:memory:", echo=True, connect_args={"check_same_thread": False}
)
Session = sessionmaker(bind=db)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
