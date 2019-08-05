import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
conf = yaml.safe_load(open('conf/application.yml'))
email = conf['user']['email']
pwd = conf['user']['password']

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

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div')))
driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div/div[9]/a/div[2]/div').click()
wait = WebDriverWait(driver,20)

driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys('UFC 239')
pyautogui.press('enter')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/a').click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/div/div[1]')))
tabToEdit = 0
while tabToEdit <10:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite('Amanda Nunes')
pyautogui.press('enter')
pyautogui.typewrite('Holly Holm')
pyautogui.press('enter')
tabToEdit = 0
while tabToEdit <4:
    pyautogui.press('tab')
    tabToEdit = tabToEdit +1
pyautogui.typewrite('UFC 239')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
