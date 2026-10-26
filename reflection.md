# Lab 5: Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were formatting problems, such as long lines, multiple statements on one line, and inconsistent function names. These changes mainly involved improving readability and following Python conventions.

The harder issues were the SQL injection risk and adoption-count logic. Fixing them required understanding parameterized database queries and ensuring that the program updated its state only when an adoption was successful. Removing global state also required restructuring the code into a `Shelter` class.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Bandit warned about using `random.randint()` to generate adoption codes. Whether this is a false positive depends on how the codes are used. If the code is only a demonstration label, cryptographic unpredictability may not be necessary. If it is used in a security-sensitive workflow, predictability could be a genuine concern.

I replaced the standard `random` module with `secrets`, which is more appropriate when unpredictable codes are required. This demonstrates that static-analysis warnings should be evaluated in the context of the application's requirements rather than dismissed automatically.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would use Flake8 to check formatting and style, Pylint to identify maintainability and potential correctness issues, and Bandit to identify potential security weaknesses.

I would run these tools during development and before committing code. I would also integrate them into a continuous integration workflow so that issues can be detected before changes are merged. I would review warnings, fix valid findings, and rerun the tools to verify the results.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The corrected program uses parameterized SQL queries, reducing the risk of SQL injection. The mutable default argument and broad exception handling were removed. Adoption counts increase only when an available pet is successfully adopted.

The code now uses consistent naming, documentation, and formatting. Encapsulating the database and adoption counter in the `Shelter` class also makes the program easier to organize and maintain.

After the fixes, Pylint reported 10.00/10, Bandit reported no findings, and Flake8 reported no style violations. These results indicate improved code quality and address the issues identified during the original analysis.
