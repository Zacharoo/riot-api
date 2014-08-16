from model.game import *
import unittest
from sqlalchemy import inspect

class TestTableExistence(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        make_tables()

    def test_game_stats_exists(self):
        assert 'game_stats' in meta_data.tables.keys()

    def test_game_exists(self):
        assert 'game' in meta_data.tables.keys()

    def test_summoner_exists(self):
        assert 'summoner' in meta_data.tables.keys()

    def test_summoner_name_exists(self):
        assert 'summoner_name' in meta_data.tables.keys()

    def test_when_game_has_right_columns(self):
        insp = inspect(engine)
        columns = insp.get_columns('game')
        assert len(columns) == 5, '{0}'.format(len(columns)) 
        expected = [ 'id', 'game_mode', 'game_type', 'game_id', 'create_date' ]
        for column in columns:
            assert column['name'] in expected, 'Couldn\' find the column name found among those expected.\n {0}'.format(column['name'])

    def test_all_tables(self):
        t = TableTester()
        test = t.has_next_table()
        while test:
            test()
            test = t.has_next_table()

        #suite = unittest.TestSuite()
        #test = t.has_next_table()
        #while test:
        #    suite.addTest(test)
        #    test = t.has_next_table()
        #
        #unittest.TextTestRunner(verbosity=2).run(suite)

class TableTester:
    def __init__(self):
        self.tables =  [ 'game', 'game_stats', 'summoner' ]
        self.expected = {
            'game':         [ 'id', 'game_mode', 'game_type', 'game_id', 'create_date' ],
            'game_stats':   [ 'id', 'summoner_name', 'champion', 'spell1', 'spell2', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'blue', 'won', 'game_id' ],
            'summoner':     [ 'id' ]
        }
        self.insp = inspect(engine)
        self.x = 0
 
    def has_next_table(self):
        if self.x >= len(self.tables):
            return None
        else:
            def next_table():
                table = self.tables[self.x]
                self.x += 1
                desired_columns = self.expected[table]
                columns = self.insp.get_columns(table)
                for column in columns:
                    assert column['name'] in desired_columns, 'Looking for {0} in table {1}:\n{2}'.format(column['name'], table, columns)
            return lambda: next_table()
if __name__ == '__main__':
    unittest.main()

