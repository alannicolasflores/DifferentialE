import pandas as pd

# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv('optimization_results_2.csv')

# Asumiendo que quieres encontrar los mínimos de una columna específica, reemplaza 'nombre_columna' con el nombre real de tu columna
minimos = df['Mejor Fitness'].nsmallest(10)

print(minimos)