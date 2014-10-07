#!/bin/python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine, MetaData
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref

# import config TODO actually use this
import sys

class Database:
    def __init__(self):
        self.Base = declarative_base()
        self.Engine = self.get_connection()
        self.SessionMaker = sessionmaker(bind=self.Engine)
        self.Meta = MetaData()

    def get_connection(self, echo=False):
        engine = None
        if sys.argv[1]:
            engine = create_engine('sqlite:///.data.sqlite')
        else:
            engine = create_engine('sqlite:///:memory:', echo=echo)
        return engine


    def make_tables(self):
        self.Base.metadata.create_all(self.Engine)
        self.Meta.reflect(bind=self.Engine)

    def destroy_tables(self):
        self.Meta.drop_all(self.Engine)

    def truncate_tables(self):
        conn = self.Engine.connect()
        trans = conn.begin()
        for table in self.Meta.sorted_tables:
            conn.execute(table.delete())
        trans.commit()
        conn.close()

spider = Database()

class Game(spider.Base):
    __tablename__ = 'game'

    id                  = Column(Integer, primary_key=True)
    game_mode           = Column(String)
    game_type           = Column(String)
    game_id             = Column(Integer)
    create_date         = Column(DateTime)

    game_stats          = relationship('GameStats', backref='game')

class GameStats(spider.Base):
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

class Summoner(spider.Base):
    __tablename__ = 'summoner'
    id = Column(Integer, primary_key=True)
    summoner_names = relationship('SummonerName')


class SummonerName(spider.Base):
    __tablename__ = 'summoner_name'
    name = Column(String, primary_key=True)
    id = Column(Integer, ForeignKey('summoner.id'))
    region = Column(String)
    games = relationship('GameStats')


spider.make_tables()
print('The tables were made.')
def assert_tables_were_made():
    assert 'game_stats' in spider.Meta.tables.keys()
    assert 'game' in spider.Meta.tables.keys()
    assert 'summoner' in spider.Meta.tables.keys()
    assert 'summoner_name' in spider.Meta.tables.keys()
assert_tables_were_made()


if __name__ == '__main__':
    make_tables()
