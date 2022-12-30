import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager #using webdriver manager
from selenium.webdriver.common.by import By #importing By idk what it does lol
from selenium.webdriver.support.wait import WebDriverWait #for WebDriverWait... in case u couldnt tell
from selenium.common.exceptions import NoSuchElementException #try except
import csv #damn idk if im supposed to import this much stuff but filewriter/reader basically

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #set up the browser
filename = "normaltitle" #create the file

driver.get('https://quizlet.com/280584853/anth101-week-10-hw-flash-cards/')
WebDriverWait(driver, timeout=100)
fullInfo = driver.find_element(By.CLASS_NAME, 'SetPageTerms-termsList').text

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', dialect='excel') #spaces in between chars
    csvwriter.writerows([[fullInfo]]) #dont use writerow, that just writes first term

with open('normaltitle', mode = 'r') as csvfile: #read out the csv file
    csvFile = csv.reader(csvfile)
    for lines in csvFile:
        print(lines)