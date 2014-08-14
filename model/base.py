#!/bin/python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    
    def __repr__(self):
        return "<User(first='%s', last='%s', password='%s')>" % (self.first_name, self.last_name, self.password)


Base.metadata.create_all(engine)
ed_user = User(first_name='Robbie', last_name='McKinstry', password='password')
print(ed_user)

from sqlalchemy.orm import sessionmaker
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()
session.add(ed_user)
our_user = session.query(User).filter_by(first_name='Robbie').first()
print(our_user)
