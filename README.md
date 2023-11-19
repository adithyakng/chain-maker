# Installation

On MAC,

Install [MongoDB Compass](https://www.mongodb.com/try/download/compass) on your machine. Then, follow these instructions to install and start the MongoDB service.

```bash
brew tap mongodb/brew
brew update
brew install mongodb-community@7.0
brew services start mongodb-community@7.0
```

# Example Usage:

```bash
 npm install
 node server.js
 # Make sure the MongoDB database is popullated 
 # In server.js, in the loadState function, you change the path of the initState.json 
 # Go to localhost:3000
```

### Flowchart
![image](./Flowchart.png)
