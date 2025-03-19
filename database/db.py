import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

db = sa.create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=db)
Base = declarative_base()
