import requests
import time

from model.game import *
from model.mapper import *

from model.database import Database

def main():
    db = Database(mode='PROD', echo=True)
    if not db.has_tables():
        db.make_tables()
    with open('.smurfs.txt') as f:
        for line in f:
            fetch_and_store_summoner(line.strip(), db)

    session = db.SessionMaker()
    print(session.query(GameStats, GameStats.champion).all())


if __name__ == '__main__':
    main()
