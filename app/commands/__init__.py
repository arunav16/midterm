"""
Module containing the abstract Command class and the CommandHandler
for the advanced REPL Calculator.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for a command.
    """
    @abstractmethod
    def execute(self, args: str) -> str:
        """
        Execute the command with the provided arguments and return a result string.
        
        Parameters:
            args (str): The arguments for the command.
        
        Returns:
            str: The result message.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")

class CommandHandler:
    """
    Class for registering and executing commands.
    """
    def __init__(self):
        """
        Initialize an empty registry for commands.
        """
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """
        Register a command under a given name.
        
        Parameters:
            command_name (str): The key for the command.
            command (Command): An instance of a Command subclass.
        """
        self.commands[command_name] = command

    def execute_command(self, command_line: str) -> str:
        """
        Execute a command based on the command line input.
        
        Parameters:
            command_line (str): The full command line string.
        
        Returns:
            str: The result of executing the command or an error message.
        """
        tokens = command_line.split(maxsplit=1)
        cmd_name = tokens[0]
        args = tokens[1] if len(tokens) > 1 else ""
        try:
            return self.commands[cmd_name].execute(args)
        except KeyError:
            return f"No such command: {cmd_name}"
