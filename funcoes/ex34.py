# 34. Crie uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Digite um número: "))
print(f"{n}º termo da sequência de Fibonacci:", fibonacci(n))