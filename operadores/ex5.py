# Crie um programa que calcule o IMC (Índice de Massa Corporal) usando a
# fórmula: IMC = peso / (altura²).

peso, altura = 70, 1.70

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")