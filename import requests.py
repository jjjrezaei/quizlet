import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager #using webdriver manager
from selenium.webdriver.common.by import By #importing By idk what it does lol
from selenium.webdriver.support.wait import WebDriverWait #for WebDriverWait... in case u couldnt tell
from selenium.common.exceptions import NoSuchElementException #try except
import csv #filewriter/reader

class quizletCSV(object):
    def __init__(self, fileName, link):
        self.fileName = fileName
        self.link = link

    def createCSV(self, fileName): #creates a new BLANK csv file
        with open(fileName, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', dialect='excel') #creates csvwriter object
            csvwriter.writerow(' ')
        print('createCSV executed...')

    def writeCSV(self, fileName, link):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #set up the browser
        driver.get(link)
        WebDriverWait(driver, timeout=100)
        fullInfo = driver.find_element(By.CLASS_NAME, 'SetPageTerms-termsList').text

        with open(fileName,'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', dialect='excel') #creates csvwriter object
            csvwriter.writerows([[fullInfo]]) #dont use writerow, that just writes first term

        with open(fileName, mode = 'r') as csvfile: #read out the csv file
            csvFile = csv.reader(csvfile)
            for lines in csvFile:
                print(lines)
        print('writeCSV executed...')
    def diffLink(self, newLink, link):
        self.link = newLink 


newOrOldInput = input('do you want to append to a new document or an old document? type NEW or OLD')
nameFile = input('what do you want to name your file?')
linkName = input('paste the link you want to append to your file')

if newOrOldInput == 'NEW':
    newFile = quizletCSV(nameFile, linkName)
    newFile.createCSV(nameFile)
    newFile.writeCSV(nameFile, linkName)

    while(input('do you want to add another link? type NO to quitpaste ') != 'NO'):
        linkName = input('paste link here')
        newFile.writeCSV(nameFile, linkName)
        
    #do you want to submit another link? while !no prompt for link then call class again...
    #does tihs create a new class instance each time? how to avoid that?
    #in general the logic here is off bc fileName in createCSV method is not used.. fix this
elif newOrOldInput == 'OLD':
    nameFile = input('what is the name of the file you want to open?')
    linkName = input('paste the link you want to append to your file')
    quizletCSV()
else:
    print('unrecognized input, type either NEW or OLD')

print('pls - end')