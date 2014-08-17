#!/bin/bash
import model.game
import time

def fetch_summoner(name):
    summoner = get_summoner_by_name(name)
    time.sleep(1)
    games = get_games_by_summoner(summoner)
    time.sleep(1)
    
    for game in games:
        champ_id    = get_champion_by_id(game['championId'])['id']
        time.sleep(1)
        champ       = get_static_about_champion(champ_id)
        time.sleep(1)
        item0       = get_item_by_id(game['stats']['item0'])['name']
        time.sleep(1)
        item1       = get_item_by_id(game['stats']['item1'])['name'] 
        time.sleep(1)
        item2       = get_item_by_id(game['stats']['item2'])['name']
        time.sleep(1)
        item3       = get_item_by_id(game['stats']['item3'])['name']
        time.sleep(1)
        item4       = get_item_by_id(game['stats']['item4'])['name']
        time.sleep(1)
        item5       = get_item_by_id(game['stats']['item5'])['name']
        time.sleep(1)
        item6       = get_item_by_id(game['stats']['item6'])['name']
        time.sleep(1)
        champ_name  = champ['name']
        win = game['stats']['win']
        
        blue = None
        if game['teamId'] == 100:
            blue = True
        if game['teamId'] == 200:
            blue = False

        summoner_name = name
        
        session = game.spider.SessionMaker()
        game_stats = game.GameStats(
            summoner_name = summoner_name,
            champion = champ_name,
            item0 = item0,
            item1 = item1,
            item2 = item2,
            item3 = item3,
            item4 = item4,
            item5 = item5,
            item6 = item6,
            won = win,
            blue = blue,
        )

        session.add(game_stats)
        session.commit()
        session.close()
        print(game_stats)
