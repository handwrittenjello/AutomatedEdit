import requests
website_url = requests.get('https://en.wikipedia.org/wiki/UFC_240')
html = website_url.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())

#allTable = str(soup.findAll('table'))
#print(soup.prettify(allTable))

resultsTable = soup.find('table', class_ = 'toccolours')
#print(soup.prettify(resultsTable))

weightClass = []
fighterWinner = []
defeat = []
fighterLoser = []
victoryType = []
victoryRound = []
victoryTime = []
notes =[]

for row in resultsTable.findAll('tr'):
    cells=row.findAll('td')
    if len(cells) == 8:
        weightClass.append(cells[0].find(text=True))
        fighterWinner.append(cells[1].find(text=True))
        defeat.append(cells[2].find(text=True))
        fighterLoser.append(cells[3].find(text=True))
        victoryType.append(cells[4].find(text=True))
        victoryRound.append(cells[5].find(text=True))
        victoryTime.append(cells[6].find(text=True))
        notes.append(cells[7].find(text=True))


import pandas as pd
df=pd.DataFrame(weightClass, columns=['Weight Class'])
df['Winner'] = fighterWinner
df['def'] = defeat
df['Loser'] = fighterLoser
df['Won By'] = victoryType
df['Round'] = victoryRound
df['Time'] = victoryTime
df['Notes'] = notes
df = df.replace('\n','', regex=True)
print (df)