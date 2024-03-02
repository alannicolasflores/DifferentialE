from abc import ABC, abstractmethod

class MathematicalModel(ABC):
    @abstractmethod
    def get_objective_function(self, variables):
        pass

    @abstractmethod
    def get_variables(self):
        pass

    @abstractmethod
    def get_bounds(self):
        pass
    
    @abstractmethod
    def get_constraints(self, variables):
        # Este método es opcional, puedes implementarlo si tu modelo tiene restricciones
        return []

    def get_constants(self):
        # Este método es opcional, puedes implementarlo para obtener las constantes del modelo
        return {}
