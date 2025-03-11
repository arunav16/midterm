"""
Exit plugin for the REPL Calculator.
"""

import sys
from app.commands import Command

class ExitCommand(Command):
    """
    Command to exit the application.
    """
    def execute(self, args: str) -> str:
        """
        Exit the application.

        Parameters:
            args (str): Unused.

        This method terminates the program.
        """
        sys.exit("Exiting the application. Goodbye!")
