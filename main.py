from src.view.cli import createMessage
from src.service.service import createAndPopulateCandidateinstacies, correctCelNumber
from src.automation.webAutomation import openBrowserAndSendMessage
from src.store.store import candidateList


createAndPopulateCandidateinstacies(candidateList)
correctCelNumber(candidateList)
Message = createMessage()
openBrowserAndSendMessage(candidateList, Message)

