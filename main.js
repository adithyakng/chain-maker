import {State, Attack, AttackDB, makeChain, BFS} from "./makeChain.js";

// Example usage:

// Define the attacks (This is basically all the data from our Spreadsheet)
let attack1 = new Attack("attackA", new State({"paramA1":"xA", "paramA2":"yA"}), new State({"paramA1":"xB", "paramA2":"yB"}));
let attack2 = new Attack("attackB", new State({"paramA1":"xB", "paramA2":"yB"}), new State({"paramB1":"z", "paramB2":"z2", "paramB3": "z3"}));
let attack3 = new Attack("attackC", new State({"paramB1":"z", "paramB2":"z2", "paramB3": "z3"}), new State({"paramC1":"z2", "paramC2":"z2"}));
let attack4 = new Attack("attackD", new State({"paramA1":"xB", "paramA2":"yB"}), new State({"parmD1":"z", "parmD2":"z2"}));

// Create the attack DB
let attackDB = new AttackDB([attack1, attack2, attack3, attack4]);

// Enter the state you want the chain to start from
let chain = makeChain(new State({"paramA1":"xA", "paramA2":"yA"}), attackDB);

// Print the result
console.log(JSON.stringify(chain, null, 2));

// Perform BFS on the generated JSON tree (chain)
BFS(chain);