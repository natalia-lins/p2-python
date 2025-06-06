# 27. Implemente uma função que receba duas listas e retorne uma nova lista
# contendo apenas os elementos comuns entre elas.

def retornarComum(l1, l2):
    return list(set(l1) & set(l2))

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [10, 9, 8, 7, 6, 5]

print(f"Lista 1: {l1}\nLista 2: {l2}\nNúmeros em comum: {retornarComum(l1,l2)}")