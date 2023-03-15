from CandidateClass import Candidate
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

import openpyxl

from openpyxl import Workbook, load_workbook

book = load_workbook('data_source.xlsx')

sheet = book.active
whastAppLink = 'https://api.whatsapp.com/send?phone='
candidateList = []

candidateNameColumn = sheet['D']
courseColumn = sheet['E']
emailColumn = sheet['F']
dddColumn = sheet['I']
celColumn = sheet['J']



def createAndPopulateCandidateinstacies(candidateList):
    counter = 3
    bufferName = 'Begin'
    for currentCell in range(len(candidateNameColumn) - 3):
        if(candidateNameColumn[counter].value == bufferName):
            counter += 1   
        else:
            bufferName = candidateNameColumn[counter].value 
            candidateList.append(Candidate(name=candidateNameColumn[counter].value, course=courseColumn[counter].value, email=emailColumn[counter].value, ddd=dddColumn[counter].value, celNumber=celColumn[counter].value),)
            counter += 1   


def correctCelNumber(candidateList):
    for currentCell in range(len(candidateList)):
        numberList = map(int, str(candidateList[currentCell].celNumber))
        numberList = list(numberList)
        if(len(numberList) < 9):
            numberList.insert(0, 9)
            s = [str(integer) for integer in numberList]
            a_string = "".join(s)
            candidateList[currentCell].celNumber = int(a_string)

        # print('Candidato: \n' + candidateList[currentCell].name + '\n' + candidateList[currentCell].course + '\n' + candidateList[currentCell].email + '\n' + str(candidateList[currentCell].ddd) + '\n' + str(candidateList[currentCell].celNumber) + '\n' + '-------------//-------------')
    
def openBrowserAndSendMessage(candidateList, massege):
    codedMassege = ''
    chrome = webdriver.Chrome()
    chrome.get('https://web.whatsapp.com/')
    time.sleep(15)
    for indexCandidate in range(len(candidateList)):
        for index in range(len(massege)):
            if(massege[index] == 'candidateList[index].name'):
                codedMassege = codedMassege + candidateList[indexCandidate].name

            elif(massege[index] == 'candidateList[index].course'):
                codedMassege = codedMassege + candidateList[indexCandidate].course

            elif(massege[index] == 'candidateList[index].email'):
                codedMassege = codedMassege + candidateList[indexCandidate].email
    
            elif(massege[index] == 'candidateList[index].ddd'):
                codedMassege = codedMassege + candidateList[indexCandidate].ddd

            elif(massege[index] == 'candidateList[index].celNumber'):
                codedMassege = codedMassege + candidateList[indexCandidate].celNumber

            else:
                codedMassege = codedMassege + massege[index]
            
        print(codedMassege)
        chrome.get(whastAppLink + '55' + '1143316160' + '&text=' + codedMassege)
        time.sleep(3)
        beginChat = chrome.find_element(By.XPATH, '//*[@id="action-button"]/span')
        beginChat.click()
        time.sleep(3)
        useWebWhatsApp = chrome.find_element(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a/span')
        useWebWhatsApp.click()
        time.sleep(10)
        sendButton = chrome.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        sendButton.click()
        time.sleep(5)
        codedMassege = ''



def createMassege():
    massegeList = []
    inputType = ''
    finalizado = False
    textFinalizado = 'False'
    os.system('cls')
    while (finalizado != True):
        print('As mensagens são escritas por etapas, essas etapas são definidas toda vez que precisamos inserir uma variável, como por exemplo o nome do candidato ou o curso. \n\nExemplo: \n1-Olá \n2-$candidato, \n3-você passou no processo seletivo para o cusro de \n4-$curso \n\nPara adicionar uma etapa podemos escolher entre as 6 opções abaixo, se escolhermos texto devemos escrever nossa mensagem e se escolhermos uma variável ela se concatenada.')
        print('\nAs variáveis disponíveis são: \n\n1 - Texto: escrever mensagem \n2 - Nome: candidateList[index].name \n3 - Curso: candidateList[index].course \n4 - Email: candidateList[index].email \n5 - DDD: candidateList[index].ddd \n6 - Número: candidateList[index].celNumber')
        
        print('\nEscolher nova adição (de 1 a 6):')
        inputType = input()
        if(inputType == '1'):
            print('Escreva seu texto:')
            massege = input()
            massegeList.append(massege.replace(' ', '%20'))
        if(inputType == '2'):
            massegeList.append('candidateList[index].name')            
        if(inputType == '3'):
            massegeList.append('candidateList[index].course')
        if(inputType == '4'):
            massegeList.append('candidateList[index].email')
        if(inputType == '5'):
            massegeList.append('candidateList[index].ddd')
        if(inputType == '6'):
            massegeList.append('candidateList[index].celNumber')


        print("\nMensagem finalizada? Para finalizar escreva True e para continuar escreva de enter")
        textFinalizado = input()
        if (textFinalizado == 'True'):            
            finalizado = True
        else: 
            os.system('cls')
            finalizado = False
    print(massegeList)
    return massegeList

createAndPopulateCandidateinstacies(candidateList)
correctCelNumber(candidateList)
massege = createMassege()
openBrowserAndSendMessage(candidateList, massege)

