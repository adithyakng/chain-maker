import nvdlib
import json

API_KEY = "99d5cd7a-70df-4fa5-bd38-d43b53da848c"
RATE_LIMIT = 0.7

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

data = read_json('./attackDB.json')

final_data = []

def addToDatabase(CVE_ID):
    # r = nvdlib.searchCVE(cveId='CVE-2021-26855', key=API_KEY, delay=RATE_LIMIT)[0]
    # print(r.tags)
    test_object = {"key1": "value1", "key2": "value2"}
    
    return test_object

for i in range(len(data)):
    # Get the required keys 

    # Get the values of those keys by querying the NVD database
    nvd = addToDatabase(data[i]['cve'])

    
    # Combine the two dictionaries
    c = {**nvd, **data[i]}
    print(c)
    # Add the values to the dictionary
    #data[i]['cwe'] = 'new_value'
    final_data.append(c)


print(data)
# Create a new JSON file with the updated data
with open('./attackDB-final.json', 'w') as file:
    json.dump(data, file, indent=4)

