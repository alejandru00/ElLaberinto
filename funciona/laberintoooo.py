
laberinto = [
    ['E', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        for celda in fila:
            print(celda, end=' ')
        print()

############################################################################################################

def buscar_entrada(laberinto):                         #Ubicamos la entrada en coordenadas
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'E':
                return (fila, columna)

def buscar_salida(laberinto):                          #Ubicamos la salida en coordenadas  
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'S':
                return (fila, columna)

def buscar_camino(laberinto, entrada, salida):
    while True:                                       #Definimos cuando estamos siguiendo bien el camino y cuando no
        if entrada == salida:                                   #Si la entrada esta en la salida, seguimos (aun que ya habriamos termianado)
            return True
        if entrada in muro:                                     #Si la entrada esta en la lista de muros, no es posible seguir
            return False
        if entrada[0] < 0 or entrada[0] >= len(laberinto):      #Si esta fuera de los límites del laberinto, no es posible seguir tampoco   
            return False
        if entrada[1] < 0 or entrada[1] >= len(laberinto[0]):
            return False
        if laberinto[entrada[0]][entrada[1]] == 'o':
            return False
        laberinto[entrada[0]][entrada[1]] = 'o'                #Se printea "o" por el camin0 tomado

        if buscar_camino(laberinto, (entrada[0] + 1, entrada[1]), salida):          #Si hay un muro a los lados y arriba va hacia abajo
            print('Abajo')
            return True
        if buscar_camino(laberinto, (entrada[0] - 1, entrada[1]), salida):          #Si hay un muro abajo y a los lados va arriba
            print('Arriba') 
            return True
        if buscar_camino(laberinto, (entrada[0], entrada[1] + 1), salida):          #Si tiene muros por arriba, abajo y a la izquiera va a la derecha
            print('Derecha')
            return True
        if buscar_camino(laberinto, (entrada[0], entrada[1] - 1), salida):          #Si tiene muros por arriba, abajo y a la derecha va a la ixquierda
            print('Izquierda')
            return True
        return False

def main():                                         #Printea todo
    print()
    imprimir_laberinto(laberinto)
    entrada = buscar_entrada(laberinto)
    salida = buscar_salida(laberinto)
    print("\n")
    print("El camino a seguir para salir del laberionto es hacia...:")
    if buscar_camino(laberinto, entrada, salida):
        print("Y... ¡¡Hemos encontrado el camino!! \n")
    else:
        print("No hemos encontrado el camino...")
    imprimir_laberinto(laberinto)                   #Printea el laberinto con las "o" en el camiino a tomar    

if __name__ == '__main__':
    main()