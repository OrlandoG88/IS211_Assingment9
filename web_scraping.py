import requests
from bs4 import BeautifulSoup



page = requests.get('https://en.wikipedia.org/wiki/List_of_World_Series_of_Poker_Main_Event_champions')

soup = BeautifulSoup(page.text, 'html.parser')
results_table = soup.find_all('table', class_= 'wikitable sortable')
rows = results_table[0].find_all('tr')
headers = rows[0].find_all('th')

print(f'{headers[1].text.strip():<8} - {headers[2].text.strip():<8} - {headers[3].text.strip():<8}')


for row in rows:
    cells = row.find_all('td')
    if not cells:
        continue

print(f'{cells[1].text.strip():<8} - {cells[2].text.strip():<8} - {cells[3].text.strip():<8}')




