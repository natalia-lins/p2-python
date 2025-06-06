# 35. Escreva uma função lambda que receba dois números e retorne o maior deles.
escolherMaior = lambda a, b: a if a > b else b

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(f"O maior número entre {n1} e {n2} é: {escolherMaior(n1,n2)}")