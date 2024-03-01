import json
import logging
from helpers.makeChain import State, Attack, AttackDB

logging.basicConfig(level=logging.INFO)


# This function takes a list of dictionaries, where each dictionary represents an attack.
# It creates an Attack object for each dictionary and returns a list of these Attack objects.
def create_attack(data):
    return [
        Attack(
            attack["name"],
            State(attack["initState"]),
            State(attack["endState"]),
            set(attack["info_required"]),
            set(attack["info_gained"]),
        )
        for attack in data
    ]


# This function takes a filename as input, opens the file, and loads the JSON data from the file.
# It then passes this data to the create_attack function to create a list of Attack objects, and returns this list.
def load_attacks(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return create_attack(data)


# This function takes a filename as input, opens the file, and loads the JSON data from the file.
# It then creates a State object from this data and returns it.
def load_state(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return State(data)
