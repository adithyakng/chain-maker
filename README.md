# Installation

1. Install docker and docker compose
2. on the root directory of this folder, run the following command:

```
docker compose up
```

# Example Usage:

### Test API
```bash
docker-compose up
curl -X POST -H "Content-Type: application/json" -d '{"initState": {"paramA1":"xA", "paramA2":"yA"}}' http://127.0.0.1:5000/api/chains
```

### Test Algorithm Locally
```bash
cd backend/algorithm-tests/
# To run test case 1
python3 test.py 1
```

### Flowchart

![image](./backend/assets/Flowchart.png)
