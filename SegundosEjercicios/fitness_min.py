import pandas as pd

# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv('optimization_results_2.csv')

# Asumiendo que quieres encontrar los 10 mínimos de la columna 'Mejor Fitness'
# También seleccionamos las columnas 'F' y 'CR'
minimos = df.nsmallest(10, 'Mejor Fitness')[['F', 'CR', 'Mejor Fitness']]

print(minimos)

