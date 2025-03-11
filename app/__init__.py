"""
Module containing the App class for the Plugin-based REPL Calculator.
This version dynamically loads commands from the app/plugins folder.
"""
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
import app.plugins

class App:
    """
    Main application class for the Plugin-based REPL Calculator.
    """
    def __init__(self):
        """
        Initialize the App with a CommandHandler.
        """
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """
        Dynamically load all plugins from the 'app/plugins' package.
        Each plugin is a package whose __init__.py defines a subclass of Command.
        The plugin's folder name is used as the command key.
        """
        for _, plugin_name, is_pkg in pkgutil.iter_modules(app.plugins.__path__):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'app.plugins.{plugin_name}')
                except ImportError as e:
                    print("Error importing plugin %s: %s", plugin_name, e)
                    continue
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
        print("Loaded commands: ", list(self.command_handler.commands.keys()))
        return self.command_handler.commands



    def start(self):
        """
        Start the REPL loop after loading plugins.
        """
        self.load_plugins()
        print("Plugin-based REPL Calculator. Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == "exit":
                sys.exit("Exiting the application. Goodbye!")
            output = self.command_handler.execute_command(user_input)
            if output:
                print(output)
