# 26. Escreva um programa que remova todos os elementos duplicados de uma lista.
lista = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
novaLista = list(set(lista))

print(f"Lista original: {lista}\nLista ajustada: {novaLista}")