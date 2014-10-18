#!/bin/bash
from model.game import GameStats
from api.riot_api import *

def fetch_and_store_summoner(name, db):
    def make_game_stats_from_game(game):
        champ_name = get_champ_name_from_game(game)
        items = get_item_names_by_game(game)
        win = get_win_from_game(game) 
        blue = get_blue_from_game(game)
        summoner_name = name

        game_stats = GameStats(
            summoner_name = summoner_name,
            champion = champ_name,
            item0 = items[0],
            item1 = items[1],
            item2 = items[2],
            item3 = items[3],
            item4 = items[4],
            item5 = items[5],
            item6 = items[6],
            won = win,
            blue = blue,
        )
        return game_stats

        
    summoner = get_summoner_by_name(name)
    games = get_games_by_summoner(summoner)
 
    for game in games:
        game_stats = make_game_stats_from_game(game)
        session = db.SessionMaker()
               
        """
        # make a new game object
        db_game = Game( 
            game_mode = , # insert the game mode ???
            game_type = , # game type ???
            game_id = ,   # this is the riot id
            create_date = , # err... datetime of the game
            game_stats = game_stats,
        )
        """
        print(game_stats)
        print(game)

        session.add(game_stats)
        session.commit()
        session.close()
        print(session.query(GameStats, GameStats.champion).all())

    session = db.SessionMaker()
    print(session.query(GameStats, GameStats.champion).all())

