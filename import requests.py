import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager #using webdriver manager
from selenium.webdriver.common.by import By #importing By idk what it does lol
from selenium.webdriver.support.wait import WebDriverWait #for WebDriverWait... in case u couldnt tell
from selenium.common.exceptions import NoSuchElementException #try except
import csv #damn idk if im supposed to import this much stuff but filewriter/reader basically

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://quizlet.com/750452137/pol-s-428-test-3-flash-cards/')
WebDriverWait(driver, timeout=100)

try:
    t = driver.find_element(By.CLASS_NAME, 'SetPageTerms-termsList').text

    filename = "normaltitle"

    with open(filename, 'w') as csvfile:
        
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', dialect='excel') #spaces in between chars
        csvwriter.writerows([[t]]) #writerow just writes first term; brackets place the item in sequence but chars still considered individual fields hence why there's a comma between each letter
        print("csv created :)")

    with open('normaltitle', mode = 'r') as csvfile: #read out the csv file just created
        csvFile = csv.reader(csvfile)
        for lines in csvFile:
            print(lines)

except NoSuchElementException:
    print("fail lmao")
    pass