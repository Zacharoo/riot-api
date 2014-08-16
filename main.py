import requests
import time

from model.game import *

DEV_KEY= '31081cca-7c15-4fbd-b4dc-fd9d5ee9c79e'

def main():

#    make_tables()

    def test_on_lustboy():
        lustboy = get_summoner_by_name('TSM LUSTBOY')
        games = get_games_by_summoner(lustboy)

        for game in games:
            champ_id = get_champion_by_id(game['championId'])['id']
            champ = get_static_about_champion(champ_id)
    
            item0_id = game['stats']['item0']
            item0 = get_item_by_id(item0_id)

            print(champ['name'])
            print(item0['name'])
            time.sleep(2.5)

    test_on_lustboy()


    # TODO test get_team_by_id
    def get_team_by_id(identifier):
        base = 'http://na.api.pvp.net/api/lol/na/v2.3/team/{0}'
        payload = { 'api_key': DEV_KEY }
        url = base.format(identifer)
        response = requests.get(url, params=payload)
        return response.json()

def get_item_by_id(identifier):
    base = 'http://na.api.pvp.net/api/lol/static-data/na/v1.2/item/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(identifier)
    response = requests.get(url, params=payload)
    return response.json()

def get_champion_by_id(identifier):
    base = 'https://na.api.pvp.net/api/lol/na/v1.2/champion/{0}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(identifier)
    response = requests.get(url, params=payload)
    return response.json()

def get_static_about_champion(champion_id):
    base = 'https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/{}'
    payload = { 'api_key': DEV_KEY }
    url = base.format(champion_id)
    response = requests.get(url, params=payload)
    return response.json()

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
    player = response.json()
    for key in player:
        result = player[key]
        break
    return result

if __name__ == '__main__':
    main()
