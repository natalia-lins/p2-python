# 11. Escreva um programa que peça dois números e imprima a soma, subtração,
# multiplicação e divisão entre eles.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2

print(f"===== Operações =====\nSoma: {soma:.2f}\nSubtração: {sub:.2f}\nMultiplicação: {mult:.2f}\nDivisão: {div:.2f}")

