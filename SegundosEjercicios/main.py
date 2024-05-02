from src.models.AlkylationModel import AlkylationModel
from src.algorithms.DifferentialEvolution import DifferentialEvolution
import numpy as np
import csv  
# Configura los rangos para F y CR
csv_filename = 'optimization_results_2.csv'

# Abre el archivo CSV para escribir los encabezados y los datos
with open(csv_filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    # Escribe los encabezados del archivo CSV
    file.seek(0, 2)  # Mueve el cursor al final del archivo
    if file.tell() == 0:  # Si estamos al principio, el archivo está vacío
        writer.writerow(['F', 'CR', 'Mejor Solución', 'Mejor Fitness', 'Violaciones'])

F_values = [ 0.8, 0.9]
CR_values = [0.11, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999]
# Inicializa el modelo de alquilación
alkylation_model = AlkylationModel()
for _ in range(1): 
    for F in F_values:
        for CR in CR_values:
            differential_evolution = DifferentialEvolution(alkylation_model, 70, F, CR, 200, None, epsilon=0.01)
            best_solution, best_fitness, best_violation = differential_evolution.optimize()
            
            # Abre el archivo CSV para escribir los datos
            with open(csv_filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([F, CR, best_solution, best_fitness, best_violation])
            
            print(f"F: {F}, CR: {CR}, Mejor solucion: {best_solution}, Mejor fitness: {best_fitness}, Violaciones: {best_violation}")
            
    
