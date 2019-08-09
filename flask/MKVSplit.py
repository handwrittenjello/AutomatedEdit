
import subprocess
import webbrowser
from flask import Flask, request, render_template
import requests
import numpy as np
import os

#Pulling UFC Data
print('You will import all fight card results to the database.  Which Card would you like to start with?')
firstCard = input()
website_url = requests.get('https://en.wikipedia.org/wiki/UFC_' + firstCard)
html = website_url.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

resultsTable = soup.find('table', class_ = 'toccolours')

ufcCard = []
weightClass = []
fighterWinner = []
defeat = []
fighterLoser = []
victoryType = []
victoryRound = []
victoryTime = []
notes =[]
ufcCard = []

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
df['Card'] = firstCard
df = df.replace('\n','', regex=True)
df = df.iloc[::-1]
df = df.tail(5)
df = df.drop(columns=['Notes'])
print (df)


#write HTML File
html_str = """

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>UFC Fight Card Splitter</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Free HTML5 Template by FreeHTML5.co" />
    <meta name="keywords" content="free html5, free template, free bootstrap, html5, css3, mobile first, responsive" />
    <meta name="author" content="FreeHTML5.co" />

  <!-- 
    //////////////////////////////////////////////////////

    FREE HTML5 TEMPLATE 
    DESIGNED & DEVELOPED by FREEHTML5.CO
        
    Website:        http://freehtml5.co/
    Email:          info@freehtml5.co
    Twitter:        http://twitter.com/fh5co
    Facebook:       https://www.facebook.com/fh5co

    //////////////////////////////////////////////////////
     -->

    <!-- Facebook and Twitter integration -->
    <meta property="og:title" content=""/>
    <meta property="og:image" content=""/>
    <meta property="og:url" content=""/>
    <meta property="og:site_name" content=""/>
    <meta property="og:description" content=""/>
    <meta name="twitter:title" content="" />
    <meta name="twitter:image" content="" />
    <meta name="twitter:url" content="" />
    <meta name="twitter:card" content="" />

    <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
    <link rel="shortcut icon" href="favicon.ico">

    <link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700" rel="stylesheet">
    
    <!-- Animate.css -->
    <link rel="stylesheet" href="{{ url_for('static',filename='css/animate.css') }}">
    <!-- Icomoon Icon Fonts-->
    <link rel="stylesheet" href="{{ url_for('static',filename='css/icomoon.css') }}">
    <!-- Simple Line Icons -->
    <link rel="stylesheet" href="{{ url_for('static',filename='css/simple-line-icons.css') }}">
    <!-- Bootstrap  -->
    <link rel="stylesheet" href="{{ url_for('static',filename='css/bootstrap.css') }}">
    <!-- Style -->
    <link rel="stylesheet" href="{{ url_for('static',filename='css/style.css') }}">


    <!-- Modernizr JS -->
    <script src="{{ url_for('static',filename='js/modernizr-2.6.2.min.js') }}"></script>
    <!-- FOR IE9 below -->
    <!--[if lt IE 9]>
    <script src="{{ url_for('static',filename='js/respond.min.js') }}"></script>
    <![endif]-->

    <style>
    .container { width: 100%; clear: both; }
    .container input { width: 100px; clear: both; }
    .container { display: flex; }
    .container {align-items: flex-start; }
    .navigation { display: flex; flex-flow: row wrap; justify-content: flex end }
    @media all and (max-width: 800px) {
        .navigation { justify-content: space-around;}    }
    @media all and (max-width: 500px){
        .navigation { flex-direction: column;}    }
    input [type="text"], textarea {
        background-color : d1d1d1;
    }
    </style>

    <section id="fh5co-home" data-section="home" style="background-image: {{ url_for('static',filename='images/full_image_1.jpg')}};" data-stellar-background-ratio="0.5">
        <div class="gradient"></div>
        <div class="container">
            <div class="text-wrap">
                <div class="text-inner">
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2 text-center">
                            <h1 class="to-animate">UFC Fightcard</h1>
                            <h2 class="to-animate">On this date</h2>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

 

    
    <!-- jQuery -->
    <script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
    <!-- jQuery Easing -->
    <script src="{{ url_for('static',filename='js/jquery.easing.1.3.js') }}"></script>
    <!-- Bootstrap -->
    <script src="{{ url_for('static',filename='js/bootstrap.min.js') }}"></script>
    <!-- Waypoints -->
    <script src="{{ url_for('static',filename='js/jquery.waypoints.min.js') }}"></script>
    <!-- Stellar Parallax -->
    <script src="{{ url_for('static',filename='js/jquery.stellar.min.js') }}"></script>
    <!-- Counters -->
    <script src="{{ url_for('static',filename='js/jquery.countTo.js') }}"></script>
    <!-- Main JS (Do not remove) -->
    <script src="{{ url_for('static',filename='js/main.js') }}"></script>

    <div style =".ufctable"></div>
        <div class="container">
            <div class="text-wrap">
                <div class="text-inner">
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2 text-center">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" text-align:center> 
                            <table id="FightCard">
                            <div style="text-align:center;">
                            {% for table in tables %}
                                    {{ table|safe }}
                            {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>





        <div class="navigation">
            <form action = '/ufc' method = "post">
                <div id = "filename">
                    <input type = "text" name = "ufcCard" placeholder="Filename"></li>
                    <input type = "text" name = "firstFightStart" placeholder="First Fight Start"></li>
                    <input type = "text" name = "firstFightEnd" placeholder="First Fight End"></li>
                    <input type = "text" name = "secondFightStart" placeholder="Second Fight Start"></li>
                    <input type = "text" name = "secondFightEnd" placeholder="Second Fight End"></li>
                    <input type = "text" name = "thirdFightStart" placeholder="Third Fight Start"></li>
                    <input type = "text" name = "thirdFightEnd" placeholder="Third Fight End"></li>
                    <input type = "text" name = "fourthFightStart" placeholder="Fourth Fight Start"></li>
                    <input type = "text" name = "fourthFightEnd" placeholder="Fourth Fight End"></li>
                    <input type = "text" name = "fifthFightStart" placeholder="Fifth Fight Start"></li>
                    <input type = "text" name = "fifthFightEnd" placeholder="Fifth Fight End"></li>
                                <input type = "submit" value = "Submit" />
                </div>
            </form>
        </div>

            <div id="fh5co-footer" role="contentinfo">
        <div class="container">
            <div class="row">
                <div class="col-md-4 to-animate">
                    <h3 class="section-title">About Me</h3>
                    <p>Blue Belt in Brazilian Jiu Jitsu.  White Belt in coding.</p>
                    <p class="copy-right">&copy; 2015 Twist Free Template. <br>All Rights Reserved. <br>
                        Designed by <a href="http://freehtml5.co/" target="_blank">FREEHTML5.co</a>
                        Demo Images: <a href="http://unsplash.com/" target="_blank">Unsplash</a>
                    </p>
                </div>

                <div class="col-md-4 to-animate">
                    <h3 class="section-title">Our Address</h3>
                    <ul class="contact-info">
                        <li><i class="icon-map-marker"></i>2700 Bennett Yard Road</li>
                        <li><i class="icon-phone"></i>724 713 2538</li>
                        <li><i class="icon-envelope"></i><a href="#">handwrittenjello@gmail.com</a></li>
                        <li><i class="icon-globe2"></i><a href="#">https://github.com/handwrittenjello</a></li>
                    </ul>
                    <h3 class="section-title">Connect with Us</h3>
                    <ul class="social-media">
                        <li><a href="#" class="facebook"><i class="icon-facebook"></i></a></li>
                        <li><a href="#" class="twitter"><i class="icon-twitter"></i></a></li>
                        <li><a href="#" class="dribbble"><i class="icon-dribbble"></i></a></li>
                        <li><a href="#" class="github"><i class="icon-github-alt"></i></a></li>
                    </ul>
                </div>
                <div class="col-md-4 to-animate">
                    <h3 class="section-title">Drop us a line</h3>
                    <form class="contact-form">
                        <div class="form-group">
                            <label for="name" class="sr-only">Name</label>
                            <input type="name" class="form-control" id="name" placeholder="Name">
                        </div>
                        <div class="form-group">
                            <label for="email" class="sr-only">Email</label>
                            <input type="email" class="form-control" id="email" placeholder="Email">
                        </div>
                        <div class="form-group">
                            <label for="message" class="sr-only">Message</label>
                            <textarea class="form-control" id="message" rows="7" placeholder="Message"></textarea>
                        </div>
                        <div class="form-group">
                            <input type="submit" id="btn-submit" class="btn btn-send-message btn-md" value="Send Message">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    </body>
</html>



"""


with open("./templates/UFC.html", "w") as file:
    file.write(html_str)

#Run Flask
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('UFC.html', tables=[df.to_html(classes='data',header='true')], titles=df.columns.values, lists=df.iloc[:5,1:5])
"""
def a():
    session['dataframe'] = df
    return redirect(url_for('b'))
"""

@app.route('/ufc', methods=['POST'])
def foo():
    card = request.form['ufcCard']
    firstFightStartInput = request.form['firstFightStart']
    firstFightStart = firstFightStartInput[:2] + ':' + firstFightStartInput[2:4] + ':' + firstFightStartInput[4:6]

    firstFightEndInput = request.form['firstFightEnd']
    firstFightEnd = firstFightEndInput[:2] + ':' + firstFightEndInput[2:4] + ':' + firstFightEndInput[4:6]

    secondFightStartInput = request.form['secondFightStart']
    secondFightStart = secondFightStartInput[:2] + ':' + secondFightStartInput[2:4] + ':' + secondFightStartInput[4:6]

    secondFightEndInput = request.form['secondFightEnd']
    secondFightEnd = secondFightEndInput[:2] + ':' + secondFightEndInput[2:4] + ':' + secondFightEndInput[4:6]

    thirdFightStartInput = request.form['thirdFightStart']
    thirdFightStart = thirdFightStartInput[:2] + ':' + thirdFightStartInput[2:4] + ':' + thirdFightStartInput[4:6]

    thirdFightEndInput = request.form['thirdFightEnd']
    thirdFightEnd = thirdFightEndInput[:2] + ':' + thirdFightEndInput[2:4] + ':' + thirdFightEndInput[4:6]

    fourthFightStartInput = request.form['fourthFightStart']
    fourthFightStart = fourthFightStartInput[:2] + ':' + fourthFightStartInput[2:4] + ':' + fourthFightStartInput[4:6]

    fourthFightEndInput = request.form['fourthFightEnd']
    fourthFightEnd = fourthFightEndInput[:2] + ':' + fourthFightEndInput[2:4] + ':' + fourthFightEndInput[4:6]

    fifthFightStartInput = request.form['fifthFightStart']
    fifthFightStart = fifthFightStartInput[:2] + ':' + fifthFightStartInput[2:4] + ':' + fifthFightStartInput[4:6]

    fifthFightEndInput = request.form['fifthFightEnd']
    fifthFightEnd = fifthFightEndInput[:2] + ':' + fifthFightEndInput[2:4] + ':' + fifthFightEndInput[4:6]

    runMKV = subprocess.call(['mkvmerge','-o', card + 'split.mkv', card + '.mkv', '--split', 'timestamps:'+ firstFightStart +','+ firstFightEnd + ',' + secondFightStart + ',' + secondFightEnd +
    ',' +thirdFightStart + ',' + thirdFightEnd + ',' + fourthFightStart + ',' + fourthFightEnd + ',' + fifthFightStart + ',' + fifthFightEnd])
##Removal of Commercial Breaks
    for i in range(1,11,2):
        os.remove(card + 'split-00' + str(i) + '.mkv')
##Removing 11th extra split
    os.remove(card + 'split-011.mkv')

##Defining Winners and losers from DataFrame
    fightOneWinner = df.loc[4]['Winner']
    fightOneLoser = df.loc[4]["Loser"]
    fightTwoWinner = df.loc[3]['Winner']
    fightTwoLoser = df.loc[3]['Loser']
    fightThreeWinner = df.loc[2]['Winner']
    fightThreeLoser = df.loc[2]['Loser']
    fightFourWinner = df.loc[1]['Winner']
    fightFourLoser = df.loc[1]['Loser']
    fightFiveWinner = df.loc[0]['Winner']
    fightFiveLoser = df.loc[0]['Loser']
    cardTable = df.loc[0]['Card']

##Defining Strings for file rename
    renameOriginOne = card+'split-002.mkv'
    renameOriginTwo = card+'split-004.mkv'
    renameOriginThree = card+'split-006.mkv'
    renameOriginFour = card+'split-008.mkv'
    renameOriginFive = card+'split-010.mkv'
    renameDestOne = 'UFC ' + cardTable + ' - ' + fightOneWinner + ' vs ' + fightOneLoser + '.mkv'
    renameDestTwo = 'UFC ' + cardTable + ' - ' + fightTwoWinner + ' vs ' + fightTwoLoser + '.mkv'
    renameDestThree = 'UFC ' + cardTable + ' - ' + fightThreeWinner + ' vs ' + fightThreeLoser + '.mkv'
    renameDestFour = 'UFC ' + cardTable + ' - ' + fightFourWinner + ' vs ' + fightFourLoser + '.mkv'
    renameDestFive = 'UFC ' + cardTable + ' - ' + fightFiveWinner + ' vs ' + fightFiveLoser + '.mkv'

    
##Renaming Files after split
    fileOneRename = os.rename(renameOriginOne,renameDestOne)
    fileTwoRename = os.rename(renameOriginTwo,renameDestTwo)
    fileThreeRename = os.rename(renameOriginThree,renameDestThree)
    fileFourRename = os.rename(renameOriginFour,renameDestFour)
    fileFiveRename = os.rename(renameOriginFive,renameDestFive)
    filerenamelist = [fileOneRename,fileTwoRename,fileThreeRename,fileFourRename,fileFiveRename]


    return  'You have successfully muxed Filename %s <br/> <a href="/">Back Home</a>' % (card);   

if __name__ == '__main__':
    app.run()





