import os

def createMessage():
    messageList = []
    messageListPlaceholder = []
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
            message = input()
            messageListPlaceholder.append(message)
            messageList.append(message.replace(' ', '%20'))
        if(inputType == '2'):
            messageListPlaceholder.append('nome candidato')
            messageList.append('candidateList[index].name')            
        if(inputType == '3'):
            messageListPlaceholder.append('Nome do Curso')
            messageList.append('candidateList[index].course')
        if(inputType == '4'):
            messageListPlaceholder.append('email candidato')
            messageList.append('candidateList[index].email')
        if(inputType == '5'):
            messageListPlaceholder.append('ddd do candidato')
            messageList.append('candidateList[index].ddd')
        if(inputType == '6'):
            messageListPlaceholder.append('celular do candidato')
            messageList.append('candidateList[index].celNumber')

        if messageListPlaceholder != None:
            print('\nSua mensagem atual é a concatenação do seguintes itens: \n', messageListPlaceholder)

        print("\nMensagem finalizada? Para finalizar escreva Finalizado e para continuar pressione enter\n")

        textFinalizado = input()
        if (textFinalizado == 'Finalizado'):            
            finalizado = True
        else: 
            os.system('cls')
            finalizado = False
    print(messageList)
    return messageList