#!/bin/python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

base = declarative_base()

class Game(base):
    __tablename__ = 'game'

    id                  = Column(Integer, primary_key=True)
    game_mode           = Column(String)
    game_type           = Column(String)
    game_id             = Column(Integer)
    create_date         = Column(DateTime)

    game_stats          = relationship('GameStats', backref='game')

class GameStats(base):
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

class Summoner(base):
    __tablename__ = 'summoner'
    id = Column(Integer, primary_key=True)
    summoner_names = relationship('SummonerName')


class SummonerName(base):
    __tablename__ = 'summoner_name'
    name = Column(String, primary_key=True)
    id = Column(Integer, ForeignKey('summoner.id'))
    region = Column(String)
    games = relationship('GameStats')

'''
spider.make_tables()
print('The tables were made.')
def assert_tables_were_made():
    assert 'game_stats' in spider.Meta.tables.keys()
    assert 'game' in spider.Meta.tables.keys()
    assert 'summoner' in spider.Meta.tables.keys()
    assert 'summoner_name' in spider.Meta.tables.keys()
assert_tables_were_made()
'''

if __name__ == '__main__':
    make_tables()
