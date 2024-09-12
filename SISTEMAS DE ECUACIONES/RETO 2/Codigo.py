import numpy as np

# Definimos la matriz A y el vector b
A = np.array([
    [0, -2, -6],
    [1, 0, -1],
    [8, 5, 0]
])

b = np.array([-8, -2, 13])

def es_diagonal_dominante(A):
    n = A.shape[0]
    for i in range(n):
        # Calculamos el valor absoluto del elemento en la diagonal
        diagonal = abs(A[i, i])
        
        # Sumamos el valor absoluto de los demás elementos de la fila
        suma_otros = sum(abs(A[i, j]) for j in range(n) if j != i)
        
        print(f"Fila {i+1}: |A[{i},{i}]| = {diagonal}, Suma de otros elementos = {suma_otros}")
        
        # Verificamos la condición de diagonal dominante
        if diagonal <= suma_otros:
            print("La matriz NO es diagonalmente dominante.")
            return False
        
    print("La matriz es diagonalmente dominante.")
    return True

# Llamamos a la función para verificar si la matriz es diagonalmente dominante
es_diagonal_dominante(A)