import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import re
from tabulate import tabulate

website_url = requests.get('https://www.ibjjfdb.com/ChampionshipResults/1303/PublicRegistrations?lang=en-US')
html = website_url.content

soup = BeautifulSoup(html, 'lxml')


searchtext = re.compile(r'BLUE / Master 1 / Male / Heavy',re.IGNORECASE)
foundtext = soup.find('h4',text=searchtext)
table = foundtext.findNext('table')
   
 
df = pd.read_html(str(table))[0]

print(df)
