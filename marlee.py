from logging import fatal
import unittest
import sqlite3
import json
import requests
import os
import csv
import matplotlib
import matplotlib.pyplot as plt
import urllib3

urllib3.disable_warnings()


# def getFruitInfo():
#     url = 'https://www.fruityvice.com/api/fruit/'
#     lst_fruits = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'grapes', 'guava', 'lemon', 'lime', 'mango', 'melon', 'orange', 'papaya', 'pear', 'persimmon']
#     fruit_dict = {}
#     for fruit in lst_fruits:
#         request = requests.get(url + fruit, verify = False)
#         data = request.json()
#         nutrition_dict = {}
#         for nut_val in data:
#             if nut_val == 'nutritions':
#                 for nut in data[nut_val]:
#                     nutrition_dict[nut] = data[nut_val][nut]
#         fruit_dict[fruit] = nutrition_dict
#     return fruit_dict

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# def getFruitInfo():
#     url = 'https://www.fruityvice.com/api/fruit/'
#     lst_fruits = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'grapes', 'guava', 'lemon', 'lime', 'mango', 'melon', 'orange', 'papaya', 'pear', 'persimmon']
#     fruit_dict = {}
#     for fruit in lst_fruits:
#         request = requests.get(url + fruit, verify = False)
#         data = request.json()
#         nutrition_dict = {}
#         for nut_val in data:
#             nutrition_dict[nut_val] = data[nut_val]
#         fruit_dict[fruit] = nutrition_dict
#     return fruit_dict

def getFruitInfo(fruit):
    url = 'https://www.fruityvice.com/api/fruit/'
    request = requests.get(url + fruit, verify = False)
    data = request.json()
    nutrition_dict = {}
    for nut_val in data:
        nutrition_dict[nut_val] = data[nut_val]
    return nutrition_dict

def create_apple_table(cur, conn):
    data = getFruitInfo('apple')
    cur.execute("CREATE TABLE IF NOT EXISTS Apple (id INTEGER PRIMARY KEY, genus TEXT, name TEXT, family TEXT, ord TEXT, carbs INTEGER, pro INTEGER, fat INTEGER, cals INTEGER, sug INTEGER)")
    id = data['id']
    genus = data['genus']
    name = data['name']
    family = data['family']
    ord = data['order']
    carbs = data['nutritions']['carbohydrates']  
    pro = data['nutritions']['protein']
    fat = data['nutritions']['fat']
    cals = data['nutritions']['calories']
    sug = data['nutritions']['sugar']
    cur.execute("INSERT INTO Apple (id, genus, name, family, ord, carbs, pro, fat, cals, sug) VALUES (?,?,?,?,?,?,?,?,?,?)", (id, genus, name, family, ord, carbs, pro, fat, cals, sug))
    conn.commit()

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('fruity_vice.db')
    create_apple_table(cur, conn)
    
if __name__ == "__main__":
    main()