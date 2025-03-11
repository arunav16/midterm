"""
Subtract plugin for the REPL Calculator.
"""

from app.commands import Command

class SubtractCommand(Command):
    """
    Command to subtract two numbers.
    """
    def execute(self, args: str) -> str:
        """
        Subtract two numbers provided as space-separated arguments.

        Parameters:
            args (str): Two numbers separated by a space.

        Returns:
            str: The result message or an error message.
        """
        tokens = args.split()
        if len(tokens) != 2:
            return "Usage: subtract <num1> <num2>"
        try:
            num1 = float(tokens[0])
            num2 = float(tokens[1])
        except ValueError:
            return f"Invalid number input: {tokens[0]} or {tokens[1]} is not valid."
        result = num1 - num2
        return f"The result of {num1} subtract {num2} is equal to {result}"
