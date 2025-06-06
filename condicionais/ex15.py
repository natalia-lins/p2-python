# 15. Crie um programa que simule um caixa eletrônico, verificando se o saldo é
# suficiente para um saque.
saldo = 1000.00
saque = float(input("Digite o valor que deseja sacar: "))

if saque <= saldo:
    saldo -= saque
    print(f"Saque realizado! Saldo atual R${saldo:.2f}")
else:
    print(f"ERRO! Saldo insuficiente para o valor que deseja sacar (Saldo atual: R${saldo:.2f})")