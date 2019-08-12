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

#Run Flask
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('input.html')

if __name__ == '__main__':
    app.run()