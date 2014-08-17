from model.game import *
import unittest
from sqlalchemy import inspect

class TestTableExistence(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        spider.make_tables()

    @classmethod
    def tearDownClass(self):
        spider.destroy_tables()

    def tearDown(self):
        spider.truncate_tables()

    def test_when_all_tables_exist(self):
        assert 'game_stats' in spider.Meta.tables.keys()
        assert 'game' in spider.Meta.tables.keys()
        assert 'summoner' in spider.Meta.tables.keys()
        assert 'summoner_name' in spider.Meta.tables.keys()

    def test_all_tables_have_rigth_columns(self):
        t = TableTester()
        test = t.has_next_table()
        while test:
            test()
            test = t.has_next_table()

class TableTester:
    def __init__(self):
        self.tables =  [ 'game', 'game_stats', 'summoner' ]
        self.expected = {
            'game':         [ 'id', 'game_mode', 'game_type', 'game_id', 'create_date' ],
            'game_stats':   [ 'id', 'summoner_name', 'champion', 'spell1', 'spell2', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'blue', 'won', 'game_id' ],
            'summoner':     [ 'id' ]
        }
        self.insp = inspect(spider.Engine)
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

