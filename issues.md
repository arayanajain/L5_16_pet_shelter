# Lab 5: Static Code Analysis Issues

## 1. Original Code Analysis

The original `pet_shelter.py` was analyzed using Pylint, Bandit, and Flake8. The tools identified security, correctness, reliability, and maintainability issues.

| Issue | Severity | Original Code Location | Description | Fix Applied |
|---|---|---|---|---|
| Potential SQL injection | Medium | Line 10 | SQL queries were constructed using string formatting, allowing input values to alter the query. | Replaced string formatting with parameterized SQL queries using placeholders. |
| Mutable default argument | Correctness | Line 9 | The default `tags=[]` list could be shared across function calls, causing unexpected behavior. | Changed the default value to `None` and initialized a new list when needed. |
| Insecure random number generation | Low | Line 22 | `random.randint()` does not provide cryptographically secure unpredictability. | Replaced the `random` module with `secrets` for adoption code generation. |
| Bare exception handler | Reliability | Lines 27–30 | A bare `except` could suppress unexpected errors and make debugging difficult. | Removed the broad exception handler and handled an empty database query result explicitly. |
| Silently ignored exceptions | Reliability | Lines 33–37 | The program ignored database errors without reporting them. | Removed exception suppression so unexpected errors can be detected. |
| Incorrect adoption counter updates | Correctness | Lines 14–17 | The adoption count increased even when the requested pet was not successfully adopted. | Incremented the counter only when the database update affected an available pet. |
| Long lines and inconsistent formatting | Code quality | Multiple | Flake8 identified long lines and multiple statements on one line. | Reformatted SQL statements and conditional logic. |
| Naming and documentation issues | Maintainability | Multiple | Pylint identified non-standard function names and missing docstrings. | Applied `snake_case` naming and added documentation strings. |
| Global state | Maintainability | Lines 6, 15–17 | A global variable was used to track adoption counts. | Encapsulated the adoption counter within the `Shelter` class. |

## 2. Improvements After Fixing the Issues

The corrected implementation uses parameterized SQL queries, avoids mutable default arguments, and generates adoption codes using the `secrets` module. It updates the adoption counter only after a successful adoption and removes broad exception handling.

The code was reorganized into a `Shelter` class to encapsulate database operations and adoption state. Function names, docstrings, and formatting were also improved.

## 3. Final Static Analysis Results

- **Pylint:** 10.00/10
- **Bandit:** No findings reported.
- **Flake8:** No style violations reported.

These results were obtained after running the tools against the corrected `pet_shelter.py`.
