import { MongoClient }  from 'mongodb';

// Connection URI
const uri = 'mongodb://127.0.0.1:27017';

// Database Name and Collection Name
const dbName = 'Attacks';
const collectionName = 'Attacks';

// Create a new MongoClient
const client = new MongoClient(uri);

// Function to connect to MongoDB
async function connectToMongoDB() {
  try {
    // Connect to the MongoDB server
    await client.connect();
    console.log('Connected to the MongoDB server');
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
  }
}

// Function to get all documents from the collection
async function getAllDocuments() {
  try {
    // Access a specific database
    const database = client.db(dbName);

    // Access a specific collection within the database
    const collection = database.collection(collectionName);

    // Find all documents in the collection
    const documents = await collection.find({}).toArray();

    console.log('Documents in the collection:');
    console.log(documents);
  } catch (error) {
    console.error('Error retrieving documents:', error);
  }
}

// Function to insert JSON data into the collection
async function insertData(data) {
  try {
    // Access a specific database
    const database = client.db(dbName);

    // Access a specific collection within the database
    const collection = database.collection(collectionName);

    // Insert JSON data into the collection
    await collection.insertOne(data);

    console.log('Data inserted successfully');
  } catch (error) {
    console.error('Error inserting data:', error);
  }
}

// Function to close the MongoDB connection
async function closeConnection() {
  try {
    // Close the connection
    await client.close();
    console.log('Connection closed');
  } catch (error) {
    console.error('Error closing connection:', error);
  }
}


const test_attack =     {
  "name": "attackE",
  "initState": {
    "paramA1": "x2",
    "paramA2": "yy"
  },
  "endState": {
    "paramB1": "zz",
    "paramB3": "z3",
    "paramB4": "z4"
  }
}

// Example usage
async function main() {
   // Connect to MongoDB
  await connectToMongoDB();

  // Insert JSON data into the collection
  await insertData(test_attack);

  // Get all documents from the collection
  await getAllDocuments();

  await closeConnection();
}

main().catch(console.error);
