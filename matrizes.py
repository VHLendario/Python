def Teste_Alpha ():
    exemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for lin in range (len(exemplo)):
        for col in range (len(exemplo[lin])):
            print (exemplo[lin] [col], end = '\t')
        print()  

        números = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14 ,15]]
    print (números[0:3])
def Teste_01():
    for lin in range(len(mtz)):
        for col in range (len(mtz[lin])):
            if col == 0:
                mtz [lin] [col] = input ("Digite seu nome: ")
            elif col == 1:
                mtz [lin] [col] = input ("Digite seu telefone: ")
            else:
                mtz [lin] [col] = input ("Digite seu sexo: ")
        
    print (mtz) 
def Teste_02 ():  
    matriz_teste = [['a00', 'a01', 'a02'], ['a10', 'a11', 'a12'], ['a20', 'a21', 'a22']]
    elementos = [0, 0, 0]

    for lin in range (len(matriz_teste)):
        for col in range (len(matriz_teste)):
            if lin == col:
                elementos [lin] = matriz_teste [lin] [col]

    print ("Diagonal principal: ")
    print (elementos)
def Teste_BETA ():
    mtz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diag_princ = [0, 0, 0]
    diag_secun = [0, 0, 0]

    for lin in range (len(mtz)):
        for col in range (len(mtz[lin])):
            if lin == col:
                diag_princ [lin] = mtz [lin] [col]
            if lin + col == len(mtz) -1:
                diag_secun [lin] = mtz [lin] [col]
    print ("A diagonal principal é: \n", diag_princ)
    print ("A diagonal secundária é: \n", diag_secun)
