# 28. Crie uma função que receba uma lista de tuplas contendo nome e idade de
# pessoas, e retorne a pessoa mais velha.
def encontrarMaisVelho(lista):
    return max(lista, key=lambda pessoa: pessoa[1])

listaPessoas = [("Fernanda", 44), ("Daniel", 40), ("Nathan", 4), ("Natalia", 19)]
print(f"Pessoa mais velha: {encontrarMaisVelho(listaPessoas)}")