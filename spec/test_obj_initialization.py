from model.game import *
from spec.support.support import *
from sqlalchemy import inspect

import unittest
import datetime

class TestObjectInitialization(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        spider.make_tables()

    @classmethod
    def tearDownClass(self):
        spider.destroy_tables()

    def tearDown(self):
        spider.truncate_tables() 
    
    def test_when_game_is_made(self):
        session = spider.SessionMaker()

        def query_for_game(session):
            return session.query(Game).first()
        
        expected = add_a_game(session)
        observed = query_for_game(session)
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

    def test_when_game_stats_is_made(self):
        session = spider.SessionMaker()

        def query_for_game_stats():
            return session.query(GameStats).filter_by(summoner_name='Bjerson').first()

        expected = add_game_stats(session)
        observed = query_for_game_stats()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

    def test_when_summoner_is_made(self):
        session = spider.SessionMaker()

        def query_for_summoner():
            return session.query(Summoner).first()

        expected = add_a_summoner(session)
        observed = query_for_summoner()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)


    def test_when_summoner_name_is_made(self):
        session = spider.SessionMaker()

        def query_for_summoner_name():
            return session.query(SummonerName).first()

        expected = add_a_summoner_name(session)
        observed = query_for_summoner_name()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

    def test_when_they_work_together(self):
        pass    


if __name__ == '__main__':
    unittest.main()

