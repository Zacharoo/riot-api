import requests
import time

from model.game import *
from model.mapper import *

def main():
    fetch_summoner('thesnowmancometh')
#    with open('.smurfs.txt') as f:
#        for line in f:
#            fetch_summoner(line)

if __name__ == '__main__':
    main()
