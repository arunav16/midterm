"""
Greet plugin for the REPL Calculator.
"""

from app.commands import Command

class GreetCommand(Command):
    """
    Command that returns a greeting.
    """
    def execute(self, args: str) -> str:
        """
        Return a greeting message.

        Parameters:
            args (str): Unused.

        Returns:
            str: "Hello, world!"
        """
        return "Hello, world!"
