"""
Tests for the basic command-based REPL Calculator (Version 1).
"""
#import sys
#import os
import pytest
from app.commands import CommandHandler
from app.__init__ import App, GreetCommand, AddCommand, ExitCommand


# Ensure the project root is in sys.path so the 'app' package is discoverable.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def test_greet_command():
    """
    Test that GreetCommand returns the correct greeting.
    """
    cmd = GreetCommand()
    result = cmd.execute("")
    assert result == "Hello, world!"

def test_add_command_valid():
    """
    Test that AddCommand returns the correct result when given valid input.
    """
    cmd = AddCommand()
    result = cmd.execute("5 3")
    expected = "The result of 5.0 add 3.0 is equal to 8.0"
    assert result == expected

def test_add_command_usage():
    """
    Test that AddCommand returns a usage message when not given two arguments.
    """
    cmd = AddCommand()
    result = cmd.execute("5")
    assert result == "Usage: add <num1> <num2>"

def test_add_command_invalid():
    """
    Test that AddCommand returns an error message for invalid number input.
    """
    cmd = AddCommand()
    result = cmd.execute("5 a")
    assert "Invalid number input" in result

def test_exit_command():
    """
    Test that ExitCommand terminates the program.
    """
    cmd = ExitCommand()
    with pytest.raises(SystemExit):
        cmd.execute("")

def test_command_handler_unknown():
    """
    Test that CommandHandler returns an error for an unknown command.
    """
    handler = CommandHandler()
    handler.register_command("greet", GreetCommand())
    result = handler.execute_command("nonexistent")
    assert "No such command: nonexistent" in result

def test_app_start(monkeypatch, capsys):
    """
    Simulate a short REPL session:
      - Type "greet" (should output greeting).
      - Type "add 5 3" (should output addition result).
      - Type "exit" (should cause the app to exit).
    """
    inputs = iter(["greet", "add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    with pytest.raises(SystemExit):
        App().start()
    captured = capsys.readouterr().out
    assert "Hello, world!" in captured
    assert "The result of 5.0 add 3.0 is equal to 8.0" in captured
