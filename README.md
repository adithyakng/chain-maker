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
python3 app.py
curl -X POST -H "Content-Type: application/json" -d '{"initState": {"paramA1":"xA", "paramA2":"yA"}}' http://127.0.0.1:5000/api/chains
```

### Flowchart
![image](./Flowchart.png)
