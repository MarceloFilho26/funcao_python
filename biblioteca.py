def soma(num1, num2):
    resp = num1 + num2
    print(resp)

def subtracao(num1, num2):
    resp = num1 - num2
    print(resp)


def divisao(num1, num2):
    resp = (num1 / num2)
    print(resp)


def multiplicacao(num1, num2):
    resp = num1 * num2
    print(resp)


def repeat(n):
    for x in range(1, n+ 1):
        print(str(x) * x)

def repeat1(n):
    for x in range(n + 1):
        for y in range(1, x + 1):
            print(y, end = " ")
        print()

def cont_vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"O total de vogais é: {cont}")

def estoque(produto, quantidade, valor):
   vTotal = quantidade * valor
   return vTotal

def argumento(num1):
    if num1 == 0:
        return "Z"
    else:
        if num1 > 0:
            return "P"
        else:
            return "N"
