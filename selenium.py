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


##Defining Web Driver
driver = webdriver.Chrome()
driver.implicitly_wait(20 )
driver.get('localhost:5000')
wait = WebDriverWait(driver, 10)



driver.find_element_by_name('cardNumber').send_keys(240)



