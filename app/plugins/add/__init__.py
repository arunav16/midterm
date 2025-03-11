"""
Add plugin for the REPL Calculator.
Uses a strategy pattern via a factory for addition.
"""

from app.commands import Command
from app.commands.factory import addition_strategy_factory

class AddCommand(Command):
    """
    Command to add two numbers using a factory-based strategy.
    """
    def __init__(self):
        self.strategy = addition_strategy_factory()

    def execute(self, args: str) -> str:
        """
        Add two numbers provided as space-separated arguments using the selected strategy.

        Parameters:
            args (str): Two numbers separated by a space.

        Returns:
            str: The result message or an error message.
        """
        tokens = args.split()
        if len(tokens) != 2:
            return "Usage: add <num1> <num2>"
        try:
            num1 = float(tokens[0])
            num2 = float(tokens[1])
        except ValueError:
            return f"Invalid number input: {tokens[0]} or {tokens[1]} is not valid."
        result = self.strategy.compute(num1, num2)
        return f"The result of {num1} add {num2} is equal to {result}"
