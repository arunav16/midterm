# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This midterm project is an advanced Python-based calculator application designed to showcase professional software development practices. The application features:

- **A Plugin-Based REPL Interface:**  
  A dynamic command-line interface (REPL) that loads command implementations as plugins. This allows for easy extension without modifying the core code.

- **Comprehensive Logging:**  
  Detailed logging is implemented using Python’s logging module (with lazy formatting) and can be configured via environment variables or a configuration file.

- **Dynamic Configuration:**  
  Environment variables are loaded via `python-dotenv`, enabling dynamic configuration of the application (e.g., logging levels, strategy selection).

- **Calculation History Management:**  
  Calculation history is maintained using Pandas. A Singleton/Facade pattern encapsulated in the HistoryManager module provides methods for adding, saving, loading, and clearing history.

- **Design Patterns Implemented:**  
  - **Command Pattern:** Each operation (add, subtract, multiply, divide, etc.) is implemented as a command class that adheres to a common interface.
  - **Factory Method / Strategy Pattern:** The Add command uses a factory to select between addition strategies (allowing for future alternative implementations).
  - **Singleton & Facade Pattern:** The HistoryManager is implemented as a Singleton that provides a simple interface to complex Pandas operations.


## Core Functionalities

- **Dynamic Plugin Loading:**  
  The App class scans the `app/plugins` directory using `pkgutil` and `importlib` to automatically discover and register command classes. This makes it easy to add new commands by simply creating a new plugin package.

- **REPL Interface:**  
  Users interact with the calculator through a command-line interface that processes commands such as:
  - `greet` – Returns a greeting.
  - `add 5 3` – Adds two numbers using a strategy chosen by a factory.
  - `subtract 10 2`, `multiply 4 5`, `divide 20 4` – Perform corresponding arithmetic operations.
  - `exit` – Terminates the application.
  - `goodbye` – Returns a farewell message.
  - *Plus, additional commands as needed.*

- **Calculation History:**  
  Every arithmetic operation is recorded in a Pandas DataFrame via the HistoryManager. Users can later save, load, or clear the calculation history.

## Design Patterns Used

- **Command Pattern:**  
  Each command is encapsulated in its own class (e.g., `GreetCommand`, `AddCommand`, etc.) that implements a common interface (`Command`). The `CommandHandler` dispatches these commands based on user input.

- **Factory Method / Strategy Pattern:**  
  The Add command uses a factory (`addition_strategy_factory`) to select between different addition strategies. This pattern facilitates future enhancements and alternative implementations.

- **Singleton & Facade Pattern:**  
  The `HistoryManager` is implemented as a Singleton, ensuring a single point of access to calculation history. It also acts as a Facade over Pandas, providing simple methods for recording and retrieving history.

## Logging and Environment Configuration

- **Logging:**  
  Logging is configured via a configuration file (`logging.conf`) if available; otherwise, a basic configuration is used. Log messages are recorded with appropriate severity levels (DEBUG, INFO, ERROR).

- **Environment Variables:**  
  The application loads environment variables using `python-dotenv`, allowing dynamic configuration (e.g., selection of an alternative addition strategy).

## Usage

1. **Setup and Installation:**
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Application:**
   ```bash
   python3 main.py
   ```

## Video Demonstration

Watch the project presentation video on YouTube [here](https://youtu.be/fADksMO8x5w).
