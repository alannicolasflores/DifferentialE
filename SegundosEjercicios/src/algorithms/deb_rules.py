class deb_rules:
    def __init__(self, mathematical_model, epsilon=0.0001):
        # Inicialización de la clase con un modelo matemático y un valor epsilon para tolerancia en comparaciones.
        self.mathematical_model = mathematical_model
        self.epsilon = epsilon
        
    def evaluate_constraints(self, solution):
        # Obtiene las restricciones, sus valores y operadores del modelo matemático para la solución dada.
        conditions, function, inequality_operators = self.mathematical_model.get_constraints(solution)

        
        total_violations = 0  # Inicializa el contador de violaciones totales de las restricciones.
        all_feasible = True  # Asume que todas las condiciones son inicialmente factibles.

        for idx, cond in enumerate(conditions):
            condition_result = cond(solution)  # Evalúa cada condición para la solución dada.
            
            operator = inequality_operators[idx]  # Obtiene el operador correspondiente a la condición actual.

            if not condition_result:
                # Si la condición es falsa, evalúa las reglas de Deb específicas para esa condición.
                if operator == "==":
                    # Si el operador es de igualdad, verifica si la condición se desvía de cero más que 'epsilon'.
                    if abs(condition_result) > self.epsilon:
                        # 'abs' calcula el valor absoluto, convirtiendo los números negativos en positivos.
                        total_violations += abs(condition_result)  # Suma la violación a 'total_violations'.
                        all_feasible = False  # Marca la solución como no factible si hay alguna violación.
                else:
                    # Para operadores de desigualdad, verifica si la condición no se cumple.
                    total_violations += abs(function[idx])  # Suma la violación de desigualdad.
                    all_feasible = False  # Marca como no factible si hay violación.
        if all_feasible == True:
            pass    #print("Factible")
            
        return total_violations, all_feasible

    
    def evaluate_individual(self, individual):
        # Convierte el individuo a un diccionario de variables basado en los nombres definidos en el modelo.
        variable_names = self.mathematical_model.get_variable_names()
        solution_dict = {name: individual[i] for i, name in enumerate(variable_names)}
        
        # Calcula el valor de la función objetivo para el diccionario de soluciones.
        objective_value = self.mathematical_model.get_objective_function(solution_dict)
        
        # Evalúa las restricciones para el individuo, obteniendo violaciones totales y factibilidad.
        total_violations, _ = self.evaluate_constraints(solution_dict)
        
        # Devuelve el individuo, su valor objetivo, violaciones totales 
        return individual, objective_value, total_violations
    
    def compare(self, individual_a, individual_b):
        # Prepara las soluciones de los individuos A y B para su evaluación.
        variable_names = self.mathematical_model.get_variable_names()
        solution_a = {name: individual_a[i] for i, name in enumerate(variable_names)}
        solution_b = {name: individual_b[i] for i, name in enumerate(variable_names)}
        
        # Evalúa las restricciones para ambos individuos, obteniendo violaciones y factibilidad.
        violations_a, feasible_a = self.evaluate_constraints(solution_a)
        violations_b, feasible_b = self.evaluate_constraints(solution_b)
        
        # Calcula el valor de la función objetivo para ambos individuos.
        objective_a = self.mathematical_model.get_objective_function(solution_a)
        objective_b = self.mathematical_model.get_objective_function(solution_b)


        if feasible_a and feasible_b: # Si ambos individuos son factibles, compara sus valores de función objetivo.
           
            if objective_a < objective_b: 
                return individual_a, objective_a, violations_a
            else:
                return individual_b, objective_b, violations_b
        elif feasible_a: # Si solo el individuo A es factible, lo devuelve.
            
            return individual_a, objective_a, violations_a
        elif feasible_b: # Si solo el individuo B es factible, lo devuelve.
            
            return individual_b, objective_b, violations_b
        else:
            if violations_a < violations_b: # Si ambos individuos son infactibles, compara sus violaciones.
                return individual_a, objective_a, violations_a
            else:
                return individual_b, objective_b, violations_b


            
