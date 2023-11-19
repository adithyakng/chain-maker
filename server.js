import express from 'express';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

import {AttackDB, makeChain, BFS} from "./makeChain.js";
import { loadAttacks, loadState } from "./loadJSON.js";
import { getAttacks } from "./mongoDB.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the 'public' directory
app.use(express.static(join(__dirname, 'public')));

// Define an endpoint to send the index.html page
app.get('/visualize', (req, res) => {
  res.sendFile(join(__dirname, 'public', 'visualize.html'));
});

// Define an endpoint to send the visualize.js script
app.get('/visualize.js', (req, res) => {
  res.sendFile(join(__dirname, 'public', 'visualize.js'));
});

// Define an endpoint to send the Chain to the client
app.get('/makeChain', async (req, res) => {
  try {
    // Get init state
    const initState = loadState('.\\tests\\initState1.json');

    // Queries the database to get a list of attacks as JSON data
    const documents = await getAttacks();

    // Creates an array of Attack objects from the JSON data  
    const attacks = loadAttacks(documents);

    // Creates the attack DB
    let attackDB = new AttackDB(attacks);

    // Creates a chain starting from the given initial state
    let chain = makeChain(initState, attackDB);

    console.log(chain);

    //BFS(chain);
    res.json(chain);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
