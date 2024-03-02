from abc import ABC, abstractmethod

class OptimizationAlgorithm(ABC):
    def __init__(self, mathematical_model):
        self.mathematical_model = mathematical_model

    @abstractmethod
    def optimize(self):
        pass

class GeneticAlgorithm(OptimizationAlgorithm):
    
    def optimize(self):
        pass