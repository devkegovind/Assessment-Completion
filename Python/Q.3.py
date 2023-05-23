"""Question 3: -
Write a program, which would download the data from the provided link, and then read the data and convert 
that into properly structured data and return it in Excel format.
Note - Write comments wherever necessary explaining the code written.
Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
Data Attributes - id: Identification Number - int num: Number of the
● Pokémon in the official Pokédex - int name: Pokémon name -
● string img: URL to an image of this Pokémon - string type:
● Pokémon type -string height: Pokémon height - float
● weight: Pokémon weight - float candy: type of candy used to evolve Pokémon or
given
● when transferred - string candy_count: the amount of candies required to evolve
- int
● egg: Number of kilometers to travel to hatch the egg - float spawn_chance:
● Percentage of spawn chance (NEW) - float avg_spawns: Number of this
pokemon on 10.000 spawns (NEW) - int
● spawn_time: Spawns most active at the time on this field. Spawn times are the same for all
time zones and are expressed in local time. (NEW) - “minutes: seconds” multipliers:
Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int
weakness: Types of
● Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of
successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous
evolutions of Pokémon - - list of dict
"""

import requests
import pandas as pd

# Download the data from the URL
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Extract the required information from the data
pokemons = data["pokemon"]
pokemon_list = []

for pokemon in pokemons:
    pokemon_data = {
        "Name": pokemon["name"],
        "Image": pokemon["img"],
        "Type": ", ".join(pokemon["type"]),
        "Height": pokemon.get("height", ""),
        "Weight": pokemon.get("weight", ""),
        "Candy": pokemon.get("candy", ""),
        "candy_count": pokemon.get("candy_count", ""),
        "egg": pokemon.get("egg", ""),
        "spawn_chance": pokemon.get("spawn_chance", ""),
        "avg_spawns": pokemon.get("avg_spawns", ""),
        "spawn_time": pokemon.get("spawn_time", ""),
        "multipliers": pokemon.get("multipliers", ""),
        "weaknesses": ", ".join(pokemon.get("weaknesses", [])),
        "Next_evolution": ", ".join(evol["name"] for evol in pokemon.get("next_evolution", [])),
        "Prev_evolution": ", ".join(evol["name"] for evol in pokemon.get("prev_evolution", []))
    
    }
    pokemon_list.append(pokemon_data)
    print(pokemon_list)