def resultado( rv, r):
    if r == 'X' and rv == 'A':
        result = 3
    elif r == 'X' and rv == 'B':
        result = 1
    elif r == 'X' and rv == 'C':
        result = 2
    elif r == 'Y' and rv == 'A':
        result = 1
    elif r == 'Y' and rv == 'B':
        result = 2
    elif r == 'Y' and rv == 'C':
        result = 3
    elif r == 'Z' and rv == 'A':
        result = 2
    elif r == 'Z' and rv == 'B':
         result = 3
    elif r == 'Z' and rv == 'C':
        result = 1
    return result

def puntuacion(rival , respuesta):
    punto = 0
    if respuesta == 'X':#Perder
            punto = 0
    elif respuesta == 'Y':#Empate
            punto = 3
    elif respuesta == 'Z':#Ganar
            punto = 6
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

