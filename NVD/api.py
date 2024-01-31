import nvdlib
import json

API_KEY = "99d5cd7a-70df-4fa5-bd38-d43b53da848c"
RATE_LIMIT = 0.7
INPUT_FILE = './attackDB.json'
OUTPUT_FILE = './attackDB-final.json'


def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def addToDatabase(CVE_ID):
    try:
        r = nvdlib.searchCVE(cveId=CVE_ID, key=API_KEY, delay=RATE_LIMIT)[0]
        return r
    except Exception as e:
        print(f"Error querying NVD database: {e}")
        return None


def main():
    data = read_json(INPUT_FILE)
    final_data = [
        {**item, **{
            "sourceIdentifier": nvd.sourceIdentifier,
            "cwe": nvd.cwe[0].value,
            "baseScore": nvd.metrics.cvssMetricV30[0].cvssData.baseScore,
            "baseSeverity": nvd.metrics.cvssMetricV30[0].cvssData.baseSeverity,
            "scope": nvd.metrics.cvssMetricV30[0].cvssData.scope,
            "vectorString": nvd.metrics.cvssMetricV30[0].cvssData.vectorString
        }}
        for item in data if (nvd := addToDatabase(item['cve'])) is not None
    ]

    with open(OUTPUT_FILE, 'w') as file:
        json.dump(final_data, file, indent=4)


if __name__ == "__main__":
    main()