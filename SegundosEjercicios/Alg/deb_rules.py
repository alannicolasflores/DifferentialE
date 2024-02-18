class deb_rules:
    def __init__(self, mathematical_model, epsilon=0.0001):
        self.mathematical_model = mathematical_model
        self.epsilon = epsilon
        
    def evaluate_constraints(self, solution):
        # Obtener las restricciones desde el modelo
        conditions, function , inequality_constants, inequality_operators = self.mathematical_model.get_constraints(solution)

        # Lista para almacenar los resultados de las condiciones (True si se cumple, False si no)
        condition_results = [cond(solution) for cond in conditions]
        
        
        # Comprobar si todas las condiciones son True (usando all())
        if all(condition_results):
            # No hay violaciones si todas las condiciones se cumplen
            return 0
        
        # Si no todas las condiciones se cumplen, calcular las violaciones específicas
        total_violations = 0
        for idx, condition_result in enumerate(condition_results):
            if not condition_result:  # Si la condición no se cumple (False)
                # Suponemos que necesitamos calcular la diferencia entre el valor actual y el valor límite
                # La manera específica de calcular esta violación dependerá de tu modelo y condiciones
                
                violation = self.calculate_violation( function[idx],  inequality_constants[idx], inequality_operators[idx])
                total_violations += violation

        return total_violations

    def calculate_violation(self,  function , constant, operator):
        
        if(operator == "<="):
            return function - constant
        if(operator == ">="):
            return constant - function
        else:
            return 0  # Retorna el cálculo de la violación aquí
    
    def is_feasible(self, solution):
        return self.evaluate_constraints(solution) <= self.epsilon
    
    def evaluate_individual(self, individual):
        # Asumiendo que 'individual' es un array numpy o una lista de valores de variables
        # Convertir el individuo a un diccionario de variables para la evaluación
        variable_names = self.mathematical_model.get_variable_names()
        solution_dict = {name: individual[i] for i, name in enumerate(variable_names)}
        
        # Calcular el valor de la función objetivo
        objective_value = self.mathematical_model.get_objective_function(solution_dict)
        
        # Calcular las violaciones de las restricciones
        total_violations = self.evaluate_constraints(solution_dict)

        
        # Retornar el individuo, su valor de función objetivo y las violaciones totales
        # Nota: El retorno de 'is_feasible' es opcional, dependiendo de si deseas utilizarlo posteriormente
        return individual, objective_value, total_violations
    
    def compare(self, individual_a, individual_b):
        # Convertir los individuos a diccionarios de variables para la evaluación
        variable_names = self.mathematical_model.get_variable_names()
        solution_a = {name: individual_a[i] for i, name in enumerate(variable_names)}
        solution_b = {name: individual_b[i] for i, name in enumerate(variable_names)}
        
        # Proceder con la evaluación y comparación como antes
        feasible_a = self.is_feasible(solution_a)
        feasible_b = self.is_feasible(solution_b)
        objective_a = self.mathematical_model.get_objective_function(solution_a)
        objective_b = self.mathematical_model.get_objective_function(solution_b)

        violations_a = self.evaluate_constraints(solution_a)
        violations_b = self.evaluate_constraints(solution_b)

        # Seleccionar el mejor individuo basado en la factibilidad y el valor de la función objetivo
        if feasible_a and feasible_b:
            better_individual = individual_a if objective_a < objective_b else individual_b
        elif feasible_a:
            better_individual = individual_a
        elif feasible_b:
            better_individual = individual_b
        else:
            better_individual = individual_a if violations_a < violations_b else individual_b

        # Determinar las violaciones y el valor de la función objetivo del mejor individuo
        better_violations = violations_a if better_individual is individual_a else violations_b
        better_objective = objective_a if better_individual is individual_a else objective_b

        # Retornar directamente el mejor individuo junto con su violación total y el valor de la función objetivo
        return better_individual, better_objective, better_violations

