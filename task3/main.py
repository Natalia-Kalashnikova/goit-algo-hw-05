import sys
from collections import defaultdict
from typing import List, Dict


def parse_log_line(line: str) -> dict:
    """
    Parse a single line from the log file into components: date, time, level, and message.

    Args:
        line (str): A single log line in the format 'YYYY-MM-DD HH:MM:SS LEVEL Message'

    Returns:
        dict: A dictionary with keys: 'date', 'time', 'level', 'message'
              or an empty dict if the line format is invalid.
    """
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        raise ValueError(f"Invalid log line format: {line}")
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3]
    }


def load_logs(file_path: str) -> List[dict]:
    """
     Load and parse all lines from the log file.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list: A list of parsed log entries (dictionaries).
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Filter logs by a specific logging level.

    Args:
        logs (list): List of parsed log entries.
        level (str): Logging level to filter by (e.g. 'ERROR', 'INFO').

    Returns:
        list: Filtered list of logs matching the specified level.
    """
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Count the number of log entries per log level.

    Args:
        logs (list): List of parsed log entries.

    Returns:
        dict: Dictionary mapping log levels to their occurrence count.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Display log level statistics in a formatted table.

    Args:
        counts (dict): Dictionary with log level counts.
    """
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts.keys()):
        print(f"{level:<17}| {counts[level]}")


def display_logs(logs: List[dict], level: str) -> None:
    """
    Display detailed log messages for a given level.

    Args:
        logs (List[dict]): Filtered list of logs.
        level (str): Log level to display.
    """
    if logs:
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"\n⚠️ Немає записів для рівня '{level.upper()}'.")


def main():
    if len(sys.argv) < 2:
        print("❗ Приклад використання: python main.py path/to/logfile.txt [level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        display_logs(filtered, level)


if __name__ == "__main__":
    main()