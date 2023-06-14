def calcular_distancias(retangulo):
    coordenadas_x = [ponto[0] for ponto in retangulo]
    coordenadas_y = [ponto[1] for ponto in retangulo]
    distancia_x = max(coordenadas_x) - min(coordenadas_x)
    distancia_y = max(coordenadas_y) - min(coordenadas_y)
    return distancia_x, distancia_y


# Exemplo de uso
retangulo = [[200, 300], [100, 300], [100, 100], [200, 100]]
distancia_x, distancia_y = calcular_distancias(retangulo)
print("Distância em relação à linha X:", distancia_x)
print("Distância em relação à linha Y:", distancia_y)
