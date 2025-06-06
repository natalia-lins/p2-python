# 17. Escreva um programa que calcule a soma dos números de 1 a N,
# onde N é informado pelo usuário.
n = int(input("Digite um número N: "))
soma = 0

for i in range(1, n + 1):
    soma += i

print(f"A soma dos números de 1 até {n} é {soma}.")