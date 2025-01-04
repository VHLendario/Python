
def somar (a, b):
    return a + b
def subtrair (a, b):
    return a - b
def multiplicar (a, b):
    return a * b
def dividir (a, b):
    if b != 0:
        return a / b
    else:
        print ("O valor inserido é inválido.")

def Add ():
    c = float(input ("Digite um numero: "))
    d = float(input ("Digite outro numero: "))
    resultado = somar (c, d)
    print (f"A sua soma deu: {resultado}")
def Sub ():
    c = float(input ("Digite um numero: "))
    d = float(input ("Digite outro numero: "))
    resultado = subtrair (c, d)
    print (f"A sua subtração deu: {resultado}")
def Mult ():
    c = float(input ("Digite um numero: "))
    d = float(input ("Digite outro numero: "))
    resultado = multiplicar (c, d)
    print (f"A sua multiplicação deu: {resultado}")
def Div ():
    c = float(input ("Digite um numero: "))
    d = float(input ("Digite outro numero: "))
    resultado = dividir (c, d)
    print (f"A sua divisão deu: {resultado}")
    

def Calculadora ():
    print ("Bem-vindo à calculadora, observe as operações que você pode realizar:")
    print ("A) Soma")
    print ("B) Subtração")
    print ("C) Multiplicação")
    print ("D) Divisão")

    escolha = input ("Digite sua escolha: ")

    if escolha == "a" or escolha == "A":
        Add ()
        
        print ("Escolha sua próxima ação:")
        print ("A) Voltar para o menu.")
        print ("B) Somar novamente.")
        print ("C) Encerrar.\n")
        escolha_02 = input ("Digite sua escolha: ")

        if escolha_02 == "A" or escolha_02 == "a":
            Calculadora ()
        elif escolha_02 == "B" or escolha_02 == "b":
            Add ()
        else:
            return 
    
    elif escolha == "b" or escolha == "B":
        Sub ()

        print ("Escolha sua próxima ação:")
        print ("A) Voltar para o menu.")
        print ("B) Subtrair novamente.")
        print ("C) Encerrar.\n")
        escolha_02 = input ("Digite sua escolha: ")

        if escolha_02 == "A" or escolha_02 == "a":
            Calculadora ()
        elif escolha_02 == "B" or escolha_02 == "b":
            Sub ()
        else:
            return 

    elif escolha == "c" or escolha == "C":
        Mult ()

        print ("Escolha sua próxima ação:")
        print ("A) Voltar para o menu.")
        print ("B) Multiplicar novamente.")
        print ("C) Encerrar.\n")
        escolha_02 = input ("Digite sua escolha: ")

        if escolha_02 == "A" or escolha_02 == "a":
            Calculadora ()
        elif escolha_02 == "B" or escolha_02 == "b":
            Mult ()
        else:
            return 
    
    elif escolha == "d" or escolha == "D":
        Div ()

        print ("Escolha sua próxima ação:")
        print ("A) Voltar para o menu.")
        print ("B) Dividir novamente.")
        print ("C) Encerrar.\n")
        escolha_02 = input ("Digite sua escolha: ")

        if escolha_02 == "A" or escolha_02 == "a":
            Calculadora ()
        elif escolha_02 == "B" or escolha_02 == "b":
            Div ()
        else:
            return 

Calculadora ()