# 19. Crie um programa que divida dois números fornecidos pelo usuário, tratando a
# divisão por zero.

try:
    n1 = float(input("Digite um número número: "))
    n2 = float(input("Digite outro número: "))
    resultado = n1 / n2
    print(f"Resultado: {resultado:.2f}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")