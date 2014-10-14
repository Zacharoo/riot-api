#!/bin/bash
from model.game import GameStats
import time
from api.riot_api import *

def get_item_names_by_game(game):
    items = []
    for num in range(7):
        item_num = "item{0}".format(num)
        item_id = game['stats'].get(item_num)
        if item_id:
            item_name = get_item_by_id(item_id)['name']
            time.sleep(1) 
            items.append(item_name)
        else:
            items.append(None)
    return items

def get_champ_name_from_game(game):
    champ_id    = get_champion_by_id(game['championId'])['id']
    time.sleep(1)
    champ       = get_static_about_champion(champ_id)
    time.sleep(1)
    return champ['name']

def get_win_from_game(game):
    win = game['stats']['win']
    return win

def get_blue_from_game(game):
    blue = True
    if game['teamId'] == 100:
        blue = True
    if game['teamId'] == 200:
        blue = False
    return blue

def fetch_and_store_summoner(name, db):
    summoner = get_summoner_by_name(name)
    time.sleep(1)
    games = get_games_by_summoner(summoner)
    time.sleep(1)
 
    for game in games:
        champ_name = get_champ_name_from_game(game)
        items = get_item_names_by_game(game)
        win = get_win_from_game(game) 
        blue = get_blue_from_game(game)
        summoner_name = name
 
        session = db.SessionMaker()
        session.autocommit = True
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
        print(game_stats)
        print(game)

        session.add(game_stats)
        session.commit()
        session.close()
        print(session.query(GameStats, GameStats.champion).all())

    session = db.SessionMaker()
    print(session.query(GameStats, GameStats.champion).all())

