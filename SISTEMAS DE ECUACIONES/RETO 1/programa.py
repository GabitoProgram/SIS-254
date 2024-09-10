import numpy as np

# Coeficientes de las ecuaciones
A = np.array([
    [0.52, 0.20, 0.25],  # Coeficientes de la ecuación de la arena
    [0.30, 0.50, 0.20],  # Coeficientes de la ecuación del grano fino
    [0.18, 0.30, 0.55]   # Coeficientes de la ecuación del grano grueso
])

# Vector de términos independientes
b = np.array([480, 5810, 5690])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)

# Mostrar resultados
print(f'Cantidad de metros cúbicos de la cantera 1: {x[0]:.2f}')
print(f'Cantidad de metros cúbicos de la cantera 2: {x[1]:.2f}')
print(f'Cantidad de metros cúbicos de la cantera 3: {x[2]:.2f}')