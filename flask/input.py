import subprocess
import webbrowser
from flask import Flask, request, render_template, url_for, flash,redirect
import requests
import numpy as np
import os
from tmdbv3api import TMDb
from tmdbv3api import Movie
import urllib
from bs4 import BeautifulSoup
import pandas as pd
from functiontest import function
from form import RegistrationForm, LoginForm, inputForm, splitForm
from flask_sqlalchemy import SQLAlchemy

#Run Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config["CACHE_TYPE"] = "null"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#class Card(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  card = db.Column(db.String(3), unique=True)

@app.route('/', methods=['GET', 'POST'])
def register():
    form = inputForm()  
    if form.validate_on_submit():
        flash(f'Data Sent for {form.cardNumber.data}!', 'success')
        return redirect(url_for('split'))
    
    return render_template('input.html', form=form)
def form():
    card = request.form(inputForm.cardNumber)
    return print(card)

@app.route('/split', methods=["GET", "POST"])
def login():
    form = splitForm()
    card = request.form.get('cardNumber')
    tmdb = TMDb()
    tmdb.api_key = '03efb1cb001d35e7a9c5a2569f12d10c'
    tmdb.language = 'en'
    tmdb.debug = False
    website_url = requests.get('https://en.wikipedia.org/wiki/UFC_' + card)
    html = website_url.content
    ## Pulling Images from TheMovieDataBase.org
    movie = Movie()
	##Movie Search
    search = movie.search('UFC ' + card)
    print(search[0].id)
    ##Selects first card from results
    cardID = search[0].id
    ##Pulls the backdrop image path from TMDb
    backdropLink = search[0].backdrop_path
    originalPath = 'https://image.tmdb.org/t/p/original'
    directBackdrop = originalPath + backdropLink

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
    posterString = (dfInfo.Poster.to_string(index=False))
    ##Removing Characters from Poster String
    posterString = posterString[16:-1]
    dateString = (dfInfo.Date.to_string(index=False))
    venueString = (dfInfo.Venue.to_string(index=False))
    cityString = (dfInfo.City.to_string(index=False))
    attendanceString = (dfInfo.Attendance.to_string(index=False))
    gateString = (dfInfo.TotalGate.to_string(index=False))



    
    return render_template('split.html', form=form, inputForm=inputForm, card=card, website_url=website_url,
    						directBackdrop=directBackdrop, dateString=dateString, posterString=posterString, venueString=venueString,
                            attendanceString=attendanceString, gateString=gateString, cityString=cityString)



if __name__ == '__main__':
    app.run(debug=True)