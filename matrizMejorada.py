def buscarCadenaAdyacenteMasLarga():
    longitudMaxima = 1
    caracter = matriz[0][0]
    longitud = len(matriz[0])
    cantidadCaracteresLinea = longitud - 1
    def controlarEnDireccion(x, y, dx, dy):
        #Buscar en una direccion determinada.
        nonlocal longitudMaxima, longitud, caracter
        char = matriz[x][y]
        count = 1
        x += dx
        y += dy
        while 0 <= x < longitud and 0 <= y < longitud:
            if(matriz[x][y] == char):
                count += 1
            else:
                count = 1
                char = matriz[x][y]
            x += dx
            y += dy 
            if count > longitudMaxima:
                longitudMaxima = count
                caracter = char
        return count

    def controlar(x, y, direcciones):
        nonlocal longitudMaxima, longitud, cantidadCaracteresLinea
        for dx, dy in direcciones:
            ## Detener el recorrido si no hay suficientes elementos para superar el maximo.
            if longitudMaxima >= max(longitud - x, longitud - y):                   
               break
            length = controlarEnDireccion(x, y, dx, dy)
            #aca

    def buscarMaximaLongitud():
        #Buscar la cadena mas larga.
        nonlocal longitudMaxima, cantidadCaracteresLinea
        #Buscar para abajo, en diagonal para abajo y para la derecha de la esquina 0,0
        controlar(0, 0, [(0, 1), (1, 0), (1, 1)])
        #Buscar en diagonal para arriba, en diagonal para abajo y para la derecha de todas las filas
        for x in range(1,longitud):
            controlar(x, 0, [(0, 1), (1, 1), (-1, 1)])
        #Buscar para abajo y en diagonal para abajo de todas las columnas
        for y in range(1,cantidadCaracteresLinea):
            controlar(0, y, [(1, 0), (1, 1)])
        #Buscar para abajo la esquina 0,longitud
        controlar(0, cantidadCaracteresLinea, [(1, 0)])
        #Buscar en la ultima columna, solo en diagonal para abajo
        for y in range(1,cantidadCaracteresLinea):
            controlar(cantidadCaracteresLinea, y, [(-1, 1)]) 
        return caracter * longitudMaxima
    result = buscarMaximaLongitud()
    return result

# Leer la matriz desde un archivo de texto
with open('matriz.txt', 'r') as file:
    lines = file.readlines()

matriz = [list(line.strip().split(', ')) for line in lines]
            
result = buscarCadenaAdyacenteMasLarga()

print(result)
