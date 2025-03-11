"""
Module containing the App class for the advanced Plugin-based REPL Calculator.
This version includes advanced features such as logging configuration, environment variable loading,
calculation history management (using Pandas), and dynamic plugin loading.
"""

import pkgutil
import importlib
import sys
import os
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
from app.history import HistoryManager
from app.commands.factory import addition_strategy_factory
import app.plugins
class App:
    """
    Main application class for the advanced Plugin-based REPL Calculator.
    """
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = dict(os.environ.items())
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()

    def configure_logging(self):
        """
        Configure logging using a configuration file if available; otherwise, use basic configuration.
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """
        Load environment variables into a dictionary.
        
        Returns:
            dict: Environment variables.
        """
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        """
        Dynamically load all plugins from the 'app/plugins' package.
        Each plugin is a package whose __init__.py defines a subclass of Command.
        The plugin's folder name is used as the command key.
        
        Returns:
            dict: The dictionary of registered commands.
        """
        for _, plugin_name, is_pkg in pkgutil.iter_modules(app.plugins.__path__):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'app.plugins.{plugin_name}')
                except ImportError as e:
                    logging.error("Error importing plugin %s: %s", plugin_name, e)
                    continue
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name, item())
                            logging.info("Registered plugin: %s -> %s", plugin_name, item_name)
                    except TypeError:
                        continue
        logging.info("Loaded commands: %s", list(self.command_handler.commands.keys()))
        return self.command_handler.commands

    def start(self):
        """
        Start the REPL loop after loading plugins and record arithmetic operations in history.
        """
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                user_input = input(">>> ").strip()
                if user_input.lower() == "exit":
                    logging.info("Application exit command received.")
                    sys.exit(0)
                result = self.command_handler.execute_command(user_input)
                if result:
                    print(result)
                    tokens = user_input.split(maxsplit=1)
                    cmd_name = tokens[0]
                    if cmd_name in ["add", "subtract", "multiply", "divide"]:
                        self.history_manager.add_record(operation=cmd_name,
                                                        expression=user_input,
                                                        result=result)
        except KeyboardInterrupt:
            logging.info("Application interrupted. Exiting gracefully.")
            sys.exit(0)
        finally:
            logging.info("Saving history and shutting down.")
            self.history_manager.save_history()
            logging.info("Application shutdown.")
