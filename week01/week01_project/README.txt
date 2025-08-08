# Data Toolkit CLI

This is a command-line Python tool that reads a `.csv` file, cleans the data (removes whitespace and empty values), and displays the result in a neatly formatted grid using the `tabulate` library.

## Features

- Accepts a `.csv` file as input via command line
- Validates file format and existence
- Cleans the data by trimming whitespace and removing empty values
- Outputs the cleaned data in an ASCII grid table
- Includes proper logging for debugging and traceability
- Production-ready setup with:
  - Logging
  - Virtual Environment support
  - `requirements.txt`
  - `.gitignore`
  - README file

## Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

Dependencies include:
- tabulate

## Usage

```bash
python data_toolkit.py your_file.csv
```

Make sure to replace `your_file.csv` with the path to your actual CSV file.

## Logging

Logs are written to `data_toolkit.log` to help trace actions and errors.

## Example CSV

```csv
Name,Age,Location
Alice,30,New York
Bob,25,San Francisco
Charlie,,Los Angeles
```

## Output

```
+----------+-------+---------------+
| Name     | Age   | Location      |
+==========+=======+===============+
| Alice    | 30    | New York      |
| Bob      | 25    | San Francisco |
| Charlie  |       | Los Angeles   |
+----------+-------+---------------+
```

