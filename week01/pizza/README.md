
# `pizza.py` – ASCII Grid Viewer for CSV Files

A Python CLI tool that reads a CSV file (in Pinocchio’s format) and outputs it as a beautifully formatted ASCII table using the `tabulate` library.

---

## Description

This script takes exactly one command-line argument — the path to a `.csv` file — and:

- Validates the file path and format.
- Reads the CSV file.
- Outputs a human-readable ASCII table (grid-style) in the terminal.
- Logs all major operations to `pizza.log`.

Perfect for inspecting data or demoing CSV contents without needing Excel or a GUI.

---

## Features

- Input validation (only `.csv` files accepted)
- Clean tabular output using [`tabulate`](https://pypi.org/project/tabulate/)
- Logging for traceability (`pizza.log`)
- Lightweight and CLI-friendly

---

## Prerequisites

- Python 3.6+
- [`tabulate`](https://pypi.org/project/tabulate/)

You can install it via pip:

```bash
pip install tabulate
```

---

## Installation & Setup

1. Clone the repo or copy the script:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

(Create `requirements.txt` with just one line: `tabulate`)

---

## Usage

```bash
python pizza.py path/to/yourfile.csv
```

Example:

```bash
python pizza.py menu.csv
```

If the file is valid, you'll see an ASCII table like:

```
+------------+----------+--------+
| Name       | Topping  | Price  |
+------------+----------+--------+
| Margherita | Cheese   | 8.5    |
| Pepperoni  | Meat     | 9.0    |
+------------+----------+--------+
```

If the file is invalid, you'll get a meaningful error and logs will be saved in `pizza.log`.

---

## Example CSV Format

```csv
Name,Topping,Price
Margherita,Cheese,8.5
Pepperoni,Meat,9.0
```

---

## Files

- `pizza.py` – main script
- `pizza.log` – log file (auto-generated)
- `requirements.txt` – dependencies

---

## Logging

All important operations (parsing, validation, errors) are logged to `pizza.log` for debugging and audit trails.

---

## Contribution

Feel free to fork this project, suggest improvements, or open issues.

---

## License

MIT – free to use, modify, and distribute.
