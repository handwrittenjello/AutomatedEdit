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

##Creating datafrom for Fight info from pulled results table from Wikiscraper
soupInfo = BeautifulSoup(html, 'lxml')


infoTable = soupInfo.find('table', class_ = 'infobox')
##Creating lists for the dataframe
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
##Pulling data from cells
tdInfo = infoTable.findAll('td')
poster.append(tdInfo[0].find(text=True))
promotion.append(tdInfo[1].find(text=True))
date.append(tdInfo[2].find(text=True))
venue.append(tdInfo[3].find(text=True))
city.append(tdInfo[4].find(text=True))
attendance.append(tdInfo[5].find(text=True))
totalGate.append(tdInfo[6].find(text=True))
previousCard.append(tdInfo[7].find(text=True))
currentCard.append(tdInfo[8].find(text=True))
futureCard.append(tdInfo[9].find(text=True))
tablePreviousCard.append(tdInfo[10].find(text=True))
##Populating data from from lists
dfInfo=pd.DataFrame(poster, columns=['Poster'])
dfInfo['Promotion'] = promotion
dfInfo['Date'] = date
dfInfo['Venue'] = venue
dfInfo['City'] = city
dfInfo['Attendance'] = attendance
dfInfo['TotalGate'] = totalGate
dfInfo['Previous Card'] = previousCard
dfInfo['Current Card'] = currentCard
dfInfo['Future Card'] = futureCard
dfInfo['Table Previous'] = tablePreviousCard
dfInfo = dfInfo.replace('\n','', regex=True)
dfInfo = dfInfo.replace("\xa0",' ', regex=True)
dateString = (dfInfo.Date.to_string(index=False))
venueString = (dfInfo.Venue.to_string(index=False))
cityString = (dfInfo.City.to_string(index=False))
attendanceString = (dfInfo.Attendance.to_string(index=False))
gateString = (dfInfo.TotalGate.to_string(index=False))



