from model.game import *
import unittest
from sqlalchemy import inspect
import datetime

class TestObjectInitialization(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        make_tables()

    @classmethod
    def tearDownClass(self):
        meta_data.drop_all(engine)

    def test_thing(self):
        assert 2*3 == 6
        s = Summoner()

    def test_when_game_is_made(self):
        session = SessionMaker()
        def add_a_game():
            game = Game(
                game_mode   = 'CLASSIC',
                game_type   = 'MATCHED_GAME',
                game_id     = 100100100101,
                create_date = datetime.datetime.now(),
            )
            session.add(game)
            session.commit()
            return game

        def query_for_game():
            return session.query(Game).filter_by(game_id=100100100101).first()
        
        expected = add_a_game()
        observed = query_for_game()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

if __name__ == '__main__':
    unittest.main()

