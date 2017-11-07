import requests

url='http://historical.elections.virginia.gov/elections/search/' \
    + 'year_from:1924/year_to:2016/office_id:1/stage:General'

html_doc = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc.text, 'html.parser')
table = soup.find('table', {'id':'search_results_table'})

output = open("election_year_id.txt","w")

for tr in table.find_all('tr', 'election_item'):
    
    id = tr.get('id')
    year_td = tr.find('td', {'class':'year'})
    year = year_td.text
    output.write("%s %s\n" % (year, id[-5:]))
    
output.close()