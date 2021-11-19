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


# def getFruitInfo(fruit):
#     url = 'https://www.fruityvice.com/api/fruit/'
#     request = requests.get(url + fruit, verify = False)
#     data = request.json()
#     print(data)
#     nutrition_dict = {}
#     for nut_val in data:
#         nutrition_dict[nut_val] = data[nut_val]
#     return nutrition_dict

# getFruitInfo('apple')

# def getFruitInfo():
#     url = 'https://www.fruityvice.com/api/fruit/'
#     lst_fruits = ['apple', 'apricot', 'banana', 'blueberry']
#     fruit_dict = {}
#     for fruit in lst_fruits:
#         request = requests.get(url + fruit, verify = False)
#         data = request.json()
#         nutrition_dict = {}
#         for nut_val in data:
#             if nut_val == 'nutritions':
#                 nutrition_dict[nut_val] = data[nut_val]
#         fruit_dict[fruit] = nutrition_dict
#     return fruit_dict

# print(getFruitInfo())

def getFruitInfo():
    url = 'https://www.fruityvice.com/api/fruit/'
    lst_fruits = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'grapes', 'guava', 'lemon', 'lime', 'mango', 'melon', 'orange', 'papaya', 'pear', 'persimmon']
    fruit_dict = {}
    for fruit in lst_fruits:
        request = requests.get(url + fruit, verify = False)
        data = request.json()
        nutrition_dict = {}
        for nut_val in data:
            if nut_val == 'nutritions':
                for nut in data[nut_val]:
                    nutrition_dict[nut] = data[nut_val][nut]
        fruit_dict[fruit] = nutrition_dict
    return fruit_dict

print(getFruitInfo())


