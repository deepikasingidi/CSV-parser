from custom_csv import CustomCsvReader

with open("test.csv", "r", encoding="utf-8") as f:
    reader = CustomCsvReader(f)
    for row in reader:
        print(row)
