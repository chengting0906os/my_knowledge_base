from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    id         = Column(Integer, primary_key=True)
    user_id    = Column(Integer, nullable=False)
    title      = Column(String(300), nullable=False)
    body       = Column(Text, nullable=False)
    word_count = Column(Integer, nullable=False)   # computed during transform


def get_engine(db_url: str = "sqlite:///etl.db"):
    return create_engine(db_url, echo=False)


def init_db(engine) -> None:
    Base.metadata.create_all(engine)
