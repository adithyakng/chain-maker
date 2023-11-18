import {AttackDB, makeChain, BFS} from "./makeChain.js";
import { loadAttacks, loadState } from "./loadJSON.js";
import { getAttacks } from "./mongoDB.js";

// Creates a State object by reading from a json file  
const initState = loadState(process.argv[2])

// Queries the database to get a list of attacks as JSON data
const documents = await getAttacks();

// Creates an array of Attack objects from the JSON data  
const attacks = loadAttacks(documents);

// Creates the attack DB
let attackDB = new AttackDB(attacks);

// Creates a chain starting from the given initial state
let chain = makeChain(initState, attackDB);

// Print the result
//console.log(JSON.stringify(chain, null, 2));

// Perform BFS on the generated JSON tree (chain)
// BFS(chain);

export {}