
from src.models.AlkylationModel import AlkylationModel
from src.algorithms.DifferentialEvolution import DifferentialEvolution


alkylation_model = AlkylationModel()


diferential_evolution = DifferentialEvolution(alkylation_model, 50 , 0.5, 0.7, 50, None, epsilon=0.01)
#F(04-09)
#[0.1-1] 

best_solution, best_fitness, best_violation = diferential_evolution.optimize()

print(f"Mejor individuo: {best_solution}")
print(f"Mejor resultado: {best_fitness}")
print(f"Violacion de restricciones: {best_violation}")
