from src.view.cli import createMessage
from src.service.service import createAndPopulateCandidateinstacies, correctCelNumber
from src.automation.webAutomation import openBrowserAndSendMessage

candidateList = []

createAndPopulateCandidateinstacies(candidateList)
correctCelNumber(candidateList)
Message = createMessage()
openBrowserAndSendMessage(candidateList, Message)

