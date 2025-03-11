"""
Tests for the basic command-based REPL Calculator (Version 1).
"""

import sys
import os
import pytest

# Ensure the project root is in sys.path so the 'app' package is discoverable.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.__init__ import GreetCommand, AddCommand, ExitCommand
from app.commands import CommandHandler

def test_greet_command():
    """
    Test that GreetCommand returns the expected greeting.
    """
    cmd = GreetCommand()
    result = cmd.execute("")
    assert result == "Hello, world!"

def test_add_command_valid():
    """
    Test that AddCommand returns the correct addition result.
    """
    cmd = AddCommand()
    result = cmd.execute("5 3")
    expected = "The result of 5.0 add 3.0 is equal to 8.0"
    assert result == expected

def test_add_command_usage():
    """
    Test that AddCommand returns a usage message when insufficient arguments are provided.
    """
    cmd = AddCommand()
    result = cmd.execute("5")
    assert result == "Usage: add <num1> <num2>"

def test_add_command_invalid():
    """
    Test that AddCommand returns an error when invalid number input is provided.
    """
    cmd = AddCommand()
    result = cmd.execute("5 a")
    assert "Invalid number input" in result

def test_command_handler_unknown():
    """
    Test that CommandHandler returns the proper error message for an unknown command.
    """
    handler = CommandHandler()
    handler.register_command("greet", GreetCommand())
    result = handler.execute_command("nonexistent")
    assert "No such command: nonexistent" in result

def test_exit_command(monkeypatch):
    """
    Test that ExitCommand causes the application to exit.
    """
    cmd = ExitCommand()
    with pytest.raises(SystemExit):
        cmd.execute("")
