# 32. Escreva uma função que use range() para calcular a soma dos primeiros n números naturais.
def somar(n):
    return sum(range(1, n + 1))

num = int(input("Digite um número: "))
print(f"Soma dos primeiros {num} números naturais:", somar(num))