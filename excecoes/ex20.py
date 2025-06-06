# 20. Escreva um programa que tente converter uma string para inteiro,
# tratando o erro caso a string não seja um número.
texto = input("Digite um número inteiro: ")

try:
    num = int(texto)
    print(f"Número digitado: {num}.")
except ValueError:
    print("ERRO: você digitou um texto, não um número inteiro.")