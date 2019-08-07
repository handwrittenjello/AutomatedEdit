##Import all
import subprocess
import webbrowser
from flask import Flask, request, render_template
import requests
import numpy as np
import os

##Create User Input Question
print('How many movies will you be importing today?')
movieNumber = input()

htmlStringBegining = """
<!DOCTYPE html>
<html lang="en">
<head>
<form action = '/handbrake' method = "post">"""

htmlStringMiddle = """
<p>Show a file-select field which allows a file to be chosen for upload:</p>
<form action="/action_page.php">
  Select a file: <input type="file" name="myFile"><br><br>"""

htmlStringEnd = """
  <input type="submit" name="Submit">
  </form>
  </head>
  </html>"""

hmtlStringJoined = htmlStringBegining + (htmlStringMiddle * int(movieNumber)) + htmlStringEnd

print(hmtlStringJoined)

##Use HTML creator
with open("./templates/Handbrake.html", "w") as file:
    file.write(hmtlStringJoined)

#Run Flask
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('Handbrake.html')

@app.route('/handbrake', methods=['POST'])
def foo():
    card = request.form['myFile']
    print(card)

    runHandbrake = '/Users/andrewlittlejohn/bin/HandBrakeCLI -i %s -o 1%s --preset-import-file drew.json' % (card,card)
    subprocess.call(runHandbrake,shell=True)

    return  'You have successfully sent %s to be transcoded<br/> <a href="/">Back Home</a>' % (card);   

if __name__ == '__main__':
    app.run()
# Create user input browse paths