import json

class State:
    def __init__(self, params):
        self.params = params

    def __eq__(self, other):
        return self.params == other.params

    def __str__(self, other):
        return self.name


class Attack:
    def __init__(self, name, initState, endState):
        self.name = name
        self.initState = initState
        self.endState = endState

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class AttackDB:
    def __init__(self, attacks):
        self.attacks = attacks


# Constructs a chain by looking up all the attacks that start from a given state 
def MakeChain(initState, attackDB):
    # This will store a list of all the attacks that begin from the initState
    attacks = []
    chain = []
    # Go through attacksDB to see if the initial states matches 
    for attack in attackDB.attacks:
        # Load the corresponding attacks in a list
        if attack.initState == initState:
            attacks.append(attack)

    if attacks:
        # It is important to note that a single initState can have more than one attacks which start from that state
        for attack in attacks:
            # We get the final state of the attack and recursivley construct a chain(tree) which starts from that state
            newState = attack.endState
            chain.extend((attack, [MakeChain(newState, attackDB)]))
        return chain
    else:
        # If no attacks are found then return empty list []
        return []
    


attack1 = Attack("attackA", initState = State({"paramA1":"xA", "paramA2":"yA"}), endState = State({"paramA1":"xB", "paramA2":"yB"})) 
attack2 = Attack("attackB", initState = State({"paramA1":"xB", "paramA2":"yB"}), endState = State({"paramB1":"z", "paramB2":"z2", "paramB3": "z3"})) 
attack3 = Attack("attackC", initState = State({"paramB1":"z", "paramB2":"z2", "paramB3": "z3"}), endState = State({"paramC1":"z2", "paramC2":"z2"})) 
attack4 = Attack("attackD", initState = State({"paramA1":"xB", "paramA2":"yB"}), endState = State({"parmD1":"z", "parmD2":"z2"})) 
# Create the attack DB (This is just a collection of all the attacks from our spreadsheet)
attackDB = AttackDB([attack1, attack2,attack3,attack4])
chain = MakeChain(State({"paramA1":"xA", "paramA2":"yA"}), attackDB)

chain = json.dumps(chain)
print(chain)