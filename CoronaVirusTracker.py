from tkinter import *
from bs4 import BeautifulSoup
import requests
from threading import Thread

root = Tk()

root.title('2020 coronavirus pandemic in Pakistan')

root.iconbitmap('virus.ico')

confirmedCasesText = StringVar()
deathsText = StringVar()
recoveredText = StringVar()


countries = ['Pakistan' , 'United States', 'Italy', 'Spain', 'China', 'India']
country = StringVar()
country.set(countries[0])


mainFrame = Frame(root, height = 600, width = 900)
mainFrame.pack()

titleText = StringVar()
titleText.set('2020 coronavirus pandemic in Pakistan')
title = Label(mainFrame, font = ('Arial', 18), textvariable = titleText)

confirmedCases =  Label(mainFrame, font = ('Montserrat', 32), textvariable = confirmedCasesText, fg = '#2e2e2e')

recovered =  Label(mainFrame, font = ('Montserrat', 32), textvariable = recoveredText, fg = '#2e2e2e')

deaths =  Label(mainFrame, font = ('Montserrat', 32), textvariable = deathsText, fg = '#2e2e2e')

loadingMessage = Label(mainFrame, font = ('Arial', 16), text = 'Wait while the stats are loading....')


def loadStats(countryName):

    loadingMessage.place(x = 310, y = 550)

    global confirmedCasesText
    confirmedCasesText.set('...')

    global recoveredText
    recoveredText.set('...')

    global deathsText
    deathsText.set('...')

    request = requests.get('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_{}'.format(countryName))

    page = BeautifulSoup(request.text, 'html.parser')

    global titleText
    titleText.set(page.title.text)
    
    title.update_idletasks()

    infoTable = page.find('table', class_='infobox').find('tbody').findAll('tr')

    requiredData = ['Confirmed cases', 'Recovered', 'Deaths']

    for row in infoTable:
        
        if row.th is not None and row.th.text in requiredData:

            if '(' in row.td.text:
                
                stats = row.td.text.split('(')[0]

            elif '[' in row.td.text:

                stats = row.td.text.split('[')[0]

            if row.th.text == 'Confirmed cases':
                
                confirmedCasesText.set(stats)

            elif row.th.text == 'Recovered':
                
                recoveredText.set(stats)

            elif row.th.text == 'Deaths':

                deathsText.set(stats)

    loadingMessage.place_forget()

thread = Thread(target = loadStats, args = (country.get(),))
thread.start()

def switchCountry(value):

    thread = Thread(target = loadStats, args = (country.get(),))
    thread.start()

def refresh():

    thread = Thread(target = loadStats, args = (country.get(),))
    thread.start()
    

confirmedCasesLabel =  Label(mainFrame, font = ('Arial', 14), text = 'Confirmed Cases')

deathsLabel =  Label(mainFrame, font = ('Arial', 14), text = 'Deaths')

recoveredLabel =  Label(mainFrame, font = ('Arial', 14), text = 'Recovered')

countrySelector = OptionMenu(mainFrame, country, *countries, command = switchCountry)

refreshButton = Button(mainFrame, font = ('Arial', 14), text = 'Refresh', relief = RAISED, command = refresh)

countrySelector.config(font = ('Aerial' , 14) , relief = RAISED)

title.place(x = 40, y = 30)
confirmedCases.place(x = 40, y = 100)
confirmedCasesLabel.place(x = 40, y = 165)
deaths.place(x = 40, y = 235)
deathsLabel.place(x = 40, y = 300)
recovered.place(x = 40, y = 370)
recoveredLabel.place(x = 40, y = 440)
countrySelector.place(x = 640, y = 150)
loadingMessage.place(x = 310, y = 550)
refreshButton.place(x = 640, y = 100)

root.mainloop()
