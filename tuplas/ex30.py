# 30. Implemente uma função que receba uma tupla de strings e retorne uma nova
# tupla com o comprimento de cada string.

def contaTamanho(tupla_strings):
    return tuple(len(s) for s in tupla_strings)

tup = ("natalia", "nathan", "leonardo")
print(f"Comprimento das strings: {contaTamanho(tup)}")