from app.commands import CommandHandler

# Simple command implementations
class GreetCommand:
    def execute(self, args: str) -> str:
        return "Hello, world!"

class AddCommand:
    def execute(self, args: str) -> str:
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
    def execute(self, args: str) -> str:
        import sys
        sys.exit("Exiting the application. Goodbye!")

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        # Manually register commands
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("exit", ExitCommand())

    def start(self):
        print("Command-based REPL Calculator. Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            output = self.command_handler.execute_command(user_input)
            if output:
                print(output)
