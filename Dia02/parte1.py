def resultado( rv, r):
    result = 0
    if r == 'X' and rv == 'A':
        result = 3
    elif r == 'X' and rv == 'B':
        result = 0
    elif r == 'X' and rv == 'C':
        result = 6
    elif r == 'Y' and rv == 'A':
        result = 6
    elif r == 'Y' and rv == 'B':
        result = 3
    elif r == 'Y' and rv == 'C':
        result = 0
    elif r == 'Z' and rv == 'A':
        result = 0
    elif r == 'Z' and rv == 'B':
         result = 6
    elif r == 'Z' and rv == 'C':
        result = 3
    return result

def puntuacion(rival , respuesta):
    punto = 0
    if respuesta == 'X':
            punto = 1
    elif respuesta == 'Y':
            punto = 2
    elif respuesta == 'Z':
            punto = 3
    return punto + resultado(rival,respuesta)

def leelinea():
    file = open("entrada.txt")
    puntos = 0
    while True:
        linea = file.readline()
        if linea:
         puntos = puntos + puntuacion(linea[0],linea[2])
        if not linea:
             break;
    print (puntos)

leelinea()

