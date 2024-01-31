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
    r = nvdlib.searchCVE(cveId=CVE_ID, key=API_KEY, delay=RATE_LIMIT)[0]
    return r


for i in range(len(data)):
    # Get the values of those keys by querying the NVD database
    nvd = addToDatabase(data[i]['cve'])

    print(nvd.metrics)
    # Get the required keys from the NVD data (this can be changed to get more data if needed)
    nvdData = {
        "sourceIdentifier": nvd.sourceIdentifier,
        "cwe": nvd.cwe[0].value,
        "baseScore": nvd.metrics.cvssMetricV30[0].cvssData.baseScore,
        "baseSeverity": nvd.metrics.cvssMetricV30[0].cvssData.baseSeverity,
        "scope": nvd.metrics.cvssMetricV30[0].cvssData.scope,
        "vectorString": nvd.metrics.cvssMetricV30[0].cvssData.vectorString
    }

    # Combine the two dictionaries
    c = {**data[i], **nvdData}
    # Add the values to the dictionary
    final_data.append(c)


# Create a new JSON file with the updated data
with open('./attackDB-final.json', 'w') as file:
    json.dump(final_data, file, indent=4)
