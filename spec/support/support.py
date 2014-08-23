#!/bin/python

from model.game import Summoner, SummonerName, GameStats, Game

def add_a_summoner(session):
    summoner = Summoner()
    session.add(summoner)
    session.commit()
    return summoner

def add_a_summoner_name(session):
    summoner_name = SummonerName(name='seven_nation_gnarmy', region='na')
    session.add(summoner_name)
    session.commit()
    return summoner_name

def add_a_game(session):
    game = Game()
    session.add(game)
    session.commit()
    return game

def add_game_stats(session):
    game_stats = GameStats(
        summoner_name = 'Bjerson',
        champion = 'Garen',
        spell1 = 'Ignite',
        spell2 = 'Flash',
        item0 =  'Bork',
        blue = True,
        won = True,
    )    
    session.add(game_stats)
    session.commit()
    return game_stats

if __name__ == '__main__':
    print('No main function in this module.')
