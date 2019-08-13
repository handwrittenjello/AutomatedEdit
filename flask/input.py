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
    
    return render_template('split.html', form=form, inputForm=inputForm, card=card, website_url=website_url,
    						directBackdrop=directBackdrop)



if __name__ == '__main__':
    app.run(debug=True)