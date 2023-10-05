from biblioteca import *
resp = "S"
while resp == "S" or resp == "s":
    print("|Bem-vindo a calculadora: 1 - soma ; 2 - subtração ; 3 - divisão ; 4 - multiplicação")
    opcao = input("Informe a opção desejada: ")
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
        opcao = input("Opção inválida, digite novamente: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o primeiro número: "))
    if opcao == "1":
        soma(num1, num2)
    elif opcao == "2":
        subtracao(num1, num2)
    elif opcao == "3":
        divisao(num1, num2)
    elif opcao == "4":
        multiplicacao(num1, num2)
    resp = input("Deseja fazer novamente? [S/N]: ")
    while (resp != "S" and resp != "s") and (resp != "N" and resp != "n"):
        resp = input("Opçõa inválida, tente novamente: ")
print("Programa encerrado!")

#Calcudora em Py com menu integrado.
#A função está na biblioteca.