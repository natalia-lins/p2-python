# 9. Converta uma lista de strings numéricas para uma lista de inteiros.
lista = ["1", "2", "3", "4", "5"]
novaLista = [int(numero) for numero in lista]

print(f"Lista de inteiros: {novaLista} | Tipo de dado armazenado: {type(novaLista[0])}")