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

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def getFruitInfo(fruit):
    url = 'https://www.fruityvice.com/api/fruit/'
    request = requests.get(url + fruit, verify = False)
    data = request.json()
    nutrition_dict = {}
    for nut_val in data:
        nutrition_dict[nut_val] = data[nut_val]
    return nutrition_dict

# def create_apple_table(cur, conn):
#     data = getFruitInfo('apple')
#     cur.execute("CREATE TABLE IF NOT EXISTS Apple (id INTEGER PRIMARY KEY, genus TEXT, name TEXT, family TEXT, ord TEXT, carbs INTEGER, pro INTEGER, fat INTEGER, cals INTEGER, sug INTEGER)")
#     id = data['id']
#     genus = data['genus']
#     name = data['name']
#     family = data['family']
#     ord = data['order']
#     carbs = data['nutritions']['carbohydrates']  
#     pro = data['nutritions']['protein']
#     fat = data['nutritions']['fat']
#     cals = data['nutritions']['calories']
#     sug = data['nutritions']['sugar']
#     cur.execute("INSERT INTO Apple (id, genus, name, family, ord, carbs, pro, fat, cals, sug) VALUES (?,?,?,?,?,?,?,?,?,?)", (id, genus, name, family, ord, carbs, pro, fat, cals, sug))
#     conn.commit()

def create_fruit_table(fruit, cur, conn):
    data = getFruitInfo(str(fruit))
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fruit} (id INTEGER PRIMARY KEY, genus TEXT, name TEXT, family TEXT, ord TEXT, carbs INTEGER, pro INTEGER, fat INTEGER, cals INTEGER, sug INTEGER)")
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
    cur.execute(f"INSERT OR REPLACE INTO {fruit} (id, genus, name, family, ord, carbs, pro, fat, cals, sug) VALUES (?,?,?,?,?,?,?,?,?,?)", (id, genus, name, family, ord, carbs, pro, fat, cals, sug))
    conn.commit()

# def calculate_carbs(cur, conn):



def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('fruity_vice.db')
    lst_fruits = ['Apple', 'Apricot', 'Banana', 'Blueberry', 'Lemon', 'Lime', 'Mango', 'Orange', 'Papaya', 'Pear']
    for fruit in lst_fruits:
        create_fruit_table(fruit, cur, conn)

if __name__ == "__main__":
    main()