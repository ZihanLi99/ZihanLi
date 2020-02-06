# Author: Zihan Li
# Date: 2020/2/4
# Description: a class named SatData that reads a JSON file containing data on 2010 SAT results for New York City
#              and writes the data to a text file in CSV (comma-separated values) format

import json

class SatData:
    def __init__(self):
        super().__init__()
        self.idmap = {}
        # declare a dict to store id and row
        
        with open('sat.json', 'r') as infile:
            self.data = json.load(infile)
            for row in self.data['data']:
                id = row[8]
                # get it's id and store it to idmap for each row
                self.idmap[id] = row

    def save_as_csv(self, dbns):
        columns = ['DBN','School Name','Number of Test Takers','Critical Reading Mean','Mathematics Mean','Writing Mean']
        # save columns
        with open('output.csv', 'w') as outfile:
            outfile.write(','.join(columns) +"\n")
            # open file for write
            for dbn in dbns:
                if dbn in self.idmap:
                    line = ','.join(self.idmap[dbn][8:])
                    # read column values, generate a record
                    outfile.write(line +'\n')
                    # write to csv file
