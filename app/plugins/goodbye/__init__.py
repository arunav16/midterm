"""
Goodbye plugin for the REPL Calculator.
"""

from app.commands import Command

class GoodbyeCommand(Command):
    """
    Command to say goodbye.
    """
    def execute(self, args: str) -> str:
        """
        Return a farewell message.

        Parameters:
            args (str): Unused.

        Returns:
            str: "Goodbye!"
        """
        return "Goodbye!"
