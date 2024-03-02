import unittest
import numpy as np
from src.algorithms.DifferentialEvolution import DifferentialEvolution

class TestAdjustMutantComponent(unittest.TestCase):

    def test_random_mutant_components(self):
        # Realiza 100 pruebas con valores aleatorios
        for i in range(100):
            # Genera componentes y límites aleatorios
            mutant_component = np.random.uniform(-100, 200)  # Valor fuera de los límites típicos
            lower_bound = np.random.uniform(0, 50)  # Límite inferior aleatorio
            upper_bound = np.random.uniform(50, 100)  # Límite superior aleatorio

            # Ajusta el componente mutante
            result = DifferentialEvolution.adjust_mutant_component(mutant_component, lower_bound, upper_bound)
            
            # Comprueba que el resultado esté dentro de los límites
            with self.subTest(i=i):
                self.assertTrue(lower_bound <= result <= upper_bound,
                                f"Test #{i}, Result: {result}, Lower: {lower_bound}, Upper: {upper_bound}")

if __name__ == '__main__':
    unittest.main()
