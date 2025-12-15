from custom_csv import CustomCsvWriter

data = [
    ["name", "age", "comment"],
    ["Alice", 23, 'Hello, "world"'],
    ["Bob", 30, "Line1\nLine2"],
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = CustomCsvWriter(f)
    writer.writerows(data)
