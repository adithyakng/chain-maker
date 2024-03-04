import os
import json
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from helpers.loadJSON import load_attacks
from helpers.makeChain import makeChain, AttackDB, State

def save_chains(chains, case_num):
    # Create a directory for the chains
    os.makedirs(f"results/test-{case_num}", exist_ok=True)

    for i, chain in enumerate(chains):
        chain_dicts = [attack.to_dict() for attack in chain]
        # Create a filename for the chain
        filename = f"results/test-{case_num}/chain_{i+1}.json"
        # Write the chain to the file
        with open(filename, "w") as f:
            json.dump(chain_dicts, f, indent=4)

def get_chains():
    test_case = sys.argv[1]

    # Read the initState from the file
    with open(f"test-{test_case}/initState.json", "r") as f:
        initState_data = json.load(f)

    # Create a State object from the initState data 
    initState = State(initState_data)

    # Load the attacks from the JSON file (get this data from the MongoDB in the future)
    attackDB = AttackDB(load_attacks(f"test-{test_case}/attackDB.json"))

    # Run the makeChain function with the loaded state and AttackDB
    chains = makeChain(initState, attackDB)

    # Convert the chains to a list of dictionaries
    chains_dicts = [[attack.to_dict() for attack in chain] for chain in chains]

    save_chains(chains, test_case)

get_chains()