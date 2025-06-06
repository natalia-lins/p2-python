# 24. Crie um programa que substitua todas as ocorrências de uma letra por outra em uma string.

texto = input("Digite uma frase: ").lower()
antigo = input("Digite o caracter que deseja substituir: ")
novo = input("Digite o novo caracter: ")

substituido = texto.replace(antigo, novo)
print(f"Frase original: {texto}\nFrase com substituição: {substituido}")