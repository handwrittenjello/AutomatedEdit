import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
conf = yaml.safe_load(open('conf/application.yml'))
email = conf['user']['email']
pwd = conf['user']['password']

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

##Defining Web Driver
driver = webdriver.Chrome()
driver.implicitly_wait(20 )
driver.get('https://app.plex.tv/desktop#')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/button[3]')))



driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[3]/button[3]').click()
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="plex"]/div[2]/div/div/div[2]/form/button').click()

#clickong on UFC Sidebar
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div')))
driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div').click()
wait = WebDriverWait(driver,20)


##First Fight
print('Please select UFC ' + cardTable + ' ' + fightOneWinner + ' vs ' + fightOneLoser)
wait = WebDriverWait(driver,20)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys('UFC 239 - 1')
pyautogui.press('enter')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/a').click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]')))
tabToEdit = 0
while tabToEdit <10:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite(fightOneWinner)
pyautogui.press('enter')
pyautogui.typewrite(fightOneLoser)
pyautogui.press('enter')
tabToEdit = 0
while tabToEdit <4:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
#Collections
pyautogui.typewrite('UFC ' + cardTable)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
##Saving
pyautogui.press('enter')




##Second Fight
print('Please select UFC ' + cardTable + ' ' + fightTwoWinner + ' vs ' + fightTwoLoser)
WebDriverWait(driver, 10)
time.sleep(10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div')))
#driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div').click()
wait = WebDriverWait(driver,20)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys('UFC 239 - 2')
pyautogui.press('enter')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/a').click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]')))
tabToEdit = 0
while tabToEdit <10:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite(fightTwoWinner)
pyautogui.press('enter')
pyautogui.typewrite(fightTwoLoser)
pyautogui.press('enter')
tabToEdit = 0
while tabToEdit <4:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
#Collections
pyautogui.typewrite('UFC ' + cardTable)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
##Saving
pyautogui.press('enter')



##Third Fight
print('Please select UFC ' + cardTable + ' ' + fightThreeWinner + ' vs ' + fightThreeLoser)
WebDriverWait(driver, 10)
time.sleep(10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div')))
#driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div').click()
wait = WebDriverWait(driver,20)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys('UFC 239 - 3')
pyautogui.press('enter')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/a').click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]')))
tabToEdit = 0
while tabToEdit <10:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite(fightThreeWinner)
pyautogui.press('enter')
pyautogui.typewrite(fightThreeLoser)
pyautogui.press('enter')
tabToEdit = 0
while tabToEdit <4:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
#Collections
pyautogui.typewrite('UFC ' + cardTable)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
##Saving
pyautogui.press('enter')


##Fourth Fight
print('Please select UFC ' + cardTable + ' ' + fightFourWinner + ' vs ' + fightFourLoser)
WebDriverWait(driver, 10)
time.sleep(10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div')))
#driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div').click()
wait = WebDriverWait(driver,20)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys('UFC 239 - 4')
pyautogui.press('enter')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/a').click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]')))
tabToEdit = 0
while tabToEdit <10:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite(fightFourWinner)
pyautogui.press('enter')
pyautogui.typewrite(fightFourLoser)
pyautogui.press('enter')
tabToEdit = 0
while tabToEdit <4:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
#Collections
pyautogui.typewrite('UFC ' + cardTable)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
##Saving
pyautogui.press('enter')



##Fifth Fight
print('Please select UFC ' + cardTable + ' ' + fightFiveWinner + ' vs ' + fightFiveLoser)
WebDriverWait(driver, 10)
time.sleep(10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div')))
#driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div').click()
wait = WebDriverWait(driver,20)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys('UFC 239 - 5')
pyautogui.press('enter')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/a').click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]')))
tabToEdit = 0
while tabToEdit <10:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite(fightFiveWinner)
pyautogui.press('enter')
pyautogui.typewrite(fightFiveLoser)
pyautogui.press('enter')
tabToEdit = 0
while tabToEdit <4:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
#Collections
pyautogui.typewrite('UFC ' + cardTable)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
##Saving
pyautogui.press('enter')

