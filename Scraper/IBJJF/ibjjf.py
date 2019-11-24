#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import re
from tabulate import tabulate
import os
from pushbullet import Pushbullet

cwd = os.getcwd()

pb = Pushbullet('o.1KwoYNtz1JnCkmfS4Xn6xuKxudks5SdA')


website_url = requests.get(
    'https://www.ibjjfdb.com/ChampionshipResults/1303/PublicRegistrations?lang=en-US')
html = website_url.content

soup = BeautifulSoup(html, 'lxml')


searchtext = re.compile(r'BLUE / Master 1 / Male / Heavy', re.IGNORECASE)
foundtext = soup.find('h4', text=searchtext)
table = foundtext.findNext('table')

pd.set_option('max_colwidth', -1)

competitorList = []
academyList = []

for row in table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 2:
        academyList.append(cells[0].find(text=True))
        competitorList.append(cells[1].find(text=True))


df = pd.DataFrame(academyList, columns=['Academy'])
df['Competitor'] = competitorList
df = df.replace('\n                               ', '', regex=True)
df = df.replace('\r', '', regex=True)


# Pretty Prints Bracket in Ascii
print(tabulate(df, headers='keys', tablefmt='psql'))

print('\n'*4)


# Opens Previous Bracket and converts original Markdown to List
l = open(cwd + "/OGBracket.md", "r")
originalBracketList = l.readlines()
l.close()


f = open(cwd + "/newBracket.md", "w")
f.write(str(df))

f = open(cwd + "/newBracket.md", "r")
newBracketList = f.readlines()
f.close()


def Diff(newBracketList, originalBracketList):
    return (list(set(newBracketList) - set(originalBracketList)))


diffValue = Diff(newBracketList, originalBracketList)

if diffValue:
    f = open(cwd + "/OGBracket.md", "w")
    f.write(str(df))
    diffValue = str(diffValue)
    diffValue = diffValue[8:]
    diffValue = diffValue[:-8]
    print('The following competitor has been added' +
          diffValue)
    push = pb.push_note("Competitor has been added", "This is the body")
    
else:
    print('No Competitors have been added')
