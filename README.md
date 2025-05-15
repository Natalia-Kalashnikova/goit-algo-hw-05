# Python Mini Tasks

## This repository contains small but practical Python tasks designed to improve your skills in file parsing, data manipulation, and real-world problem solving. Each task includes a clearly defined function and its use case in a business or practical scenario.

---

## Task 01 – Fibonacci Sequence with Caching

**Function:** `caching_fibonacci()`

Implement a function `caching_fibonacci()` that creates and returns a `fibonacci(n)` function which calculates the n-th Fibonacci number using recursion with caching.

The inner `fibonacci(n)` function:

- Returns 0 if `n` is less than or equal to 0
- Returns 1 if `n` equals 1
- Checks if value is already cached:
  - If yes, returns it directly
  - If no, computes recursively as `fibonacci(n-1) + fibonacci(n-2)`, stores in cache, and returns the result

This implementation uses memoization to optimize recursive computation, greatly reducing redundant calculations.

---

## Task 02 – Sum Valid Floats from Text

**Function:** `generator_numbers(), sum_profit()`

Implement `generator_numbers()` to extract valid float numbers from a string using regex. Floats must be clearly surrounded by spaces. Use `yield` to return numbers as a generator.

Implement `sum_profit()` to calculate the total sum of floats from the generator.

---

## Task 03 – Log File Analyzer with Level Filtering

**Functions:** `parse_log_line(line: str) -> dict, load_logs(file_path: str) -> list,
filter_logs_by_level(logs: list, level: str) -> list, count_logs_by_level(logs: list) -> dict,
display_log_counts(counts: dict)`

Create a Python script that reads a log file passed as a command-line argument and analyzes it by log levels (INFO, ERROR, DEBUG, WARNING).

- Implement `parse_log_line(line: str) -> dict` to parse a single log line into a dictionary with keys: date, time, level, and message.

- Implement `load_logs(file_path: str) -> list` to load and parse all log lines from a given file.

- Implement `filter_logs_by_level(logs: list, level: str) -> list` to filter logs by a specified log level.

- Implement `count_logs_by_level(logs: list) -> dict` to count the number of log entries per log level.

- Implement `display_log_counts(counts: dict)` to display counts in a formatted table.

The script also supports an optional second argument for filtering logs by level and handles errors such as missing files or invalid formats gracefully.

---

## Task 04 – CLI Contact Assistant Bot

**Function:** `main(), parse_input(), add_contact(), change_contact(), show_phone(), show_all_contacts()`

Developed a command-line interface (CLI) assistant bot that processes text commands entered via keyboard and responds accordingly. The assistant stores contact names and phone numbers, allows updating and retrieving contacts, and displays all saved entries. A Python dictionary is used to manage the contacts, with names as keys and phone numbers as values. The bot continuously processes user input until the **"exit"** or **"close"** command is received. Input is case-insensitive, and the program handles incorrect commands with appropriate messages.

To ensure centralized and consistent error handling, a dedicated decorator input_error is implemented. This decorator intercepts common exceptions (`ValueError, IndexError, and KeyError`) raised within command handler functions and returns informative messages to the user without interrupting the program flow.

---
