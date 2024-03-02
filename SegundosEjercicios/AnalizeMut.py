import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv('optimization_results.csv')

# Agrupar por generación y calcular la media de los resultados
mean_results_by_generation = df.groupby('Generacion')['Resultado'].mean()

# Opcional: calcular también la desviación estándar para ver la dispersión de los resultados
std_dev_results_by_generation = df.groupby('Generacion')['Resultado'].std()

# Imprimir las medias de los resultados por generación
print("Media de los resultados por generación:")
print(mean_results_by_generation)

# Imprimir las desviaciones estándar de los resultados por generación
print("\nDesviación estándar de los resultados por generación:")
print(std_dev_results_by_generation)

# Opcional: Crear un gráfico simple para visualizar la convergencia
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(mean_results_by_generation.index, mean_results_by_generation.values, label='Media de Resultados')
plt.fill_between(mean_results_by_generation.index,
                 mean_results_by_generation.values - std_dev_results_by_generation.values,
                 mean_results_by_generation.values + std_dev_results_by_generation.values,
                 color='gray', alpha=0.2, label='Desviación Estándar')
plt.title('Convergencia de Resultados por Generación')
plt.xlabel('Generación')
plt.ylabel('Resultado')
plt.legend()
plt.grid(True)
plt.show()
