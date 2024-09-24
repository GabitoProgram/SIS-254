import matplotlib.pyplot as plt
import numpy as np

# Coeficientes de las ecuaciones
A1 = [1.0001, 1.0000]  # Coeficientes de la primera ecuación
A2 = [1.0000, 1.0000]  # Coeficientes de la segunda ecuación
b1 = 2  # Término independiente de la primera ecuación
b2 = 2  # Término independiente de la segunda ecuación

# Crear un rango de valores para x1 (de -10 a 10)
x1 = np.linspace(-10, 10, 400)

# Calcular los valores correspondientes de x2 para ambas ecuaciones
x2_1 = (b1 - A1[0] * x1) / A1[1]
x2_2 = (b2 - A2[0] * x1) / A2[1]

# Graficar las líneas correspondientes a las ecuaciones
plt.figure(figsize=(8, 6))
plt.plot(x1, x2_1, label='1.0001*x1 + 1.0000*x2 = 2')
plt.plot(x1, x2_2, label='1.0000*x1 + 1.0000*x2 = 2', linestyle='--')

# Añadir etiquetas y título
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Gráfica del sistema de ecuaciones')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()