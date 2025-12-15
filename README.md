# Custom CSV Reader and Writer in Python

## Overview
This project implements a custom CSV (Comma-Separated Values) reader and writer from scratch in Python, without relying on Python’s built-in `csv` module for parsing or serialization.

The objective is to understand low-level CSV mechanics such as quoted fields, escaped double quotes, embedded newlines, streaming file I/O, and performance benchmarking.

## Testing & Validation

- Verified correctness by comparing output with Python's built-in `csv.reader`.
- Tested handling of:
  - Quoted fields
  - Escaped quotes (`""`)
  - Fields containing commas
  - Fields containing newlines
- Confirmed that CSV files written by `CustomCsvWriter` are readable by the standard csv module.
- Benchmarked performance using `timeit` on a dataset of 10,000 rows.
