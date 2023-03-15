from CandidateClass import Candidate
import openpyxl

from openpyxl import Workbook, load_workbook

book = load_workbook('data_source.xlsx')

sheet = book.active
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

        print('Candidato: \n' + candidateList[currentCell].name + '\n' + candidateList[currentCell].course + '\n' + candidateList[currentCell].email + '\n' + str(candidateList[currentCell].ddd) + '\n' + str(candidateList[currentCell].celNumber) + '\n' + '-------------//-------------')
    

createAndPopulateCandidateinstacies(candidateList)
correctCelNumber(candidateList)

