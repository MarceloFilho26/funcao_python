from biblioteca import estoque
produto = input("Informe o nome do produto: ")
quantidade = int(input("Informe a quantidade do produto: "))
valor = float(input("Informe o valor unitário: "))

T = estoque(produto, quantidade, valor)
print(T)

#Programa que recebe nome do produto, a quantidade e o valor. Após isso retornar o valor total do estoque.
#A função está na biblioteca
