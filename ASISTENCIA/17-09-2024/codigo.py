import numpy as np

# Coeficientes del sistema de ecuaciones
A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

# Términos independientes
b = np.array([7.85, -19.3, 71.4])

# Tolerancia y número máximo de iteraciones
tolerance = 1e-10
max_iterations = 1000

# Valores iniciales de las incógnitas
x = np.zeros_like(b)

# Método de Gauss-Seidel
def gauss_seidel(A, b, x, tolerance, max_iterations):
    n = len(b)
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        
        for i in range(n):
            sum_Ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_Ax) / A[i][i]
        
        # Comprobación de la convergencia
        if np.allclose(x, x_new, atol=tolerance, rtol=0):
            print(f"Convergencia alcanzada después de {iteration + 1} iteraciones.")
            return x_new
        
        x = x_new
    
    print("No se alcanzó la convergencia dentro del número máximo de iteraciones.")
    return x

# Resolver el sistema
solution = gauss_seidel(A, b, x, tolerance, max_iterations)

# Mostrar la solución
print(f"Solución aproximada: x1 = {solution[0]}, x2 = {solution[1]}, x3 = {solution[2]}")
