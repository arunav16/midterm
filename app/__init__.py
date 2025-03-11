"""
Module containing the App class and basic command implementations for the REPL Calculator.
"""
import sys
from app.commands import CommandHandler

class GreetCommand:
    """
    Command to return a greeting.
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

class AddCommand:
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

class ExitCommand:
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

class App:
    """
    Main application class for the REPL Calculator.
    """
    def __init__(self):
        """
        Initialize the App with a CommandHandler and register commands manually.
        """
        self.command_handler = CommandHandler()
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("exit", ExitCommand())

    def start(self):
        """
        Start the REPL loop.
        """
        print("Command-based REPL Calculator. Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            output = self.command_handler.execute_command(user_input)
            if output:
                print(output)
