# 21. Crie um programa que abra um arquivo para leitura e trate o erro
# caso o arquivo não exista.

arq = "NataliaRamirez.txt"

try:
    with open(arq, "r") as arquivo:
        cont = arquivo.read()
        print("Conteúdo do arquivo:")
        print(cont)
except FileNotFoundError:
    print(f"ERRO: o arquivo '{arq}' não foi encontrado.")