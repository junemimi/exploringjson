from pymongo import MongoClient
import sqlite3

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

conn = sqlite3.connect("pokemon.sqlite")

def insertInto(): 
    c = conn.cursor() 
    sql = """
            SELECT 
            pokemon.id,
            pokemon.name,
            pokemon.pokedex_number,
            GROUP_CONCAT(type.name, ', ') AS type_names,
            pokemon.hp,
            pokemon.attack,
            pokemon.defense,
            pokemon.speed,
            pokemon.sp_attack,
            pokemon.sp_defense,
            replace(GROUP_CONCAT(DISTINCT ability.name), ',', ', ')
            FROM pokemon
            JOIN pokemon_abilities ON pokemon.id = pokemon_abilities.pokemon_id
            JOIN ability ON pokemon_abilities.ability_id = ability.id
            JOIN pokemon_type ON pokemon.id = pokemon_type.pokemon_id
            JOIN type ON pokemon_type.type_id = type.id
            GROUP BY pokemon.id
            """
    
    c.execute(sql)
    pokemons = c.fetchall()

    c.close()
    conn.close()

    for group in pokemons:
        if group[3] == '':
            types = "[" + group[2] + "]"
        else:
            types = "[" + group[2] + ", " + group[3] + "]"

        pokemon = {
            "pokedex_number": int(group[0]),
            "name": group[1],
            "types": types,
            "hp": group[4],
            "attack": group[5],
            "defense": group[6],
            "speed": group[7],
            "sp_attack": group[8],
            "sp_defense": group[9],
            "abilities": group[10]
        }

        pokemonColl.insert_one(pokemon)