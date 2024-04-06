from flask import Flask, request, jsonify
from helpers.loadJSON import load_attacks
from helpers.makeChain import makeChain, AttackDB, State, Attack, makeChainWithEndState
from helpers.mongoDB import getAttackDB
import os
import json

app = Flask(__name__)

#Read AttackDB from MongoDB
DB= getAttackDB()
if(not DB["success"]):
   print("MongoDB unable to connect")
   exit
attackDB = AttackDB(DB["attacks"])

# HealthCheck
@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return "Server is Alive!"


@app.route("/chains", methods=["POST"])
def get_chains():

    try:
        # Get the initState from the request body
        initState_data = request.json.get("initState")

        # Create a State object from the initState data 
        initState = State(initState_data)

        # Run the makeChain function with the loaded state and AttackDB
        chains = makeChain(initState, attackDB,set(),{})
       
        # Convert the chains to a list of dictionaries
        if len(chains) == 1 and len(chains[0]) == 0:
            chains_dicts = []
        else:
            chains_dicts = [
                {index: attack.to_dict() for index, attack in enumerate(chain)}
                for chain in chains
            ] 
        return {
            'status' : True,
            'chains' : chains_dicts
        }
    except Exception as error:
        return {
            'status' : False,
            'message' : str(error)
        }
        


@app.route("/chainsWithEndAttack", methods=["POST"])
def get_chains_with_end_attack():
        
    try:
        # Get the initState from the request body
        initState_data = request.json.get("initState")

        # Get the end attack from the request body
        endAttack_data = request.json.get("endAttack")

        # Create a State object from the initState data 
        initState = State(initState_data)

        # Create an attack object from the endAttack data
        endAttack = Attack(
                endAttack_data["name"],
                State(endAttack_data["initState"]),
                State(endAttack_data["endState"]),
                set(endAttack_data["info_required"]),
                set(endAttack_data["info_gained"]),
                "endAttackID"
            )

        # Run the makeChainWithEndState function with the loaded state and AttackDB and EndAttack
        chains = makeChainWithEndState(initState, endAttack, attackDB)
        if len(chains) == 1 and len(chains[0]) == 0:
            chains_dicts = []
        else:
            # Convert the chains to a list of dictionaries
            chains_dicts = [
                {index: attack.to_dict() for index, attack in enumerate(chain)}
                for chain in chains
            ]
        return {
                'status' : True,
                'chains' : chains_dicts
            }
    except Exception as error:
        return {
            'status' : False,
            'message' : str(error)
        }


if __name__ == "__main__":

    app.run(debug=True, port=5001)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
