from ModMat.MathematicalModel import MathematicalModel

class HeatExchangerDesign(MathematicalModel):
     
    def get_objective_function(self, x):
        # Obtenemos las constantes llamando al método get_constants()
        # Utilizamos las constantes obtenidas para calcular el valor de la función objetivo.
        return x['x1'] + x['x2'] + x['x3']
    
    def get_variables(self):
        return 8

    def get_variable_names(self):
        return ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
    
    def get_bounds(self):
        return {
            'x1': (100, 10000),
            'x2': (1000, 10000),
            'x3': (1000, 10000),
            'x4': (10, 1000),
            'x5': (10, 1000),
            'x6': (10, 1000),
            'x7': (10, 1000),
            'x8': (10, 1000)
        }
        
    def get_constraints(self, x):
        # Definimos las condiciones directamente, sin usar un método get_constants()
        conditions = [
            lambda x: 833.33252*x['x1']**-1 * x['x4'] * x['x6']**-1 + 100.0*x['x6']**-1 - 83333.333*x['x1']**-1 * x['x6']**-1 <= 1,
            lambda x: 1250.0*x['x2']**-1 * x['x5'] * x['x7']**-1 + 1.04*x['x4'] * x['x7']**-1 - 1250.0*x['x2']**-1 * x['x4'] * x['x7']**-1 <= 1,
            lambda x: 1250000.0*x['x3']**-1 * x['x8']**-1 + x['x8']**-1 + 1.0*x['x5'] - 2500.0*x['x3']**-1 * x['x5'] * x['x8']**-1 <= 1,
            lambda x: 0.0025*x['x4'] + 0.0025*x['x6'] <= 1,
            lambda x: -0.0025*x['x4'] + 0.0025*x['x5'] + 0.0025*x['x7'] <= 1,
            lambda x: 0.01*x['x8'] - 0.01*x['x5'] <= 1,
        ]

        # Lista de expresiones de función para evaluar el valor del resultado
        function = [
            lambda x: 833.33252*x['x1']**-1 * x['x4'] * x['x6']**-1 + 100.0*x['x6']**-1 - 83333.333*x['x1']**-1 * x['x6']**-1,
            lambda x: 1250.0*x['x2']**-1 * x['x5'] * x['x7']**-1 + 1.04*x['x4'] * x['x7']**-1 - 1250.0*x['x2']**-1 * x['x4'] * x['x7']**-1,
            lambda x: 1250000.0*x['x3']**-1 * x['x8']**-1 + x['x8']**-1 + 1.0*x['x5'] - 2500.0*x['x3']**-1 * x['x5'] * x['x8']**-1,
            lambda x: 0.0025*x['x4'] + 0.0025*x['x6'],
            lambda x: -0.0025*x['x4'] + 0.0025*x['x5'] + 0.0025*x['x7'],
            lambda x: 0.01*x['x8'] - 0.01*x['x5'],
        ]

        # Lista de constantes de las desigualdades
        inequality_constants = [
            1,
            1,
            1,
            1,
            1,
            1,
        ]

        # Lista de operadores de desigualdad
        inequality_operators = [
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
        ]

        return conditions, function, inequality_constants, inequality_operators
