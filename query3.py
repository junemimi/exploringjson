import sqlite3
from pymongo import MongoClient
import sys

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# QUERY 3: Write a query that returns all the Pokemon with an ability of "Overgrow"
overgrow = pokemonColl.find({ "abilities": { "$regex": ".*Overgrow.*" } })
for group in overgrow:
    print(group)