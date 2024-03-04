from flask import Flask, request, jsonify
from helpers.loadJSON import load_attacks
from helpers.makeChain import makeChain, AttackDB, State
import os
import json

app = Flask(__name__)


# HealthCheck
@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return "Server is Alive!"


@app.route("/api/chains", methods=["POST"])
def get_chains():
    # Get the initState from the request body
    initState_data = request.json.get("initState")

    # Create a State object from the initState data 
    initState = State(initState_data)

    # Load the attacks from the JSON file (get this data from the MongoDB in the future)
    attackDB = AttackDB(load_attacks("./algorithm-tests/test-1/attackDB.json"))

    # Run the makeChain function with the loaded state and AttackDB
    chains = makeChain(initState, attackDB)

    # Convert the chains to a list of dictionaries
    chains_dicts = [[attack.to_dict() for attack in chain] for chain in chains]

    return jsonify(chains_dicts)


if __name__ == "__main__":

    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
