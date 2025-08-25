import logging
import csv
import os
from tabulate import tabulate
import argparse



logging.basicConfig(
    filename="data_toolkit.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s-%(message)s",
    datefmt="%Y/%m/%d %H/%M/%S"
)

class CSVLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        logging.info(f"CSVLoader initialized for {filename}")


    def validate_file(self):
        if not self.filename.lower().endswith(".csv"):
            logging.error("Only csv file allowed")
            raise ValueError("Only csv files allowed")
        if not os.path.isfile(self.filename):
            logging.error("File doesn't exist")
            raise FileNotFoundError(f"{self.filename} doesn't exist")
        try:
            with open(self.filename, "r") as f:
                f.read(1) # try reading 1 character
        except OSError as e:
            logging.error(f"File not readable: {e}")
            raise
        logging.info(f"Validated the file: {self.filename}")
        return True
    def load(self):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            final_list = []
            for row in rows:
                edited_dict = {}
                for key in row:
                    value = row[key]
                    if value:
                        edited_dict[key] = value.strip()
                final_list.append(edited_dict)
            logging.info("Appended the cleaned dictionary to the empty list prepared(final_list)")
        return final_list


class TableDisplayer:
    def __init__(self, data):
        self.data = data

    def display(self):
        return tabulate(self.data, headers="keys", tablefmt="grid")
    
class DataToolKit:
    def __init__(self, filename):
        self.filename = filename
    def run(self):
        loader = CSVLoader(self.filename)
        loader.validate_file()
        data = loader.load()
        

        displayer = TableDisplayer(data)
        print(displayer.display())





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "Cleans and displays CSV in table format")
    parser.add_argument("filename", help="enter a csv file")
    args = parser.parse_args()

    app= DataToolKit(args.filename)
    app.run()