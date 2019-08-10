import subprocess
import webbrowser
from flask import Flask, request, render_template
import requests
import numpy as np
import os
from tmdbv3api import TMDb
from tmdbv3api import Movie
import urllib
from bs4 import BeautifulSoup
import pandas as pd

print('Which fight card will you be splitting today?')
firstCard = input()
website_url = requests.get('https://en.wikipedia.org/wiki/UFC_' + firstCard)
html = website_url.content

##Creating datafrom from pulled results table from Wikiscraper
soup = BeautifulSoup(html, 'lxml')


infoTable = soup.find('table', class_ = 'infobox')
#print(infoTable)

poster = []
promotion = []
date = []
venue = []
city = []
attendance = []
totalGate = []
previousCard = []
currentCard = []
futureCard = []
tablePreviousCard = []
tableCurrentCard = []
tableFutureCard = []

td = infoTable.findAll('td')
poster.append(td[0].find(text=True))
promotion.append(td[1].find(text=True))
date.append(td[2].find(text=True))
venue.append(td[3].find(text=True))
city.append(td[4].find(text=True))
attendance.append(td[5].find(text=True))
totalGate.append(td[6].find(text=True))
previousCard.append(td[7].find(text=True))
currentCard.append(td[8].find(text=True))
futureCard.append(td[9].find(text=True))
tablePreviousCard.append(td[10].find(text=True))

df=pd.DataFrame(poster, columns=['Poster'])
df['Promotion'] = promotion
df['Date'] = date
df['Venue'] = venue
df['City'] = city
df['Attendance'] = attendance
df['Total Gate'] = totalGate
df['Previous Card'] = previousCard
df['Current Card'] = currentCard
df['Future Card'] = futureCard
df['Table Previous'] = tablePreviousCard
df = df.replace('\n','', regex=True)
df = df.replace("\xa0",' ', regex=True)
dateString = (df.Date.to_string(index=False))
print (df.Attendance.to_string(index=False))
print(dateString)


