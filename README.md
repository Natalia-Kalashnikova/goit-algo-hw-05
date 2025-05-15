# Python Mini Tasks

## This repository contains small but practical Python tasks designed to improve your skills in file parsing, data manipulation, and real-world problem solving. Each task includes a clearly defined function and its use case in a business or practical scenario.

## Task 04 – CLI Contact Assistant Bot

**Function:** `main(), parse_input(), add_contact(), change_contact(), show_phone(), show_all_contacts()`

Developed a command-line interface (CLI) assistant bot that processes text commands entered via keyboard and responds accordingly. The assistant stores contact names and phone numbers, allows updating and retrieving contacts, and displays all saved entries. A Python dictionary is used to manage the contacts, with names as keys and phone numbers as values. The bot continuously processes user input until the **"exit"** or **"close"** command is received. Input is case-insensitive, and the program handles incorrect commands with appropriate messages.

To ensure centralized and consistent error handling, a dedicated decorator input_error is implemented. This decorator intercepts common exceptions (`ValueError, IndexError, and KeyError`) raised within command handler functions and returns informative messages to the user without interrupting the program flow.

---
