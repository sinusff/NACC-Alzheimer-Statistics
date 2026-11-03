import os

data_dir = "data"

for filename in ["mriscanclean.csv", "udslong_imputed.csv"]:
    filepath = os.path.join(data_dir, filename)
    if not os.path.exists(filepath):
        filepath = os.path.join("..", data_dir, filename)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        line_count = sum(1 for _ in f)

    print(f"File: {filename}")
    print(f"  Total lines: {line_count}")
    print(f"  Data rows: {line_count - 1}\n")