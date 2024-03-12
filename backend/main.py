import os
import json
import logging
from helpers.loadJSON import load_attacks, load_state
from helpers.makeChain import makeChain, AttackDB


# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the attacks and state from a JSON file
logging.info("Loading attacks from JSON file...")
attackDB = AttackDB(load_attacks("./algorithm-tests/test-1/attackDB.json"))

# Load the initial state from a JSON file
logging.info("Loading initial state from JSON file...")
state = load_state("./algorithm-tests/test-1/initState.json")

# Run the makeChain function with the loaded state and AttackDB
logging.info("Running makeChain function...")
chains = makeChain(state, attackDB)
chainIndex = 0
for idx, attack_list in enumerate(chains):
    print(f"Attack List {idx}:")
    for attack in attack_list:
        print(attack)

