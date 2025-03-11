"""
Integration tests for the advanced Plugin-based REPL Calculator (Version 3).
"""

import os
import pytest
#import tempfile
from app import App
from app.history import HistoryManager
from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.exit import ExitCommand
from app.plugins.history import HistoryCommand

def test_load_plugins():
    """
    Test that App.load_plugins() loads all expected plugins.
    Expected plugins: greet, add, subtract, multiply, divide, exit, goodbye.
    """
    app_instance = App()
    commands = app_instance.load_plugins()
    expected = {"greet", "add", "subtract", "multiply", "divide", "exit", "goodbye"}
    assert expected.issubset(set(commands.keys()))

def test_history_manager_add_and_get():
    """
    Test that HistoryManager correctly adds and retrieves a record.
    """
    hm = HistoryManager()
    hm.clear_history()
    hm.add_record("add", "5 3", "8")
    history = hm.get_history()
    assert not history.empty
    last_record = history.iloc[-1]
    assert last_record["operation"] == "add"
    assert last_record["result"] == "8"

def test_history_manager_save_and_load(tmp_path):
    """
    Test that HistoryManager can save to and load from a CSV file.
    """
    hm = HistoryManager()
    hm.clear_history()
    hm.add_record("subtract", "10 2", "8")
    filename = tmp_path / "history.csv"
    hm.save_history(str(filename))
    hm.clear_history()
    hm.load_history(str(filename))
    history = hm.get_history()
    assert not history.empty
    assert history.iloc[-1]["operation"] == "subtract"

def test_plugin_greet():
    """
    Test that the greet plugin returns the expected greeting.
    """
    cmd = GreetCommand()
    result = cmd.execute("")
    assert result == "Hello, world!"

def test_plugin_add_valid():
    """
    Test that the add plugin returns the correct result with valid input.
    """
    cmd = AddCommand()
    result = cmd.execute("5 3")
    expected = "The result of 5.0 add 3.0 is equal to 8.0"
    assert result == expected

def test_plugin_add_usage():
    """
    Test that the add plugin returns a usage message when insufficient arguments are provided.
    """
    cmd = AddCommand()
    result = cmd.execute("5")
    assert result == "Usage: add <num1> <num2>"

def test_plugin_add_invalid():
    """
    Test that the add plugin returns an error for invalid numeric input.
    """
    cmd = AddCommand()
    result = cmd.execute("5 a")
    assert "Invalid number input" in result

def test_plugin_subtract():
    """
    Test that the subtract plugin returns the correct result.
    """
    cmd = SubtractCommand()
    result = cmd.execute("10 2")
    expected = "The result of 10.0 subtract 2.0 is equal to 8.0"
    assert result == expected

def test_plugin_subtract_usage():
    """
    Test that SubtractCommand returns a usage message when not given exactly two arguments.
    """
    cmd = SubtractCommand()
    result = cmd.execute("10")
    assert result == "Usage: subtract <num1> <num2>"

def test_plugin_subtract_invalid():
    """
    Test that SubtractCommand returns an error message for invalid numeric input.
    """
    cmd = SubtractCommand()
    result = cmd.execute("10 a")
    assert "Invalid number input" in result

def test_plugin_multiply():
    """
    Test that the multiply plugin returns the correct result.
    """
    cmd = MultiplyCommand()
    result = cmd.execute("4 5")
    expected = "The result of 4.0 multiply 5.0 is equal to 20.0"
    assert result == expected

def test_plugin_multiply_usage():
    """Usage Test"""
    cmd = MultiplyCommand()
    result = cmd.execute("4")
    assert result == "Usage: multiply <num1> <num2>"

def test_plugin_multiply_invalid():
    """Invalid Input Test"""
    cmd = MultiplyCommand()
    result = cmd.execute("4 b")
    assert "Invalid number input" in result

def test_plugin_divide_valid():
    """
    Test that the divide plugin returns the correct result for valid input.
    """
    cmd = DivideCommand()
    result = cmd.execute("20 4")
    expected = "The result of 20.0 divide 4.0 is equal to 5.0"
    assert result == expected

def test_plugin_divide_usage():
    """
    Test that the divide plugin returns a usage message when insufficient arguments are provided.
    """
    cmd = DivideCommand()
    result = cmd.execute("20")
    assert result == "Usage: divide <num1> <num2>"

def test_plugin_divide_invalid():
    """
    Test that the divide plugin returns an error for invalid numeric input.
    """
    cmd = DivideCommand()
    result = cmd.execute("20 a")
    assert "Invalid number input" in result

def test_plugin_divide_by_zero():
    """
    Test that the divide plugin returns an error message when dividing by zero.
    """
    cmd = DivideCommand()
    result = cmd.execute("10 0")
    assert "Cannot divide by zero" in result

def test_plugin_goodbye():
    """
    Test that the goodbye plugin returns the expected farewell message.
    """
    cmd = GoodbyeCommand()
    result = cmd.execute("")
    assert result == "Goodbye!"

def test_plugin_exit(monkeypatch):
    """
    Test that the exit plugin terminates the application.
    """
    cmd = ExitCommand()
    with pytest.raises(SystemExit):
        cmd.execute("")

def test_app_repl(monkeypatch, capsys):
    """
    Simulate a REPL session:
      1. "greet" should output a greeting.
      2. "add 5 3" should output the addition result.
      3. "nonexistent" should output an unknown command message.
      4. "exit" should terminate the REPL.
    """
    inputs = iter(["greet", "add 5 3", "nonexistent", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    with pytest.raises(SystemExit):
        App().start()
    output = capsys.readouterr().out
    assert "Hello, world!" in output
    assert "The result of 5.0 add 3.0 is equal to 8.0" in output
    assert "No such command: nonexistent" in output
def test_history_command_no_args_empty(monkeypatch):
    """Ensure history is cleared"""
    HistoryManager().clear_history()
    cmd = HistoryCommand()
    result = cmd.execute("")
    assert result == "No history available."

def test_history_command_no_args_non_empty(monkeypatch):
    """Check that the history string includes the record"""
    hm = HistoryManager()
    hm.clear_history()
    hm.add_record("add", "5 3", "8")
    cmd = HistoryCommand()
    result = cmd.execute("")
    assert "add" in result

def test_history_command_with_args():
    """Check that the history command doesnt accept any args"""
    cmd = HistoryCommand()
    result = cmd.execute("extra")
    assert result == "History command does not accept any arguments."

def test_environment_loading():
    """
    Test that App.load_environment_variables() returns a dictionary
    containing environment variables.
    """
    app_instance = App()
    env_vars = app_instance.load_environment_variables()
    assert isinstance(env_vars, dict)
    # Check that at least one variable from os.environ is present.
    for key in os.environ:
        assert key in env_vars
