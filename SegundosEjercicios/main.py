
from ModMat.AlkylationModel import AlkylationModel
from Alg.DifferentialEvolution import DifferentialEvolution


alkylation_model = AlkylationModel()


diferential_evolution = DifferentialEvolution(alkylation_model, 150 , 0.9, 0.8, 5, None, epsilon=0.0001)


best_solution, best_fitness, best_violation = diferential_evolution.optimize()

print(f"Mejor individuo: {best_solution}")
print(f"Mejor resultado: {best_fitness}")
print(f"Violacion de restricciones: {best_violation}")
