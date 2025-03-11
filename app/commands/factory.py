"""
Module implementing a factory for selecting an addition strategy.
"""

import os

class OperationStrategy:
    """
    Base class for an operation strategy.
    """
    def compute(self, num1: float, num2: float) -> float:
        """compute method"""
        raise NotImplementedError("Subclasses must implement this method.")

class DefaultAdditionStrategy(OperationStrategy):
    """
    Default strategy for addition.
    """
    def compute(self, num1: float, num2: float) -> float:
        return num1 + num2

class AlternativeAdditionStrategy(OperationStrategy):
    """
    Alternative strategy for addition (for demonstration, same as default).
    """
    def compute(self, num1: float, num2: float) -> float:
        return num1 + num2

def addition_strategy_factory():
    """
    Factory method to select an addition strategy based on an environment variable.
    
    Returns:
        OperationStrategy: The selected strategy.
    """
    if os.getenv("ADDITION_STRATEGY") == "alternative":
        return AlternativeAdditionStrategy()
    return DefaultAdditionStrategy()
