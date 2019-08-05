
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


<body>
    <table id="FightCard"
    <caption>UFC FightCard Results</caption>
{% for table in tables %}
            {{ table|safe }}
{% endfor %}




<form action = '/ufc' method = "post">
Filename: <input type = "text" name = "ufcCard"><br />
First Fight Start: <input type = "text" name = "firstFightStart"><br />
First Fight End: <input type = "text" name = "firstFightEnd"><br />
Second Fight Start: <input type = "text" name = "secondFightStart"><br />
Second Fight End: <input type = "text" name = "secondFightEnd"><br />
Third Fight Start: <input type = "text" name = "thirdFightStart"><br />
Third Fight End: <input type = "text" name = "thirdFightEnd"><br />
Fourth Fight Start: <input type = "text" name = "fourthFightStart"><br />
Fourth Fight End: <input type = "text" name = "fourthFightEnd"><br />
Fifth Fight Start: <input type = "text" name = "fifthFightStart"><br />
Fifth Fight End: <input type = "text" name = "fifthFightEnd"><br />

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

def a():
    session['dataframe'] = df
    return redirect(url_for('b'))


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

    for i in range(1,11,2):
        os.remove(card + 'split-00' + str(i) + '.mkv')
    
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
    
    return 'You have successfully muxed Filename %s <br/> <a href="/">Back Home</a>' % (card), runMKV, printdf;   

if __name__ == '__main__':
    app.run()





