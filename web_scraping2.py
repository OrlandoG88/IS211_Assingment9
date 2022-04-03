import requests
from bs4 import BeautifulSoup

# requesting page

page = requests.get('https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions')
#parsing HTML into soup tree
soup = BeautifulSoup(page.text, 'html.parser')
#extracting table
results_table = soup.find_all('table', class_= 'wikitable sortable')
#extraxting row from table
rows = results_table[0].find_all('tr')
#extracting headers from table
headers = rows[0].find_all('th')

print(f'{headers[0].text.strip():<8} - {headers[1].text.strip():<8} - {headers[2].text.strip():<8}')

#finding data cells to append into my new table
for row in rows:
    cells = row.find_all('td')
    if not cells:
        continue

    print(f'{cells[0].text.strip():<8} - {cells[1].text.strip():<8} - {cells[2].text.strip():<8}')