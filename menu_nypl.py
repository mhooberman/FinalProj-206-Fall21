
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

def getDishInfo():
    url = 'http://api.menus.nypl.org/dishes?token='
    token = 'r6g4jg2ihzhad4xsjknj3lnr7u'
    request = requests.get(url + token, verify = False)
    data = request.json()
    data_dict = {}
    for d in data:
        data_dict[d] = data[d]
    return data_dict


def create_dish_table(cur, conn):
    dish_dict = getDishInfo()
    cur.execute("CREATE TABLE IF NOT EXISTS Dishes (id INTEGER PRIMARY KEY, name TEXT, menus_appeared INTEGER, times_appeared INTEGER, first_appeared INTEGER, last_appeared INTEGER, lowest_price INTEGER, highest_price INTEGER)")
    for d in dish_dict['dishes']:
        id = d['id']
        name = d['name']
        menus_appeared = d['menus_appeared']
        times_appeared = d['times_appeared']
        first_appeared = d['first_appeared']
        last_appeared = d['last_appeared']
        lowest_price = d['lowest_price']
        highest_price = d['highest_price']
        cur.execute("INSERT OR REPLACE INTO Dishes (id, name, menus_appeared, times_appeared, first_appeared, last_appeared, lowest_price, highest_price) VALUES (?,?,?,?,?,?,?,?)", (id, name, menus_appeared, times_appeared, first_appeared, last_appeared, lowest_price, highest_price))
    conn.commit()

def calculuate_expensive_dishes(cur, conn):
    data = cur.execute("SELECT name, highest_price FROM Dishes").fetchall()
    conn.commit()
    
    dish_prices = []
    for tup in data:
        if tup[1] != None:
            price = float(tup[1].strip('$'))
            dish_prices.append((tup[0], price))
        else:
            continue
    sorted_dish_prices = sorted(dish_prices, key = lambda x: x[1], reverse = True)
    print(sorted_dish_prices)
    return sorted_dish_prices

def main():
    cur, conn = setUpDatabase('menus.db')
    create_dish_table(cur, conn)
    calculuate_expensive_dishes(cur, conn)

if __name__ == "__main__":
    main()