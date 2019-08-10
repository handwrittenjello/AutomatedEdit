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

promotion = []
date = []
venue = []
city = []
attendance = []
totalGate = []
eventChronology = []

##Addes rows to the databale based on UFC Results
for row in infoTable.findAll('tr'):
    cells=row.findAll('td')
    if len(cells) == 8:
        promotion.append(cells[0].find(text=True))
        date.append(cells[1].find(text=True))
        venue.append(cells[2].find(text=True))
        city.append(cells[3].find(text=True))
        attendance.append(cells[4].find(text=True))
        totalGate.append(cells[5].find(text=True))
        eventChronology.append(cells[6].find(text=True))

df=pd.DataFrame(promotion, columns=['Promotion'])
df['Date'] = date
df['Venue'] = venue
df['City'] = city
df['Attendance'] = attendance
df['Total Gate'] = totalGate
df['Event Chronology'] = eventChronology
df = df.replace('\n','', regex=True)
print (df)

