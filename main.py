import requests
import time

from model.game import *
from model.mapper import *

DEV_KEY= '31081cca-7c15-4fbd-b4dc-fd9d5ee9c79e'

def main():

    make_tables()
    fetch_summoner('TSM LUSTBOY')

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
        

#    test_on_lustboy()


    # TODO test get_team_by_id
    def get_team_by_id(identifier):
        base = 'http://na.api.pvp.net/api/lol/na/v2.3/team/{0}'
        payload = { 'api_key': DEV_KEY }
        url = base.format(identifer)
        response = requests.get(url, params=payload)
        return response.json()


