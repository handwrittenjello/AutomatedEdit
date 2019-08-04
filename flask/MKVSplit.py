
import subprocess
import webbrowser
from flask import Flask, request, render_template

#write HTML File
html_str = """
<p>UFC Fight Card</p>

<form action = '/ufc' method = "post">
Filename: <input type = "text" name = "ufcCard"><br />
How many Fights?: <input type = "text" name = "ufcFightNumber"><br />
First Fight Start?: <input type = "text" name = "firstFightStart"><br />
First Fight End: <input type = "text" name = "firstFightEnd"><br />
<input type = "submit" value = "Submit" />
</form>

"""

with open("./templates/UFC.html", "w") as file:
    file.write(html_str)

#Run Flask
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('UFC.html')



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