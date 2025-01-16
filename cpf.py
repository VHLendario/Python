def cpf ():
    dados = [['Nome', 'Idade', 'CPF'], ['Nome', 'Idade', 'CPF']]
    for lin in range (len(dados)):
        for col in range (len(dados[lin])):
            if col == 0:
                dados [lin] [col] = input ("Digite seu nome: ")
            elif col == 1:
                dados [lin] [col] = input ("Digite sua idade: ")
            else:
                dados [lin] [col] = input ("Digite seu CPF: ")     
    
    arq = open ('loja.txt', 'w')
    print ('-----------------------', file = arq)
    print ('|Nome\t|Idade\t|CPF\t\t|', file=arq)
    arq.close ()
    arq = open ('loja.txt', 'a')
    for lin in range (len(dados)):
        for col in range (len(dados[lin])):
            print ('|', end = '', file = arq)
            print (dados[lin] [col], end = '\t', file=arq)
        print ('|', file = arq)
    
    print ('-----------------------', file= arq)
    arq.close()

cpf ()