# Matriz mal condicionada A (3x3)
A_bad = np.array([[1, 1, 1],
                  [1, 1.0001, 1],
                  [1, 1, 1.0002]])

# Vector b correspondiente
b_bad = np.array([3, 3.0001, 3.0002])

# Calcular el número de condición de la matriz mal condicionada
cond_num_bad = np.linalg.cond(A_bad)

# Crear un rango de valores para x1, x2, y x3
x_vals = np.linspace(-10, 10, 400)

# Graficar las superficies correspondientes a las ecuaciones del sistema mal condicionado
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear las funciones para las ecuaciones
X1, X2 = np.meshgrid(x_vals, x_vals)
Z1 = (b_bad[0] - A_bad[0][0]*X1 - A_bad[0][1]*X2) / A_bad[0][2]
Z2 = (b_bad[1] - A_bad[1][0]*X1 - A_bad[1][1]*X2) / A_bad[1][2]
Z3 = (b_bad[2] - A_bad[2][0]*X1 - A_bad[2][1]*X2) / A_bad[2][2]

# Graficar las tres superficies
ax.plot_surface(X1, X2, Z1, color='r', alpha=0.6, label="Eq1")
ax.plot_surface(X1, X2, Z2, color='g', alpha=0.6, label="Eq2")
ax.plot_surface(X1, X2, Z3, color='b', alpha=0.6, label="Eq3")

# Añadir etiquetas
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')
plt.title(f'Gráfico de sistema mal condicionado\nNúmero de condición: {cond_num_bad:.2f}')

plt.show(), cond_num_bad


# Resumen del análisis de la matriz mal condicionada
det_A_bad = np.linalg.det(A_bad)  # Determinante de la matriz mal condicionada
cond_num_bad = np.linalg.cond(A_bad)  # Número de condición de la matriz

# Resolver el sistema de ecuaciones original
x_original = np.linalg.solve(A_bad, b_bad)

# Hacer un pequeño cambio en el vector b
b_modified = np.array([3, 3.0002, 3.0004])  # Cambio pequeño en el vector b
x_modified = np.linalg.solve(A_bad, b_modified)  # Nueva solución con b modificado

# Matriz identidad correspondiente para referencia
I = np.identity(3)

det_A_bad, cond_num_bad, x_original, x_modified, I
