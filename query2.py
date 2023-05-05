import sqlite3
from pymongo import MongoClient
import sys

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# QUERY 2: Write a query that returns all the Pokemon with an attack greater than 150
attack_150_plus = pokemonColl.find({ "attack": { "$gt": 150 } })
for group in attack_150_plus:
    print(group)