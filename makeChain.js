// Define a State class representing the state of an attack
class State {
    constructor(params) {
        this.params = params;
    }

    // Custom equality check for comparing two State objects
    equals(other) {
        return JSON.stringify(this.params) === JSON.stringify(other.params);
    }
}

// Define an Attack class representing an attack with initial and end states
class Attack {
    constructor(name, initState, endState) {
        this.name = name;
        this.initState = initState;
        this.endState = endState;
    }
}

// Define an AttackDB class representing a collection of attacks
class AttackDB {
    constructor(attacks) {
        this.attacks = attacks;
    }
}

// Function to construct a chain by looking up all attacks that start from a given state
function makeChain(initState, attackDB) {
    let chains = [];

    // Find attacks with matching initState
    let matchingAttacks = attackDB.attacks.filter(attack => attack.initState.equals(initState));

    // For each matching attack, recursively construct chains
    matchingAttacks.forEach(attack => {
        let chain = [attack];
        let endState = attack.endState;

        // Recursively find chains starting from the endState
        let subChains = makeChain(endState, attackDB);
        subChains.forEach(subChain => {
            chains.push(chain.concat(subChain));
        });
    });

    if (chains.length === 0) {
        // If no chains are found, return a chain with the current initState
        return [[{ name: "End"}]];
    }

    return chains;
}

// Perform BFS on the JSON tree
function BFS(tree) {
    // Initialize the queue with the root of the tree
    let queue = [tree];  

    while (queue.length > 0) {
        let currentNode = queue.shift();  // Dequeue the front node

        // Process the current node
        if (currentNode instanceof Object && currentNode.hasOwnProperty("name")) {
            console.log(currentNode.name);
        }

        // Enqueue child nodes (chains)
        if (currentNode instanceof Array) {
            for (let i = 0; i < currentNode.length; i++) {
                queue.push(currentNode[i]);
            }
        }
    }
}

function hello (){
    return 0;
}

export { State, Attack, AttackDB, makeChain, BFS , hello};
