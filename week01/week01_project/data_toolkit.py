""" 
You're building a clean, CLI-based data cleaning and 
summarization tool in Python, which takes in a CSV file, 
validates and cleans the data, summarizes it, and handles 
errors — all organized into functions and pushed to GitHub 
professionally.
 """
import sys
import os
import logging
import csv
import argparse
from tabulate import tabulate


"""Logging setup  """
logging.basicConfig(filename="data_toolkit.log",
                    filemode= "a",
                    level=logging.INFO,
                    format= "%(asctime)s %(levelname)s-%(message)s",
                    datefmt="%Y/%m/%d %H/%M/%S")
""" Main logic """
def main():
    parser = argparse.ArgumentParser(description="Cleans and outputs the cleaned csv in a grid format")
    parser.add_argument("filename",
                        help="Enter a .csv file")
    args = parser.parse_args()
    logging.info("Succesfully succeeded in using argparse")

    if not args.filename.endswith(".csv"):
        logging.error("Only .csv file is allowed")
        sys.exit("Only .csv file is allowed")
    if not os.path.isfile(args.filename):
        logging.error("the file doesn't exit")
        sys.exit("the file doesn't exit")

    cleaned_data = load(args.filename)
    display_table = display(cleaned_data)
    print(display_table)


""" Load and Clean CSV """
def load(file_path):
    """ It loads the csv file loaded and then clean the data then prepares the cleaned one in a list form """
    with open(file_path, "r") as file:
        reader = csv.DictReader(file) # dictreader assumes the headers to be the first rows in scv, and it stores it in a dict format
        rows = list(reader)  #Converted to list to store all rows for easier processing or inspection
        edited = []
        for row in rows: # meaning each row represents 1 dict inside
            cleaned_row = {} # Create a fresh container for cleaned key-value pairs per row
            for key in row:
                value = row[key]
                if value:            # if not value == None and not value == ""
                    cleaned_row[key] = value.strip()
            edited.append(cleaned_row)
        logging.info("Appended the cleaned dictionary to the empty list prepared(edited)")

    return edited
                
        
""" Display Cleaned table """
def display(data):
    logging.info("Successfully displayed")
    return tabulate(data, headers="keys", tablefmt="grid")
    
    



if __name__ == "__main__":
    main()