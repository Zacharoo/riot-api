from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

import config
import game

import sys

class Database:
    def __init__(self, mode='TEST', echo=False):
        self.mode = mode
        self.Base = game.base
        self.Engine = self.get_connection(echo=echo)
        print(self.Engine)
        self.SessionMaker = sessionmaker(bind=self.Engine)
        self.Meta = MetaData()
        self.Meta.reflect(bind=self.Engine)
        if not self.has_tables():
            self.make_tables()

    # double check this...
    def has_tables(self):
        a = 'game_stats' in self.Meta.tables.keys()
        b = 'game' in self.Meta.tables.keys()
        c = 'summoner' in self.Meta.tables.keys()
        d = 'summoner_name' in self.Meta.tables.keys()
        if not (a and b and c and d):
            print('does not have tables already')
            return False
        print('has tables already')
        return True

    def get_connection(self, echo=False):
        engine = None
        if not self.mode == 'TEST':
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

