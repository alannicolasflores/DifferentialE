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
        
        # Inicializar el vector de prueba con el individuo objetivo actual
        trial_vector = np.copy(population[target_idx])
        
        # Obtener los límites de cada variable
        bounds = self.mathematical_model.get_bounds()
        variable_names = self.mathematical_model.get_variable_names()

        # Para cada variable en el individuo
        for j in range(num_variables):
            # Verificar si se realiza la mutación basada en el ratio de recombinación
            if np.random.rand() < self.CR or j == np.random.randint(0, num_variables):
                # Seleccionar tres índices aleatorios distintos de target_idx y de entre sí
                candidates = [idx for idx in range(self.population_size) if idx != target_idx]
                rand1, rand2, rand3 = np.random.choice(candidates, 3, replace=False)
                
                # Crear el componente mutante para la variable j
                mutant_component = population[rand1, j] + self.F * (population[rand2, j] - population[rand3, j])

                # Ajustar el componente mutante si está fuera de los límites
                lower_bound, upper_bound = bounds[variable_names[j]]
                while mutant_component < lower_bound or mutant_component > upper_bound:
                                if mutant_component < lower_bound:
                                    mutant_component = 2 * lower_bound - mutant_component
                                elif mutant_component > upper_bound:
                                    mutant_component = 2 * upper_bound - mutant_component
                            
                # Asignar el componente mutante al vector de prueba
                trial_vector[j] = mutant_component
            # Si no hay mutación, el componente permanece igual (ya está en trial_vector)
        
        return trial_vector

    def optimize(self):
        # Inicializar población
        population = self._initialize_population()
        # Inicializar estructuras para almacenar el valor de la función objetivo, violaciones y los individuos
        objective_values = np.zeros(self.population_size)
        violations = np.zeros(self.population_size)
        # La población ya está definida
        print(population)
        
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

        # Encontrar los índices de las soluciones sin violaciones.
        no_violation_index = np.where(violations == 0)[0]
        print(population)
       
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

