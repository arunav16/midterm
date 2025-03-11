"""
Tests for the addition_strategy_factory in the factory module.
"""


from app.commands.factory import addition_strategy_factory, DefaultAdditionStrategy, AlternativeAdditionStrategy

def test_addition_strategy_default(monkeypatch):
    """
    Test that the factory returns a DefaultAdditionStrategy when the ADDITION_STRATEGY
    environment variable is not set.
    """
    monkeypatch.delenv("ADDITION_STRATEGY", raising=False)
    strategy = addition_strategy_factory()
    assert isinstance(strategy, DefaultAdditionStrategy)
    # Verify computation (for example, 2 + 3 should equal 5)
    assert strategy.compute(2, 3) == 5

def test_addition_strategy_alternative(monkeypatch):
    """
    Test that the factory returns an AlternativeAdditionStrategy when the ADDITION_STRATEGY
    environment variable is set to 'alternative'.
    """
    monkeypatch.setenv("ADDITION_STRATEGY", "alternative")
    strategy = addition_strategy_factory()
    assert isinstance(strategy, AlternativeAdditionStrategy)
    # Verify computation (for example, 2 + 3 should equal 5)
    assert strategy.compute(2, 3) == 5
