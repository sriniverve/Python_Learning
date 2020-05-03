'''
This is to demonstrate on how to play around with json files
'''

import json
import os

#person = json.load('C:\PyCharm Projects\Python_Learning\venv\data\data_config.json')
with open('C:\\PyCharm Projects\\Python_Learning\\venv\\data\\data_config.json', 'r') as file:
    person = json.load(file)
    print(person)

