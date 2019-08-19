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
#from flask_sqlalchemy import SQLAlchemy
import time
import json

#Run Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config["CACHE_TYPE"] = "null"


@app.route('/', methods=['GET', 'POST'])
def register():
    form = inputForm()  
    if form.validate_on_submit():
        flash(f'Data Sent for {form.cardNumber.data}!', 'success')
        return redirect(url_for('split'))
    
    return render_template('input.html', form=form)
def form():
    card = request.form(inputForm.cardNumber)
    cardType = request.form(inputForm.cardNumberSelect)
    return print(card)

@app.route('/split', methods=["GET", "POST"])
def login():
    form = splitForm()
    card = request.form.get('cardNumber')
    global cardType
    cardType = request.form.get('cardNumberSelect')
    #print(cardType)
    tmdb = TMDb()
    tmdb.api_key = '03efb1cb001d35e7a9c5a2569f12d10c'
    tmdb.language = 'en'
    tmdb.debug = False
    if cardType == 'ppv':
        website_url = requests.get('https://en.wikipedia.org/wiki/UFC_' + card)
    elif cardType == 'espn':
        card = card.replace(' ', '_')
        website_url = requests.get('https://en.wikipedia.org/wiki/UFC_on_ESPN:_' + card)
        print(card)
        card = card.replace('_', ' ')
    elif cardType == 'fightNight':
        card = card.replace(' ', '_')
        website_url = requests.get('https://en.wikipedia.org/wiki/UFC_Fight_Night:_' + card)
        print(card)
        card = card.replace('_', ' ')
    html = website_url.content
    ## Pulling Images from TheMovieDataBase.org
    movie = Movie()
	##Movie Search
    if cardType == 'ppv':
        search = movie.search('UFC ' + card)
    elif cardType == 'espn':
        search = movie.search(card)
    elif cardType == 'fightNight':
        search = movie.search(card)
        #print(card)
    #print(search)
    #print(search[0].id)
    ##Selects first card from results
    cardID = search[0].id
    ##Pulls the backdrop image path from TMDb
    backdropLink = search[0].backdrop_path
    #print(backdropLink)
    originalPath = 'https://image.tmdb.org/t/p/original'
    if not backdropLink:
        directBackdrop = '000000'
    else:
        directBackdrop = 'url(' + originalPath + backdropLink +')'
    
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
    #tablePreviousCard.append(tdInfo[10].find(text=True))
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
    #dfInfo['Table Previous'] = tablePreviousCard
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

    ##Creating datafrom from pulled results table from Wikiscraper
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


    ##Addes rows to the datatable based on UFC Results
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


    global df
    df=pd.DataFrame(weightClass, columns=['Weight Class'])
    df['Winner'] = fighterWinner
    df['def'] = defeat
    df['Loser'] = fighterLoser
    df['Won By'] = victoryType
    df['Round'] = victoryRound
    df['Time'] = victoryTime
    df['Notes'] = notes
    df['Card'] = card
    df = df.replace('\n','', regex=True)
    df = df.iloc[::-1]
    if cardType == 'ppv':
        df = df.tail(5)
    elif cardType == 'espn':
        df = df.tail(6)
    elif cardType == 'fightNight':
        df = df.tail(6)
    df = df.drop(columns=['Notes'])
    #print (df)
    #print (dfJson)





    if cardType == 'ppv':
        return render_template('split.html', form=form, inputForm=inputForm, card=card, website_url=website_url,
                                directBackdrop=directBackdrop, dateString=dateString, posterString=posterString, venueString=venueString,
                                attendanceString=attendanceString, gateString=gateString, cityString=cityString, 
                                tables=[df.to_html(classes='data',header='true')], titles=df.columns.values, lists=df.iloc[:5,1:5], df=df, 
                                cardType=cardType)
    elif cardType == 'espn':
        return render_template('espnsplit.html', form=form, inputForm=inputForm, card=card, website_url=website_url,
                                directBackdrop=directBackdrop, dateString=dateString, posterString=posterString, venueString=venueString,
                                attendanceString=attendanceString, gateString=gateString, cityString=cityString, 
                                tables=[df.to_html(classes='data',header='true')], titles=df.columns.values, lists=df.iloc[:5,1:5], df=df, 
                                cardType=cardType)
    elif cardType == 'fightNight':
        return render_template('espnsplit.html', form=form, inputForm=inputForm, card=card, website_url=website_url,
                                directBackdrop=directBackdrop, dateString=dateString, posterString=posterString, venueString=venueString,
                                attendanceString=attendanceString, gateString=gateString, cityString=cityString, 
                                tables=[df.to_html(classes='data',header='true')], titles=df.columns.values, lists=df.iloc[:5,1:5], df=df, 
                                cardType=cardType)



@app.route('/ufc', methods=['GET', 'POST'])
def foo():
    print(df)
    global card
    card = request.form['filename']
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

    if cardType == 'ppv':
        runMKV = subprocess.call(['mkvmerge','-o', card + 'split.mkv', card + '.mkv', '--split', 'timestamps:'+ 
                                firstFightStart +','+ firstFightEnd + ',' + secondFightStart + ',' + secondFightEnd +
                                ',' +thirdFightStart + ',' + thirdFightEnd + ',' + fourthFightStart + ',' + fourthFightEnd 
                                + ',' + fifthFightStart + ',' + fifthFightEnd])

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


    elif cardType == 'espn':
        sixthFightStartInput = request.form['sixthFightStart']
        sixthFightStart = sixthFightStartInput[:2] + ':' + sixthFightStartInput[2:4] + ':' + sixthFightStartInput[4:6]
        sixthFightEndInput = request.form['sixthFightEnd']
        sixthFightEnd = sixthFightEndInput[:2] + ':' + sixthFightEndInput[2:4] + ':' + sixthFightEndInput[4:6]
        runMKV = subprocess.call(['mkvmerge','-o', card + 'split.mkv', card + '.mkv', '--split', 'timestamps:'+ 
                                firstFightStart +','+ firstFightEnd + ',' + secondFightStart + ',' + secondFightEnd +
                                ',' +thirdFightStart + ',' + thirdFightEnd + ',' + fourthFightStart + ',' + fourthFightEnd 
                                + ',' + fifthFightStart + ',' + fifthFightEnd + ',' + sixthFightStart + ',' + sixthFightEnd])

        ##Removal of Commercial Breaks
        for i in range(1,11,2):
            os.remove(card + 'split-00' + str(i) + '.mkv')
        ##Removing 11th extra split
        os.remove(card + 'split-011.mkv')
        ##Removing 13th extra split
        os.remove(card + 'split-013.mkv')


        ##Defining Winners and losers from DataFrame
        fightOneWinner = df.loc[5]['Winner']
        fightOneLoser = df.loc[5]["Loser"]
        fightTwoWinner = df.loc[4]['Winner']
        fightTwoLoser = df.loc[4]['Loser']
        fightThreeWinner = df.loc[3]['Winner']
        fightThreeLoser = df.loc[3]['Loser']
        fightFourWinner = df.loc[2]['Winner']
        fightFourLoser = df.loc[2]['Loser']
        fightFiveWinner = df.loc[1]['Winner']
        fightFiveLoser = df.loc[1]['Loser']
        fightSixWinner = df.loc[0]['Winner']
        fightSixLoser = df.loc[0]['Loser']
        cardTable = df.loc[0]['Card']

    ##Defining Strings for file rename
        renameOriginOne = card+'split-002.mkv'
        renameOriginTwo = card+'split-004.mkv'
        renameOriginThree = card+'split-006.mkv'
        renameOriginFour = card+'split-008.mkv'
        renameOriginFive = card+'split-010.mkv'
        renameOriginSix = card+'split-012.mkv'
        renameDestOne = 'UFC on ESPN: ' + cardTable + ' - ' + fightOneWinner + ' vs ' + fightOneLoser + '.mkv'
        renameDestTwo = 'UFC on ESPN: ' + cardTable + ' - ' + fightTwoWinner + ' vs ' + fightTwoLoser + '.mkv'
        renameDestThree = 'UFC on ESPN: ' + cardTable + ' - ' + fightThreeWinner + ' vs ' + fightThreeLoser + '.mkv'
        renameDestFour = 'UFC on ESPN: ' + cardTable + ' - ' + fightFourWinner + ' vs ' + fightFourLoser + '.mkv'
        renameDestFive = 'UFC on ESPN: ' + cardTable + ' - ' + fightFiveWinner + ' vs ' + fightFiveLoser + '.mkv'
        renameDestSix = 'UFC on ESPN: ' + cardTable + ' - ' + fightSixWinner + ' vs ' + fightSixLoser + '.mkv'


        
    ##Renaming Files after split
        fileOneRename = os.rename(renameOriginOne,renameDestOne)
        fileTwoRename = os.rename(renameOriginTwo,renameDestTwo)
        fileThreeRename = os.rename(renameOriginThree,renameDestThree)
        fileFourRename = os.rename(renameOriginFour,renameDestFour)
        fileFiveRename = os.rename(renameOriginFive,renameDestFive)
        fileSixRename = os.rename(renameOriginSix,renameDestSix)
        filerenamelist = [fileOneRename,fileTwoRename,fileThreeRename,fileFourRename,fileFiveRename,fileSixRename]

    elif cardType == 'fightNight':
        sixthFightStartInput = request.form['sixthFightStart']
        sixthFightStart = sixthFightStartInput[:2] + ':' + sixthFightStartInput[2:4] + ':' + sixthFightStartInput[4:6]
        sixthFightEndInput = request.form['sixthFightEnd']
        sixthFightEnd = sixthFightEndInput[:2] + ':' + sixthFightEndInput[2:4] + ':' + sixthFightEndInput[4:6]
        runMKV = subprocess.call(['mkvmerge','-o', card + 'split.mkv', card + '.mkv', '--split', 'timestamps:'+ 
                                firstFightStart +','+ firstFightEnd + ',' + secondFightStart + ',' + secondFightEnd +
                                ',' +thirdFightStart + ',' + thirdFightEnd + ',' + fourthFightStart + ',' + fourthFightEnd 
                                + ',' + fifthFightStart + ',' + fifthFightEnd + ',' + sixthFightStart + ',' + sixthFightEnd])

        ##Removal of Commercial Breaks
        for i in range(1,11,2):
            os.remove(card + 'split-00' + str(i) + '.mkv')
        ##Removing 11th extra split
        os.remove(card + 'split-011.mkv')
        ##Removing 13th extra split
        os.remove(card + 'split-013.mkv')


        ##Defining Winners and losers from DataFrame
        fightOneWinner = df.loc[5]['Winner']
        fightOneLoser = df.loc[5]["Loser"]
        fightTwoWinner = df.loc[4]['Winner']
        fightTwoLoser = df.loc[4]['Loser']
        fightThreeWinner = df.loc[3]['Winner']
        fightThreeLoser = df.loc[3]['Loser']
        fightFourWinner = df.loc[2]['Winner']
        fightFourLoser = df.loc[2]['Loser']
        fightFiveWinner = df.loc[1]['Winner']
        fightFiveLoser = df.loc[1]['Loser']
        fightSixWinner = df.loc[0]['Winner']
        fightSixLoser = df.loc[0]['Loser']
        cardTable = df.loc[0]['Card']

    ##Defining Strings for file rename
        renameOriginOne = card+'split-002.mkv'
        renameOriginTwo = card+'split-004.mkv'
        renameOriginThree = card+'split-006.mkv'
        renameOriginFour = card+'split-008.mkv'
        renameOriginFive = card+'split-010.mkv'
        renameOriginSix = card+'split-012.mkv'
        renameDestOne = 'UFC Fight Night: ' + cardTable + ' - ' + fightOneWinner + ' vs ' + fightOneLoser + '.mkv'
        renameDestTwo = 'UFC Fight Night: ' + cardTable + ' - ' + fightTwoWinner + ' vs ' + fightTwoLoser + '.mkv'
        renameDestThree = 'UFC Fight Night: ' + cardTable + ' - ' + fightThreeWinner + ' vs ' + fightThreeLoser + '.mkv'
        renameDestFour = 'UFC Fight Night: ' + cardTable + ' - ' + fightFourWinner + ' vs ' + fightFourLoser + '.mkv'
        renameDestFive = 'UFC Fight Night: ' + cardTable + ' - ' + fightFiveWinner + ' vs ' + fightFiveLoser + '.mkv'
        renameDestSix = 'UFC Fight Night: ' + cardTable + ' - ' + fightSixWinner + ' vs ' + fightSixLoser + '.mkv'


        
    ##Renaming Files after split
        fileOneRename = os.rename(renameOriginOne,renameDestOne)
        fileTwoRename = os.rename(renameOriginTwo,renameDestTwo)
        fileThreeRename = os.rename(renameOriginThree,renameDestThree)
        fileFourRename = os.rename(renameOriginFour,renameDestFour)
        fileFiveRename = os.rename(renameOriginFive,renameDestFive)
        fileSixRename = os.rename(renameOriginSix,renameDestSix)
        filerenamelist = [fileOneRename,fileTwoRename,fileThreeRename,fileFourRename,fileFiveRename,fileSixRename]


    return  'You have successfully muxed Filename %s <br/> <a href="/">Back Home</a>' % (card);  


if __name__ == '__main__':
    app.run(debug=True)