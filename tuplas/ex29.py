# 29. Escreva um programa que converta uma lista de coordenadas (x, y)
# em uma tupla contendo as médias de x e y.

coordenadas = [(2, 4), (5, 9), (8, 3), (7,1)]
somaX = sum(coord[0] for coord in coordenadas)
somaY = sum(coord[1] for coord in coordenadas)
qnt = len(coordenadas)
media= (somaX/qnt, somaY/qnt)

print(f"Média das coordenadas (x,y): {media}")