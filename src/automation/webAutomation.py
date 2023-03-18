
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def openBrowserAndSendMessage(candidateList, Message):
    codedMessage = ''
    whastAppLink = 'https://api.whatsapp.com/send?phone='
    chrome = webdriver.Chrome()
    chrome.get('https://web.whatsapp.com/')
    time.sleep(15)
    for indexCandidate in range(len(candidateList)):
        for index in range(len(Message)):
            if(Message[index] == 'candidateList[index].name'):
                codedMessage = codedMessage + candidateList[indexCandidate].name

            elif(Message[index] == 'candidateList[index].course'):
                codedMessage = codedMessage + candidateList[indexCandidate].course

            elif(Message[index] == 'candidateList[index].email'):
                codedMessage = codedMessage + candidateList[indexCandidate].email
    
            elif(Message[index] == 'candidateList[index].ddd'):
                codedMessage = codedMessage + candidateList[indexCandidate].ddd

            elif(Message[index] == 'candidateList[index].celNumber'):
                codedMessage = codedMessage + candidateList[indexCandidate].celNumber

            else:
                codedMessage = codedMessage + Message[index]
            
        print(codedMessage)
        chrome.get(whastAppLink + '55' + str(candidateList[indexCandidate].ddd) + str(candidateList[indexCandidate].celNumber) + '&text=' + codedMessage)
        print(whastAppLink + '55' + str(candidateList[indexCandidate].celNumber) + '&text=' + codedMessage)
        time.sleep(3)
        beginChat = chrome.find_element(By.XPATH, '//*[@id="action-button"]/span')
        beginChat.click()
        time.sleep(3)
        useWebWhatsApp = chrome.find_element(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a/span')
        useWebWhatsApp.click()
        time.sleep(10)
        try:
            sendButton = chrome.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            sendButton.click()
        except:
            time.sleep(5)
            codedMessage = ''