from .MathematicalModel import MathematicalModel

class AlkylationModel(MathematicalModel):
     
    def get_variable_names(self):
        return ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']
    
    def get_objective_function(self, x):
        c = self.get_constants()
       
        result = ((c[1] * x['x1']) +
                      (c[2] * x['x1'] * x['x6']) +
                      (c[3] * x['x3']) +
                      (c[4] * x['x2']) +
                      c[5] -
                      c[6] * x['x3'] * x['x5'])
        return result

    
    def get_variables(self):
        return 7

    
    def get_bounds(self):
        return {
            'x1': (1500, 2000),
            'x2': (1, 120),
            'x3': (3000, 3500),
            'x4': (85, 93),
            'x5': (90, 95),
            'x6': (3, 12),
            'x7': (145, 162)
        }
    
    
    def get_constraints(self, x):
        c = self.get_constants()

        # Lista de expresiones de función para evaluarla y saber el valor del resultado
        conditions = [
            lambda x: c[7] * x['x6']**2 + c[8] * x['x1']**-1 * x['x3'] - c[9] * x['x6']<=1,
            lambda x: c[10] * x['x1'] * x['x3']**-1 + c[11] * x['x1'] * x['x6'] + x['x3']**-1 - c[12] * x['x1'] * x['x3']**-1 + x['x6']**2<=1,
            lambda x: c[13] * x['x6']**2 + c[14] * x['x5'] - c[15] * x['x4'] - c[16] * x['x6']<=1,
            lambda x: c[17] * x['x5']**-1 + c[18] * x['x5']**-1 * x['x6'] + c[19] * x['x4'] * x['x5']**-1 - c[20] * x['x5']**-1 * x['x6']**2<=1,
            lambda x: c[21] * x['x7'] + c[22] * x['x2'] * x['x3']**-1 * x['x4']**-1 - c[23] * x['x1'] * x['x3']**-1<=1,
            lambda x: c[24] * x['x7']**-1 + c[25] * x['x2'] * x['x3']**-1 * x['x7']**-1 - c[26] * x['x2'] * x['x3']**-1 * x['x4']**-1 * x['x7']**-1<=1,
            lambda x: c[27] * x['x5']**-1 + c[28] * x['x5']**-1 * x['x7']<=1,
            lambda x: c[29] * x['x5'] - c[30] * x['x7']<=1,
            lambda x: c[31] * x['x3'] - c[32] * x['x1']<=1,
            lambda x: c[33] * x['x1'] * x['x3']**-1 + c[34] * x['x3']**-1<=1,
            lambda x: c[35] * x['x2'] * x['x3']**-1 * x['x4']**-1 - c[36] * x['x2'] * x['x3']**-1<=1,
            lambda x: c[37] * x['x4'] + c[38] * x['x2']**-1 * x['x3'] * x['x4']<=1,
            lambda x: c[39] * x['x1'] * x['x6'] + c[40] * x['x1'] - c[41] * x['x3']<=1,
            lambda x: c[42] * x['x1']**-1 * x['x3'] + c[43] * x['x1']**-1 - c[44] * x['x6']<=1
        ]

        # Lista de expresiones de condición para evaluar en booleano
        function = [
            c[7] * x['x6']**2 + c[8] * x['x1']**-1 * x['x3'] - c[9] * x['x6'],
            c[10] * x['x1'] * x['x3']**-1 + c[11] * x['x1'] * x['x6'] + x['x3']**-1 - c[12] * x['x1'] * x['x3']**-1 + x['x6']**2,
            c[13] * x['x6']**2 + c[14] * x['x5'] - c[15] * x['x4'] - c[16] * x['x6'],
            c[17] * x['x5']**-1 + c[18] * x['x5']**-1 * x['x6'] + c[19] * x['x4'] * x['x5']**-1 - c[20] * x['x5']**-1 * x['x6']**2,
            c[21] * x['x7'] + c[22] * x['x2'] * x['x3']**-1 * x['x4']**-1 - c[23] * x['x1'] * x['x3']**-1,
            c[24] * x['x7']**-1 + c[25] * x['x2'] * x['x3']**-1 * x['x7']**-1 - c[26] * x['x2'] * x['x3']**-1 * x['x4']**-1 * x['x7']**-1,
            c[27] * x['x5']**-1 + c[28] * x['x5']**-1 * x['x7'],
            c[29] * x['x5'] - c[30] * x['x7'],
            c[31] * x['x3'] - c[32] * x['x1'],
            c[33] * x['x1'] * x['x3']**-1 + c[34] * x['x3']**-1,
            c[35] * x['x2'] * x['x3']**-1 * x['x4']**-1 - c[36] * x['x2'] * x['x3']**-1,
            c[37] * x['x4'] + c[38] * x['x2']**-1 * x['x3'] * x['x4'],
            c[39] * x['x1'] * x['x6'] + c[40] * x['x1'] - c[41] * x['x3'],
            c[42] * x['x1']**-1 * x['x3'] + c[43] * x['x1']**-1 - c[44] * x['x6']
        ]

        # Lista de constantes de las desigualdades
        inequality_constants = [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
        ]

        inequality_operators = [
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<=",
            "<="
        ]

        return  conditions, function, inequality_constants, inequality_operators

 
 
    def get_constants(self):
        # Este método es opcional, puedes implementarlo para obtener las constantes del modelo
        return {
         1: 1.715,
         2: 0.035,
         3: 4.0565,
         4: 10.0,
         5: 3000.0,
         6: 0.063,
         7: 0.59553571E-2,
         8: 0.88392857E-1,
         9: 0.11756250,
         10: 1.10880000,
         11: 0.13035330,
         12: 0.00660330,
         13: 0.66173269E-3,
         14: 0.17239878E-1,
         15: 0.56595559E-2,
         16: 0.19120592E-1,
         17: 0.56850750E+2,
         18: 1.08702000,
         19: 0.32175000,
         20: 0.03762000,
         21: 0.00619800,
         22: 0.24623121E+4,
         23: 0.25125634E+2,
         24: 0.16118996E+3,
         25: 5000.0,
         26: 0.489551000E+6,
         27: 0.44333333E+2,
         28: 0.33000000,
         29: 0.02255600,
         30: 0.00759500,
         31: 0.00061000,
         32: 0.0005,
         33: 0.81967200,
         34: 0.81967200,
         35: 24500.0,
         36: 250.0,
         37: 0.10220482E-1,
         38: 0.12244898E-4,
         39: 0.00006250,
         40: 0.00006250,
         41: 0.00007625,
         42: 1.22,
         43: 1.0,
         44: 1.0
        } 
