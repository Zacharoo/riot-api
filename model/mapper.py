#!/bin/bash
import model.game as spider_den
import time
from api.riot_api import *

def fetch_summoner(name):
    summoner = get_summoner_by_name(name)
    time.sleep(1)
    games = get_games_by_summoner(summoner)
    time.sleep(1)
 
    for game in games:
        print(game)
        champ_id    = get_champion_by_id(game['championId'])['id']
        time.sleep(1)
        champ       = get_static_about_champion(champ_id)
        time.sleep(1)


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

        champ_name  = champ['name']
        win = game['stats']['win']
        
        blue = None
        if game['teamId'] == 100:
            blue = True
        if game['teamId'] == 200:
            blue = False

        summoner_name = name
 
        session = spider_den.spider.SessionMaker()
        game_stats = spider_den.GameStats(
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
        print('Now printing the sorted tables!')
        print(spider_den.spider.Meta.sorted_tables)
        print('\n')
        session.add(game_stats)
        session.commit()
