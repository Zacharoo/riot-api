#!/bin/python
import requests
import time

DEV_KEY = '31081cca-7c15-4fbd-b4dc-fd9d5ee9c79e'

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


def get_item_by_id(identifier):
    base = 'http://na.api.pvp.net/api/lol/static-data/na/v1.2/item/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(identifier)
    response = requests.get(url, params=payload)
    try:
        result = response.json()
    except ValueError:
        print(response.text)
    time.sleep(1)
    return result


def get_champion_by_id(identifier):
    base = 'https://na.api.pvp.net/api/lol/na/v1.2/champion/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(identifier)
    response = requests.get(url, params=payload)
    time.sleep(1)
    try:
        result = response.json()
    except ValueError:
        print(response.text)
    return result


def get_static_about_champion(champion_id):
    base = 'https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/{}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(champion_id)
    response = requests.get(url, params=payload)
    time.sleep(1)
    try:
        result = response.json()
    except ValueError:
        print(response.text)
    return result


def get_games_by_summoner(summoner):
    base = 'https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/{0}/recent'
    payload = { 'api_key': DEV_KEY }
    url = base.format(summoner['id'])
    response = requests.get(url, params=payload)
    time.sleep(1)
    return [ game for game in response.json()['games'] ]


def get_summoner_by_name(name):
    base = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(name)
    response = requests.get(url, params=payload)
    player = None
    result = None
    time.sleep(1)
    try:
        player = response.json()
    except ValueError:
        print(response.text)

    if player:
        for key in player:
            result = player[key]
            break
    return result

if __name__ == '__main__':
    main()
