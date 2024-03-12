import logging

logging.basicConfig(level=logging.INFO)


class State:
    def __init__(self, params):
        self.params = params

    # Checks if the endState is a subset of the initState
    def equals(self, other):
        for key in self.params:
            if self.params[key] != other.params.get(key):
                return False
        return True
    
    def __str__(self):
        return "State: " + str(self.params)
    
    def to_dict(self):
        return self.params


class Attack:
    def __init__(self, name, initState, endState, info_required, info_gained, id):
        self.name = name
        self.initState = initState
        self.endState = endState
        self.info_required = info_required
        self.info_gained = info_gained
        self.id = id
    
    def __str__(self):
        return f"Attack: {self.name}, Init State: {self.initState}, End State: {self.endState}"

    def to_dict(self):
        return {
            'name': self.name,
            'initState': self.initState.to_dict(),
            'endState': self.endState.to_dict(),
            'id': self.id
        }


class AttackDB:
    def __init__(self, attacks):
        self.attacks = attacks

    def __str__(self):
        attack_names = [attack.name for attack in self.attacks]
        return "AttackDB: " + ", ".join(attack_names)


"""
Algorithm Steps:
1) The function starts by finding all attacks in the database that match the initial state.
2) For each matching attack, the function checks if the current knowledge is a superset
of the information required for the attack.
3) If it is, the function logs that the attack is possible and adds the attack to a chain of attacks.
4) The end state of the attack is set as the initial state for the next attack, before recursively 
calling the function again.
"""
def makeChain(initState, attackDB, knowledge=set(), attacksVisited={}):
    logging.info('Starting makeChain with initState: %s', initState.params)
    chains = []
    logging.info('Current knowledge: %s', knowledge)

    # Find attacks with matching initState and knowledge
    matchingAttacks = [attack for attack in attackDB.attacks if attack.initState.equals(initState) and attack.id not in attacksVisited]

    logging.info('Found %d matching attacks', len(matchingAttacks))
    for attack in matchingAttacks:
        logging.info('Matching attack: %s', attack.name)

    # For each matching attack, recursively construct chains
    for attack in matchingAttacks:
        logging.info('Processing attack: %s', attack.name)
        logging.info('Info gained: %s', attack.info_gained)
        
        # Iterate over each possible attack
        # Check if the current knowledge is a superset of the information required for the attack
        if knowledge.issuperset(attack.info_required):
            logging.info('Attack is possible with current knowledge')
            # Add the attack to the chain
            chain = [attack]

            # Mark the attack as visited
            attacksVisited[attack.id] = True
        else:
            # skip this attack and continue with the next one in the loop
            continue

        # Update the knowledge with the information gained from the current attack
        knowledge.update(attack.info_gained)

        # Set the initState for the next attack to be the endState of the current attack
        initState = attack.endState

        # Recursively find chains starting from the endState
        subChains = makeChain(initState, attackDB, knowledge, attacksVisited)
        for subChain in subChains:
            chains.append(chain + subChain)

        # Mark the attack as not visited
        attacksVisited[attack.id] = False

    if len(chains) == 0:
        # If no chains are found, return a chain with the current initState
        logging.info('No chains found, returning end state')
        return [[]]

    logging.info('Returning %d chains', len(chains))
    return chains