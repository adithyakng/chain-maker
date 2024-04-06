import os
import json
import logging
from helpers.loadJSON import load_attacks, load_state, load_end_state
from helpers.makeChain import makeChain, AttackDB, makeChainWithEndState, Attack, State
import sys

#Give argv [1] as 1, if we want chains with initState and EndAttack as input
withEndState = 0
if(len(sys.argv) > 1):
    withEndState = sys.argv[1]


# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the attacks and state from a JSON file
logging.info("Loading attacks from JSON file...")
attackDB = AttackDB(load_attacks("./algorithm-tests/test-1/attackDB.json"))

# Load the initial state from a JSON file
logging.info("Loading initial state from JSON file...")
state = load_state("./algorithm-tests/test-1/initState.json")
if(withEndState == "1"):
    # Load the end state from a JSON file
    logging.info("Loading end state from JSON file...")
    endState = load_end_state("./algorithm-tests/test-1/endState.json")

    # Create an attack object from the endState data
    endAttack = Attack(
            endState["name"],
            State(endState["initState"]),
            State(endState["endState"]),
            set(endState["info_required"]),
            set(endState["info_gained"]),
            "endAttackID"
        )


logging.info("Running function...")
if(withEndState == "1"):

    # Run the makeChainWithEndsState function with the loaded state and AttackDB
    chains = makeChainWithEndState(state, endAttack, attackDB)
else:
    # Run the makeChain function with the loaded state and AttackDB
    chains = makeChain(state, attackDB)

for idx, attack_list in enumerate(chains):
    print(f"Attack List {idx}:")
    for attack in attack_list:
        print(attack)

