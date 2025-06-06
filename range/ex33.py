# 33. Implemente uma função que use range() para criar uma lista de potências de 2 até um determinado expoente.
def potencias(expoente):
    return [2 ** i for i in range(expoente + 1)]

num = int(input("Digite um número: "))
print(f"Potências de 2 até o expoente {num}:", potencias(num))