import csv
import timeit
from custom_csv import CustomCsvReader, CustomCsvWriter

ROWS = 10000
COLS = 5
FILE_NAME = "benchmark.csv"


def generate_csv():
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for i in range(ROWS):
            writer.writerow(
                [f'value {i},{j} "test"\nline' for j in range(COLS)]
            )


def benchmark_custom_reader():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = CustomCsvReader(f)
        for _ in reader:
            pass


def benchmark_csv_reader():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for _ in reader:
            pass


def benchmark_custom_writer():
    data = [[f"val {i},{j}\n" for j in range(COLS)] for i in range(ROWS)]
    with open("custom_out.csv", "w", encoding="utf-8", newline="") as f:
        writer = CustomCsvWriter(f)
        writer.writerows(data)


def benchmark_csv_writer():
    data = [[f"val {i},{j}\n" for j in range(COLS)] for i in range(ROWS)]
    with open("csv_out.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    generate_csv()

    print("Custom Reader:", timeit.timeit(benchmark_custom_reader, number=3))
    print("CSV Reader:", timeit.timeit(benchmark_csv_reader, number=3))
    print("Custom Writer:", timeit.timeit(benchmark_custom_writer, number=3))
    print("CSV Writer:", timeit.timeit(benchmark_csv_writer, number=3))
