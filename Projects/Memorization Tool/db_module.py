from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String(100))
    answer = Column(String(50))
    box = Column(Integer, default=1)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
