import sqlite3
import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# QUERY 1: Write a query that returns all the Pokemon named "Pikachu"
pikachu = pokemonColl.find({'name': "Pikachu"})
for group in pikachu:
   print(group)