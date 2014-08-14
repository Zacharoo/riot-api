#!/bin/python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
SessionMaker = sessionmaker(bind=engine)

class Game(Base):
    __tablename__ = 'game'

    id                  = Column(Integer, primary_key=True)
    game_mode           = Column(String)
    game_type           = Column(String)
    game_id             = Column(Integer)
    game_association_id = Column(Integer, ForeignKey('game_association.id'))
    create_data         = Column(DateTime)



class GameAssociation(Base):
    __tablename__ = 'game_association'

    id      = Column(Integer, primary_key=True)
    player0 = Column(Integer, ForeignKey('game_stats.id'))
    player1 = Column(Integer, ForeignKey('game_stats.id'))
    player2 = Column(Integer, ForeignKey('game_stats.id'))
    player3 = Column(Integer, ForeignKey('game_stats.id'))
    player4 = Column(Integer, ForeignKey('game_stats.id'))
    player5 = Column(Integer, ForeignKey('game_stats.id'))
    player6 = Column(Integer, ForeignKey('game_stats.id'))
    player7 = Column(Integer, ForeignKey('game_stats.id'))
    player8 = Column(Integer, ForeignKey('game_stats.id'))
    player9 = Column(Integer, ForeignKey('game_stats.id'))

class GameStats(Base):
    __tablename__ = 'game_stats'

    id              = Column(Integer, primary_key=True)
    summoner_name   = Column(String)
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

#class Summoner(Base):
#    __tablename__ = 'summoner'
#
#    summoner_name = Column(String, primary_key=True)
#    team_name = Column(String)
#    alternative_names_id = Column(Integer) # hmmm, this should be managed by sqlalchemy

def make_tables():
    Base.metadata.create_all(engine)
    print('Ravioli! Ravioli! Give me the formuoli!')
