entries = []
with open("ELECTION_ID", "r") as f:
    items = f.read().split('\n')
    for item in items:
        entries.append(item.split())

import requests
url = 'http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/'

for entry in entries:
    if len(entry) < 2:
        continue
        
    html_doc = requests.get(url % (entry[1]))
    with open("president_general_" + entry[0] + ".csv", "w") as f:
        f.write(html_doc.text)
    