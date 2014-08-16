#!/bin/python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine, MetaData
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///:memory:')
SessionMaker = sessionmaker(bind=engine)
meta_data = MetaData()

class Game(Base):
    __tablename__ = 'game'

    id                  = Column(Integer, primary_key=True)
    game_mode           = Column(String)
    game_type           = Column(String)
    game_id             = Column(Integer)
    create_date         = Column(DateTime)

    game_stats          = relationship('GameStats', backref='game')

class GameStats(Base):
    __tablename__ = 'game_stats'

    id              = Column(Integer, primary_key=True)
    summoner_name   = Column(String, ForeignKey('summoner_name.name'))
    champion        = Column(String)
    spell1          = Column(String)
    spell2          = Column(String)
    item0           = Column(String)
    item1           = Column(String)
    item2           = Column(String)
    item3           = Column(String)
    item4           = Column(String)
    item5           = Column(String)
    item6           = Column(String)
    blue            = Column(Boolean)
    won             = Column(Boolean)

    game_id         = Column(Integer, ForeignKey('game.id'))

class Summoner(Base):
    __tablename__ = 'summoner'
    id = Column(Integer, primary_key=True)
    summoner_names = relationship('SummonerName')


class SummonerName(Base):
    __tablename__ = 'summoner_name'
    name = Column(String, primary_key=True)
    id = Column(Integer, ForeignKey('summoner.id'))
    region = Column(String)
    games = relationship('GameStats')


def make_tables():
    Base.metadata.create_all(engine)
    meta_data.reflect(bind=engine)

if __name__ == '__main__':
    make_tables()
