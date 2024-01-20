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
    def __init__(self, name, initState, endState, info_required, info_gained):
        self.name = name
        self.initState = initState
        self.endState = endState
        self.info_required = info_required
        self.info_gained = info_gained
    
    def __str__(self):
        return f"Attack: {self.name}, Init State: {self.initState}, End State: {self.endState}"

    def to_dict(self):
        return {
            'name': self.name,
            'initState': self.initState.to_dict(),
            'endState': self.endState.to_dict(),
        }


class AttackDB:
    def __init__(self, attacks):
        self.attacks = attacks

    def __str__(self):
        attack_names = [attack.name for attack in self.attacks]
        return "AttackDB: " + ", ".join(attack_names)



def makeChain(initState, attackDB, knowledge=set()):
    logging.info('Starting makeChain with initState: %s', initState.params)
    chains = []

    logging.info('Current knowledge: %s', knowledge)

    # Find attacks with matching initState and knowledge
    matchingAttacks = [attack for attack in attackDB.attacks if attack.initState.equals(initState)]
                    #    and knowledge.issuperset(attack.info_required)]

    logging.info('Found %d matching attacks', len(matchingAttacks))
    for attack in matchingAttacks:
        logging.info('Matching attack: %s', attack.name)

    # For each matching attack, recursively construct chains
    for attack in matchingAttacks:
        logging.info('Processing attack: %s', attack.name)
        logging.info('Info gained: %s', attack.info_gained)
        

        if knowledge.issuperset(attack.info_required):
            logging.info('Attack is possible with current knowledge')
            chain = [attack]
        else:
            continue

        # Set the initState for the next attack to be the endState of the current attack
        initState = attack.endState

        knowledge.update(attack.info_gained)

        # Recursively find chains starting from the endState
        subChains = makeChain(initState, attackDB, knowledge)
        for subChain in subChains:
            chains.append(chain + subChain)

    if len(chains) == 0:
        # If no chains are found, return a chain with the current initState
        logging.info('No chains found, returning end state')
        return [[]]

    logging.info('Returning %d chains', len(chains))
    return chains