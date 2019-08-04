
import subprocess
import webbrowser
from flask import Flask, request, render_template
import requests
import numpy as np

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
print (df)


#write HTML File
html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
<style>
.floatLeft { width: 75%; float: left; }
.floatRight {width: 25%; float: right; }
.container { overflow: hidden; }
</style>
    <meta charset="UTF-8">
</head>
<div class="container">
<div class="floatLeft">

<body>
    <table id="FightCard"
    <caption>UFC FightCard Results</caption>
{% for table in tables %}
            {{ table|safe }}
{% endfor %}
</div>
<div class="floatRight">
<style>
table, th, td {
  border: 1px solid black;
}
</style>
  <table style="width:100%">
  <caption>Times</caption>
  <tr>
    <th>Fight Start</th>
    <th>Fight End</th>
  </tr>
  <tr>
    <td><input type = "text" name = "firstFightStart"</td>
    <td><input type = "text" name = "secondFightEnd"</td>
  </tr>
  <tr>
    <td><input type = "text" name = "firstFightStart"</td>
    <td><input type = "text" name = "secondFightEnd"</td>
  </tr>
</table> 
</div>
</div>


<form action = '/ufc' method = "post">
Filename: <input type = "text" name = "ufcCard"><br />
How many Fights?: <input type = "text" name = "ufcFightNumber"><br />
First Fight Start?: <input type = "text" name = "firstFightStart"><br />
First Fight End: <input type = "text" name = "firstFightEnd"><br />
<input type = "submit" value = "Submit" />
</form>

</html>

"""

with open("./templates/UFC.html", "w") as file:
    file.write(html_str)

#Run Flask
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('UFC.html', tables=[df.to_html(classes='data',header='true')], titles=df.columns.values, lists=df.iloc[:5,1:5])



@app.route('/ufc', methods=['POST'])
def foo():
    card = request.form['ufcCard']
    firstFightStartInput = request.form['firstFightStart']
    firstFightStart = firstFightStartInput[:2] + ':' + firstFightStartInput[2:4] + ':' + firstFightStartInput[4:6]

    firstFightEndInput = request.form['firstFightEnd']
    firstFightEnd = firstFightEndInput[:2] + ':' + firstFightEndInput[2:4] + ':' + firstFightEndInput[4:6]

    runMKV = subprocess.call(['mkvmerge','-o', card + 'split.mkv', card + '.mkv', '--split', 'timestamps:'+ firstFightStart +','+ firstFightEnd ])

    return 'You hav envtered Filename %s <br/> <a href="/">Back Home</a>' % (bar), runMKV;   

if __name__ == '__main__':
    app.run()
#UfcPage = open('UFC Fight Card.html', 'w')
#filename = 'file:///Users/andrewlittlejohn/projects/AutomatedEdit/' + 'UFC Fight Card.html'
#webbrowser.open_new_tab(filename)

print('How many fights are on this card?')
numberOfFights = input()

#if numberOfFights == '5':
#    print('Please enter the name of the file you would like to edit:')
#    filenameInput = input()
#    print('Please enter the start of the First Of 5 Fights')
#    firstFightStartInput = input()
#    firstFightStart = firstFightStartInput[:2] + ':' + firstFightStartInput[2:4] + ':' + firstFightStartInput[4:6]
#    print(firstFightStart)
#    print('Please enter the end of the First Fight')
#    firstFightEndInput = input()
#    firstFightEnd = firstFightEndInput[:2] + ':' + firstFightEndInput[2:4] + ':' + firstFightEndInput[4:6]
#    print(firstFightEnd)
#    subprocess.call([r'mkvmerge','-o', filenameInput + 'split.mkv', filenameInput + '.mkv', '--split', 'timestamps:'+firstFightStart+','+firstFightEnd])#

#    #If Fightcard has 6 fights
#elif numberOfFights == '6':
#    print('Please enter the name of the file you would like to edit:')
#    filenameInput = input()
#    print('Please enter the start of the First of 6 Fights')
#    firstFightStartInput = input()
#    firstFightStart = firstFightStartInput[:2] + ':' + firstFightStartInput[2:4] + ':' + firstFightStartInput[4:6]
#    print(firstFightStart)
#    print('Please enter the end of the First Fight')
#    firstFightEndInput = input()
#    firstFightEnd = firstFightEndInput[:2] + ':' + firstFightEndInput[2:4] + ':' + firstFightEndInput[4:6]
#    print(firstFightEnd)
#    subprocess.call([r'mkvmerge','-o', filenameInput + 'split.mkv', filenameInput + '.mkv', '--split', 'timestamps:'+firstFightStart+','+firstFightEnd])