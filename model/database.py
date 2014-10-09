from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

import config
import game

class Database:
    def __init__(self, mode='TEST', echo=False):
        self.mode = mode
        self.Base = game.base
        self.Engine = self.get_connection(echo=echo)
        print(self.Engine)
        self.SessionMaker = sessionmaker(bind=self.Engine)
        self.Meta = MetaData()

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

