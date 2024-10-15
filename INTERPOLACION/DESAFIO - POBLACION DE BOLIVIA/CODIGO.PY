# Volvemos a verificar el ajuste del modelo logístico y lineal para corregir cualquier error
from scipy.optimize import curve_fit

# Redefinimos los datos actualizados de años y población
years_updated = np.array([2010, 2015, 2020, 2023, 2024])
population_updated = np.array([10.03, 10.98, 11.67, 12.1, 11.31])

# Función para extrapolación lineal
def linear_model(x, a, b):
    return a * x + b

# Ajustamos los datos de años y población a un modelo lineal
params, _ = curve_fit(linear_model, years_updated, population_updated)

# Proyección para 2024 y 2025 con extrapolación lineal
pop_2024_linear = linear_model(2024, *params)
pop_2025_linear = linear_model(2025, *params)

# Modelo logístico para crecimiento poblacional (L es la población máxima estimada)
def logistic_model(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# Ajustamos los datos al modelo logístico con valores iniciales L, k, x0
logistic_params, _ = curve_fit(logistic_model, years_updated, population_updated, p0=[12, 0.03, 2015])

# Proyección para 2024 y 2025 con el modelo logístico
pop_2024_logistic = logistic_model(2024, *logistic_params)
pop_2025_logistic = logistic_model(2025, *logistic_params)

# Resultados corregidos
pop_2024_linear, pop_2025_linear, pop_2024_logistic, pop_2025_logistic