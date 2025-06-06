# 22. Crie um programa que conte quantas vezes uma determinada letra aparece em uma string.

frase = input("Digite uma frase: ")
letra = input("Digite o caracter que deseja contar: ")

qnt = frase.count(letra)
print(f"Frase: {frase}\nLetra escolhida: {letra} | Quantidade repetida: {qnt}")