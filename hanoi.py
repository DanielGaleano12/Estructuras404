def hanoi(n, origen, auxiliar, destino):
    if n == 1:  # Caso base
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        # Paso 1: mover n-1 discos al auxiliar
        hanoi(n - 1, origen, destino, auxiliar)
        
        # Paso 2: mover el disco grande
        print(f"Mover disco {n} de {origen} a {destino}")
        
        # Paso 3: mover los n-1 discos al destino
        hanoi(n - 1, auxiliar, origen, destino)


# Número de discos
hanoi(3, "A", "B", "C")