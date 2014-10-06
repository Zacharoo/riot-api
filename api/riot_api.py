#!/bin/python
import requests

DEV_KEY = '31081cca-7c15-4fbd-b4dc-fd9d5ee9c79e'

def get_item_by_id(identifier):
    base = 'http://na.api.pvp.net/api/lol/static-data/na/v1.2/item/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(identifier)
    response = requests.get(url, params=payload)
    try:
        result = response.json()
    except ValueError:
        print(response.text)
    return result

def get_champion_by_id(identifier):
    base = 'https://na.api.pvp.net/api/lol/na/v1.2/champion/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(identifier)
    response = requests.get(url, params=payload)

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

    return [ game for game in response.json()['games'] ]

def get_summoner_by_name(name):
    base = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(name)
    response = requests.get(url, params=payload)
    player = None
    result = None
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
