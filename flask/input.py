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
from form import RegistrationForm, LoginForm, inputForm

#Run Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/', methods=['GET', 'POST'])
def register():
    form = inputForm()
    if form.validate_on_submit():
        flash(f'Data Sent for {form.cardNumber.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('input.html', form=form)

@app.route('/split', methods=["GET", "POST"])
def login():
    form = RegistrationForm()
    return render_template('register.html', form=form, inputForm=inputForm)



if __name__ == '__main__':
    app.run(debug=True)