
def findTheCenter(forma_geometrica):
    # Inicializar as somas das coordenadas x e y
    soma_x = 0
    soma_y = 0

    # Calcular a soma das coordenadas x e y
    for ponto in forma_geometrica:
        soma_x += ponto[0]
        soma_y += ponto[1]

    # Calcular o centro
    centro_x = soma_x / len(forma_geometrica)
    centro_y = soma_y / len(forma_geometrica)

    return centro_x, centro_y


print(findTheCenter([[74, 218], [282, 212], [284, 258], [76, 264]]))
