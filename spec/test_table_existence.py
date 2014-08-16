from model.game import *
import unittest

class TestTableExistence(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        make_tables()

    def test_works(self):
        assert True, 'Failed?'

    def test_game_stats_exists(self):
        engine.dialect.has_table(engine.connect(), "game_stats")

    def test_game_exists(self):
        engine.dialect.has_table(engine.connect(), "game")

    def test_summoner_exists(self):
        engine.dialect.has_table(engine.connect(), "summoner")

    def test_summoner_name_exists(self):
        engine.dialect.has_table(engine.connect(), "summoner_name")

if __name__ == '__main__':
    unittest.main()

