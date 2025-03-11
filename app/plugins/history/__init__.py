"""
History plugin for the REPL Calculator.
Displays the calculation history managed by HistoryManager.
"""

from app.commands import Command
from app.history import HistoryManager

class HistoryCommand(Command):
    """
    Command to show the calculation history.
    """
    def execute(self, args: str) -> str:
        """
        Retrieve and return the calculation history as a string.

        Parameters:
            args (str): Unused.

        Returns:
            str: The history in a string format, or a message if no history exists. if args:
            return "History command does not accept any arguments."
        """
        if args:
            return "History command does not accept any arguments."
        hm = HistoryManager()
        history = hm.get_history()
        if history.empty:
            return "No history available."
        return history.to_string(index=False)
