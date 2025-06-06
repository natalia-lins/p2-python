# 13. Crie um programa que verifique se um número é positivo, negativo ou zero.
num = float(input("Digite um número: "))

if num > 0:
    print(f"O número {num} é positivo.")
elif num < 0:
    print(f"O número {num} é negativo.")
else:
    print("O número é zero.")