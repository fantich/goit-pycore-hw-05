import sys
import re

def parse_log_line(line: str) -> dict:
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
    match = re.match(pattern, line)
    if match:
        return {"date": match.group(1), "time": match.group(2), "level": match.group(3), "message": match.group(4)}
    return None

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in sorted(counts.items()):
        print(f"{level.ljust(16)} | {count}")

def display_filtered_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_filtered_logs(filtered_logs, level_filter)

if __name__ == "__main__":
    main()