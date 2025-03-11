"""
Add plugin for the REPL Calculator.
"""

from app.commands import Command

class AddCommand(Command):
    """
    Command to add two numbers.
    """
    def execute(self, args: str) -> str:
        """
        Add two numbers provided as space-separated arguments.

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
            return "Invalid number input."
        result = num1 + num2
        return f"The result of {num1} add {num2} is equal to {result}"
