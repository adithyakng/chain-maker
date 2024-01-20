import os
import json
import logging
from loadJSON import load_attacks, load_state
from makeChain import makeChain, AttackDB


# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the attacks and state from a JSON file
logging.info("Loading attacks from JSON file...")
attackDB = AttackDB(load_attacks('./tests/attackDB.json'))

# Load the initial state from a JSON file
logging.info("Loading initial state from JSON file...")
state = load_state('./tests/initState.json')

# Run the makeChain function with the loaded state and AttackDB
logging.info("Running makeChain function...")
chains = makeChain(state, attackDB)

