# 18. Crie um programa que imprima a tabuada de um número informado pelo usuário.
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")