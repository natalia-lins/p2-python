# 23. Escreva um programa que verifique se uma palavra é um palíndromo
# (lê-se igual de trás para frente).

palavra = input("Digite uma palavra: ").lower()

if palavra == palavra[::-1]:
    print(f"A palavra escolhida ({palavra}) é um palíndromo.")
else:
    print(f"A palavra escolhida ({palavra}) não é um palíndromo.")