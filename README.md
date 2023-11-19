# Example Usage:

``` node 
npm install
node main.js [PATH/TO/INITIAL_STATE.json]
```

* The MongoDB server will store a list attacks (test/attackDB.json)
* The server will query the database and create a chain of attacks in the form of a JSON object
* This JSON data will be given to visualize.js, so we can visualize the chain 