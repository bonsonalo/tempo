""" In a file called pizza.py, implement a program that expects exactly one 
command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at 
pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified 
file’s name does not end in .csv, or if the specified file does not exist, the program 
should instead exit via sys.exit. """

import sys
import os
import argparse
from tabulate import tabulate
import csv
import logging


logging.basicConfig(filename="pizza.log",
                    filemode= "a",
                    level = logging.INFO,
                    format = "%(asctime)s %(levelname)s-%(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S")

def main():
    parser = argparse.ArgumentParser("To show the contents in a grid format")
    parser.add_argument(
        "filename",
        help="Path to the csv file"
    )
    args = parser.parse_args()
    logging.info("Parsed the CLI file")

    if not args.filename.endswith(".csv"):
        logging.error("Only csv file allowed")
        sys.exit("Only csv file allowed")
    elif not os.path.isfile(args.filename):
        logging.error(f"Error: {args.filename} could not be found")
        sys.exit(f"Error: {args.filename} could not be found")

    show = display(args.filename)
    print(show)

def display(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        row = list(reader)
        return tabulate(row, headers="keys",tablefmt="grid")
    logging.info("Read and formatted the file by grid")

if __name__ == "__main__":
    main()