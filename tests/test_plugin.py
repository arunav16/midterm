"""
Tests for the Plugin-based REPL Calculator (Version 2).
"""

import pytest
from app import App
from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.exit import ExitCommand

def test_load_plugins():
    """
    Test that the App.load_plugins() method loads the expected plugins.
    Expected plugins are 'greet', 'add', and 'exit'.
    """
    app_instance = App()
    commands = app_instance.load_plugins()
    expected = {"greet", "add", "exit"}
    assert expected.issubset(set(commands.keys()))

def test_plugin_greet():
    """
    Test the greet plugin.
    """
    cmd = GreetCommand()
    result = cmd.execute("")
    assert result == "Hello, world!"

def test_plugin_add_valid():
    """
    Test the add plugin with valid input.
    """
    cmd = AddCommand()
    result = cmd.execute("5 3")
    expected = "The result of 5.0 add 3.0 is equal to 8.0"
    assert result == expected

def test_plugin_add_invalid():
    """
    Test the add plugin with invalid input.
    """
    cmd = AddCommand()
    result = cmd.execute("5 a")
    assert "Invalid number input" in result

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
      - "greet" should output greeting.
      - "add 5 3" should output addition result.
      - "nonexistent" should output an unknown command message.
      - "exit" should terminate the REPL.
    """
    inputs = iter(["greet", "add 5 3", "nonexistent", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    with pytest.raises(SystemExit):
        App().start()
    output = capsys.readouterr().out
    assert "Hello, world!" in output
    assert "The result of 5.0 add 3.0 is equal to 8.0" in output
    assert "No such command: nonexistent" in output
