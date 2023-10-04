def buscarCadenaAdyacenteMasLarga():
    longitudMaxima = 0
    carater = None
    
    def controlarEnDireccion(x, y, dx, dy):
        #Buscar en una direccion determinada.
        nonlocal longitudMaxima
        char = matriz[x][y]
        count = 0
        while 0 <= x < len(matriz) and 0 <= y < len(matriz[0]) and matriz[x][y] == char:
            count += 1
            x += dx
            y += dy
            # Detener el recorrido si no hay suficientes elementos para superar el maximo.
            if count + max(len(matriz[0]) - x, len(matriz[0]) - y) <= longitudMaxima:                   
                return count            
        return count

    def buscarMaximaLongitud():
        #Buscar la cadena mas larga.
        nonlocal longitudMaxima, carater
        for x in range(len(matriz)):
                #Detener el recorrido si se encuentra una cadena de longitud maxima igual que la longitud 
                # de la matriz. Esto hace que si hay otro con la misma longitud, lo va a ignorar, solo en el caso
                # del máximo permitido.
                if longitudMaxima >= len(matriz[0]):                   
                    break
                for y in range(len(matriz[0])):
                    # Detener el recorrido si no hay suficientes elementos para superar el maximo.
                    if longitudMaxima >= max(len(matriz[0]) - x, len(matriz[0]) - y):                   
                        break             
                    for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                        length = controlarEnDireccion(x, y, dx, dy)
                        if length > longitudMaxima:
                            longitudMaxima = length
                            carater = matriz[x][y]
                        # Detener el recorrido si no hay suficientes elementos para superar el maximo.
                        if longitudMaxima >= max(len(matriz[0]) - x, len(matriz[0]) - y):                   
                            break                                                
        return carater * longitudMaxima
    result = buscarMaximaLongitud()
    return result

# Leer la matriz desde un archivo de texto
with open('matriz.txt', 'r') as file:
    lines = file.readlines()

matriz = [list(line.strip().split(', ')) for line in lines]

result = buscarCadenaAdyacenteMasLarga()
print(result)
