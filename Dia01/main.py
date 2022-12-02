def mayorCaloria():
    file = open("entrada.txt")
    actual = 0
    suma = 0
    arr = []
    while True:
        linea = file.readline()
        if not linea == '\n' and linea:
            suma = suma + int(linea)
        elif linea == '\n':
            arr.append(suma)
            suma = 0
        if not linea:
             break;
    arr.sort(reverse=True)
    print(arr[0]+arr[1]+arr[2])

mayorCaloria()