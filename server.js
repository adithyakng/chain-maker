import express from 'express';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the 'public' directory
app.use(express.static(join(__dirname, 'public')));

// Define an endpoint to send the index.html page
app.get('/', (req, res) => {
  res.sendFile(join(__dirname, 'public', 'index.html'));
});

// Define an endpoint to send the visualize.js script
app.get('/visualize.js', (req, res) => {
  res.sendFile(join(__dirname, 'public', 'visualize.js'));
});

// This is the output of makeChain function 
const jsonArray = [
    [
      {
        "name": "attackA",
        "initState": {
          "params": {
            "paramA1": "xA",
            "paramA2": "yA"
          }
        },
        "endState": {
          "params": {
            "paramA1": "xB",
            "paramA2": "yB"
          }
        }
      },
      {
        "name": "attackB",
        "initState": {
          "params": {
            "paramA1": "xB",
            "paramA2": "yB"
          }
        },
        "endState": {
          "params": {
            "paramB1": "z",
            "paramB2": "z2",
            "paramB3": "z3",
            "paramB4": "z4"
          }
        }
      },
      {
        "name": "attackC",
        "initState": {
          "params": {
            "paramB1": "z",
            "paramB2": "z2",
            "paramB3": "z3",
            "paramB4": "z4"
          }
        },
        "endState": {
          "params": {
            "paramB1": "z",
            "paramB2": "z2",
            "paramB4": "z4"
          }
        }
      },
      {
        "name": "End"
      }
    ],
    [
      {
        "name": "attackA",
        "initState": {
          "params": {
            "paramA1": "xA",
            "paramA2": "yA"
          }
        },
        "endState": {
          "params": {
            "paramA1": "xB",
            "paramA2": "yB"
          }
        }
      },
      {
        "name": "attackB",
        "initState": {
          "params": {
            "paramA1": "xB",
            "paramA2": "yB"
          }
        },
        "endState": {
          "params": {
            "paramB1": "z",
            "paramB2": "z2",
            "paramB3": "z3",
            "paramB4": "z4"
          }
        }
      },
      {
        "name": "attackD",
        "initState": {
          "params": {
            "paramB1": "z",
            "paramB2": "z2",
            "paramB3": "z3",
            "paramB4": "z4"
          }
        },
        "endState": {
          "params": {
            "paramC1": "z2",
            "paramC2": "z2"
          }
        }
      },
      {
        "name": "End"
      }
    ],
    [
      {
        "name": "attackA",
        "initState": {
          "params": {
            "paramA1": "xA",
            "paramA2": "yA"
          }
        },
        "endState": {
          "params": {
            "paramA1": "xB",
            "paramA2": "yB"
          }
        }
      },
      {
        "name": "attackE",
        "initState": {
          "params": {
            "paramA1": "xB",
            "paramA2": "yB"
          }
        },
        "endState": {
          "params": {
            "parmD1": "z",
            "parmD2": "z2"
          }
        }
      },
      {
        "name": "End"
      }
    ]
];
  

// Define an endpoint to send the jsonArray to the client
app.get('/getJsonArray', (req, res) => {
  res.json(jsonArray);
  //To Do 
  // Get init State from the user
  // Call makeChain
  // Send output of makeChain as JSON object
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
