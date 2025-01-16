def Conversor ():
    letra = input ("Digite qualquer letra: ")
    valor_DECIMAL = ord (letra)
    valor_HEXADECIMAL = hex(valor_DECIMAL)
    valor_BINARIO = bin (valor_DECIMAL)

    print ("A letra digitada foi: ", letra)
    print (f"A sua letra em decimal é: {valor_DECIMAL}")
    print (f"Sua letra em hexadecimal: {valor_HEXADECIMAL}")
    print (f"Sua letra em binário: {valor_BINARIO}")
    
    return
Conversor ()