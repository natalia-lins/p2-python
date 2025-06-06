# 36. Implemente uma função que receba uma lista e uma função como parâmetros,
# e aplique a função a cada elemento da lista.

def aplicarFuncao(lista, funcao):
    return [funcao(x) for x in lista]

nomes = ["natalia", "leonardo", "nathan"]
resultado = aplicarFuncao(nomes, lambda nome: nome.upper())
print("Nomes em maiúsculo:", resultado)
