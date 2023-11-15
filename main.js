import {State, Attack, AttackDB, makeChain, BFS} from "./makeChain.js";
import { loadAttacks, loadState } from "./loadJSON.js";

// Creates a State object by reading from a json file  
const initState = loadState(process.argv[2])

// Creates a Attack DB object by reading from a json file
const attacks = loadAttacks(process.argv[3])

// Create the attack DB
let attackDB = new AttackDB(attacks);

// Enter the state you want the chain to start from
let chain = makeChain(initState, attackDB);

// Print the result
console.log(JSON.stringify(chain, null, 2));

// Perform BFS on the generated JSON tree (chain)
BFS(chain);
