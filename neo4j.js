const neo4j = require('neo4j-driver');

const uri = 'bolt://localhost:7687';
const user = 'neo4j';
const password = 'neo4j';

const query = `CREATE(:State{
  protocol: $protocol,
  Which_standard_does_this_vulnerability_apply_to:$standard,
  Device:$device',
  Attack_Type:$attack_type,
  Approach:$approach,
  CWE_Class:$cwe,
  Name_of_Paper:$paper_name,
  Conference:$conference,
  Open_Source_Repository_Link:$repo,
  CVE_Number:$cve,
  Adversarial_Knowledge:$knowledge,
  System_State:$state,
  Which_devices_did_the_authors_confirm_the_vulnerability_on: $devices
  })`

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password));

async function run() {
  const session = driver.session();

  try {
    const result = await session.run(query, json_data);
    console.log(result.summary);
  } finally {
    await session.close();
  }
}

run()
  .then(() => {
    console.log('Query executed successfully.');
  })
  .catch((error) => {
    console.error('Error executing query:', error);
  })
  .finally(() => {
    driver.close();
  });
