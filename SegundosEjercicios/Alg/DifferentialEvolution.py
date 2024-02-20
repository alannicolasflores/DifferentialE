import numpy as np

from .OptimizationAlgorithm import OptimizationAlgorithm
from .deb_rules import deb_rules

import numpy as np

class DifferentialEvolution(OptimizationAlgorithm):
    def __init__(self, mathematical_model, population_size, F, CR, max_generations, seed=None, epsilon=0.0001):
        super().__init__(mathematical_model)
        self.population_size = population_size
        self.F = F
        self.CR = CR
        self.max_generations = max_generations
        self.seed = seed  # Agregar un atributo para la semilla
        self.deb = deb_rules(mathematical_model, epsilon)

    def _initialize_population(self):
        # Establecer la semilla del generador de números aleatorios si se proporcionó una
        if self.seed is not None:
            np.random.seed(self.seed)
        
        bounds = self.mathematical_model.get_bounds()
        num_variables = self.mathematical_model.get_variables()

        # Inicializar la población con valores aleatorios dentro de los límites
        population = np.zeros((self.population_size, num_variables))
        for i, (key, (lower, upper)) in enumerate(bounds.items()):
            population[:, i] = np.random.uniform(lower, upper, self.population_size)

        self.population = population
        return population
 
    def _mutate_and_recombine(self, population, target_idx):
        # Número de variables de decisión
        num_variables = self.mathematical_model.get_variables()
        
        # Seleccionar tres índices aleatorios distintos de target_idx
        candidates = [idx for idx in range(self.population_size) if idx != target_idx]
        rand1, rand2, rand3 = np.random.choice(candidates, 3, replace=False)
        
        # Crear el vector mutante
        mutant_vector = population[rand1] + self.F * (population[rand2] - population[rand3])
        
        # Recombinación para crear el vector de prueba
        trial_vector = np.array([mutant_vector[j] 
                                 if np.random.rand() < self.CR or j == np.random.randint(0, num_variables) 
                                else population[target_idx, j] for j in range(num_variables)])
        
        # Obtener los límites de cada variable
        bounds = self.mathematical_model.get_bounds()
        variable_names = self.mathematical_model.get_variable_names()
    
        # Ajustar las variables fuera de los límites
        for i, name in enumerate(variable_names):
            lower_bound, upper_bound = bounds[name]
            if trial_vector[i] < lower_bound:
                trial_vector[i] = lower_bound + (lower_bound - trial_vector[i])  # Reflejar sobre el límite inferior
            elif trial_vector[i] > upper_bound:
                trial_vector[i] = upper_bound - (trial_vector[i] - upper_bound)  # Reflejar sobre el límite superior
        
        return trial_vector

    

        

    def _get_bounds_arrays(self):
        # Obtener los límites de cada variable como arreglos separados
        bounds = self.mathematical_model.get_bounds()
        lower_bounds = np.array([bound[0] for bound in bounds.values()])
        upper_bounds = np.array([bound[1] for bound in bounds.values()])
        return lower_bounds, upper_bounds
    
    def _select_best_solution(self, population):
        # Inicializa la mejor solución y el mejor valor de la función objetivo
        best_solution = population[0]
        best_fitness = self.mathematical_model.get_objective_function(best_solution)

        # Itera a través de la población para encontrar la mejor solución
        for individual in population:
            fitness = self.mathematical_model.get_objective_function(individual)
            if fitness < best_fitness:
                best_solution = individual
                best_fitness = fitness

        return best_solution
    
    
    
    def optimize(self):
        # Inicializar población
        population = self._initialize_population()
        # Inicializar estructuras para almacenar el valor de la función objetivo, violaciones y los individuos
        objective_values = np.zeros(self.population_size)
        violations = np.zeros(self.population_size)
        # La población ya está definida

        
        # Evaluar la aptitud inicial de la población
        for i, individual in enumerate(population):
            _, objective_values[i], violations[i] = self.deb.evaluate_individual(individual)
  
        # Iterar para cada generación
        for G in range(self.max_generations):
            for i in range(self.population_size):
                # Mutar y recombinar para crear el vector de prueba
                trial_vector = self._mutate_and_recombine(population, i)

                # Comparar directamente el individuo actual con el vector de prueba utilizando las DebRules
                # Asumiendo que 'DebRules.compare' ahora se encarga de evaluar ambos internamente
                # y decide cuál de los dos (individuo actual vs. vector de prueba) es mejor
# Supongamos que 'compare' retorna el mejor individuo, su resultado (valor de función objetivo),
# y sus violaciones de restricciones
                better_individual, better_result, better_violation = self.deb.compare(population[i], trial_vector)
                
                # Actualizar la población y los registros correspondientes si el vector de prueba es mejor
                # Aquí comprobamos si el 'better_individual' es igual a 'trial_vector'
                if np.array_equal(better_individual, trial_vector):
                    population[i] = trial_vector
                    objective_values[i] = better_result
                    violations[i] = better_violation
        print(objective_values)
        # Encontrar los índices de las soluciones sin violaciones.
        no_violation_index = np.where(violations == 0)[0]

        if len(no_violation_index) > 0:
            # Si hay al menos una solución sin violaciones, selecciona la de mejor fitness entre ellas.
            # Extrae los valores de la función objetivo de las soluciones sin violaciones.
            no_violation_objective_values = objective_values[no_violation_index]
            
            # Encuentra el índice de la mejor valor de función objetivo entre las soluciones sin violaciones.
            best_no_violation_index = no_violation_index[np.argmin(no_violation_objective_values)]
            
            best_solution = population[best_no_violation_index]
            best_fitness = objective_values[best_no_violation_index]
            best_violation = violations[best_no_violation_index]
            
        else:
            # Si no hay soluciones sin violaciones, podrías manejar esto de diferentes maneras.
            # Una opción es simplemente seleccionar la solución con el menor número de violaciones,
            # o podrías decidir manejar este caso de una manera específica relevante para tu problema.
            print("No se encontraron soluciones sin violaciones.")
            # Aquí podrías retornar None o alguna solución por defecto, dependiendo de tus necesidades.
            
            
            return None, None, None

        
        return best_solution, best_fitness, best_violation

