# Installation

1. Install docker and docker compose
2. on the root directory of this folder, run the following command:

```
docker compose up
```

# Example Usage:

### Test API
```bash
# Set the tests/attackDB.json
# Set the tests/initState.json
docker-compose up
curl -X POST -H "Content-Type: application/json" -d '{"initState": {"paramA1":"xA", "paramA2":"yA"}}' http://127.0.0.1:5000/api/chains
# Chains identified within attackDB.json will be stored in the 'chains' directory.
```

### Flowchart

![image](./backend/assets/Flowchart.png)
