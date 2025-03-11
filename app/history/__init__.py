"""
HistoryManager: A Singleton that encapsulates Pandas operations for calculation history.
"""

from datetime import datetime
import pandas as pd

class HistoryManager:
    """
    Class History Manager
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HistoryManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'history'):
            self.history = pd.DataFrame(columns=["timestamp", "operation", "expression", "result"])

    def add_record(self, operation: str, expression: str, result: str):
        """
        Add a record to the calculation history.
        """
        record = {
            "timestamp": datetime.now(),
            "operation": operation,
            "expression": expression,
            "result": result
        }
        new_record_df = pd.DataFrame([record])
        if self.history.empty:
            self.history = new_record_df
        else:
            self.history = pd.concat([self.history, new_record_df], ignore_index=True)

    def save_history(self, filename: str = "logs/history.csv"):
        """
        Save the calculation history to a CSV file.
        """
        self.history.to_csv(filename, index=False)

    def load_history(self, filename: str = "logs/history.csv"):
        """
        Load calculation history from a CSV file.
        """
        self.history = pd.read_csv(filename)

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history = pd.DataFrame(columns=["timestamp", "operation", "expression", "result"])

    def get_history(self):
        """
        Retrieve the current calculation history.
        
        Returns:
            DataFrame: The history of calculations.
        """
        return self.history
