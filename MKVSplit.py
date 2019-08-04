
import subprocess
import webbrowser
from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('UFC.html')



@app.route('/ufc', methods=['POST'])
def foo():
    bar = request.form['ufcCard']
    firstFightStart = request.form['firstFightStart']
    firstFightEnd = request.form['firstFightEnd']
    return 'You hav envtered Filename %s <br/> <a href="/">Back Home</a>' % (bar),
    subprocess.call([r'mkvmerge','-o', 'ufc1' + 'split.mkv', 'ufc1' + '.mkv', '--split', 'timestamps:'+firstFightStart+','+firstFightEnd]);
   

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