def media (a, b):
    return (a + b) / 2
    
def calculo ():
    c = float (input("Digite a primeira nota do aluno: "))
    d = float (input ("Digite a segunda nota do aluno: "))
    resultado = media (c, d)
    return resultado
    
def Start ():
    print ("Bem vindo professor!")
    contador = 0
    aprovados = []
    reprovados = []

    while contador < 30:
        nome = input("Digite o nome do aluno: ")
        resultado = calculo ()
        if resultado >= 7:
            print (f"O aluno {nome} com média {resultado} está aprovado.")
            aprovados.append ((nome, resultado))
        else:
            print (f"O aluno {nome} com média {resultado} está em exame.")
            reprovados.append ((nome, resultado))
        contador += 1

    print ("\nA lista de alunos aprovados: ")
    for nome, resultado in aprovados:
        print(f"{nome} - Média: {resultado}")

    print ("\nA lista de alunos reprovados: ")
    for nome, resultado in reprovados:
        print (f"{nome} - Média: {resultado}")
    return 

Start ()