# 31. Crie uma função que use range() para gerar uma lista de números pares entre 0 e n.
def listarPares(n):
    return list(range(0, n + 1, 2))

num = int(input("Digite um número: "))
print(f"Números pares até {num}:", listarPares(num))