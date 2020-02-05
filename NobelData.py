# Author: Zihan Li
# Date: 2020/2/4
# Description: a class named NobelData that reads a JSON file containing data on Nobel Prizes
#              and allows the user to search that data

import json
import requests

class NobelData:
    def __init__(self):
        response = requests.get("http://api.nobelprize.org/v1/prize.json")
        self.data = response.json()
        # an init method that reads from the web

    def search_nobel(self, year, category):
        p = len(self.data['prizes'])
        winner = []
        # initialize winner
        for i in range(0, p):
            if (self.data['prizes'][i]['year'] == year and self.data['prizes'][i]['category'] == category):
                winner = self.data['prizes'][i]['laureates']
                # use loop to search the year and category
                break

        w = len(winner)
        winner_surname = []
        # initialize winner's surname
        for j in range(0, w):
            winner_surname.append(winner[j]['surname'])
            # use loop to search winner's surname
        winner_surname.sort()
        # in normal dictionary order
        return winner_surname
