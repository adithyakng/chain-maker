from flask import Flask, request, jsonify
from loadJSON import load_attacks
from makeChain import makeChain, AttackDB, State
import os
import json

app = Flask(__name__)

def log_and_save_chains(chains):
    # Create a directory for the chains
    os.makedirs('chains', exist_ok=True)

    for i, chain in enumerate(chains):
        chain_dicts = [attack.to_dict() for attack in chain]
        # Create a filename for the chain
        filename = f'chains/chain_{i+1}.json'
        # Write the chain to the file
        with open(filename, 'w') as f:
            json.dump(chain_dicts, f, indent=4)


@app.route('/api/chains', methods=['POST'])
def get_chains():
    # Get the initState from the request body
    initState_data = request.json.get('initState')

    # Create a State object from the initState data
    initState = State(initState_data)

    # Load the attacks from the JSON file
    attackDB = AttackDB(load_attacks('./tests/attackDB.json'))

    # Run the makeChain function with the loaded state and AttackDB
    chains = makeChain(initState, attackDB)

    # Convert the chains to a list of dictionaries
    chains_dicts = [[attack.to_dict() for attack in chain] for chain in chains]

    log_and_save_chains(chains)


if __name__ == '__main__':
    app.run(debug=True)
