# in a file called lines.py, implement a program that expects 
# exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments 
# and blank lines. If the user does not specify exactly one command-line argument, 
# or if the specified file’s name does not end in .py, or if the specified file does 
# not exist, the program should instead exit via sys.exit.

import argparse
import sys
import os
import logging

logging.basicConfig(filename= "lines.log",
                    filemode= "a",
                    level= logging.INFO,
                    format= "%(asctime)s %(levelname)s-%(message)s",
                    datefmt= "%Y/%M/%d %H:%M:%S")


def main():
    """  
    Main entry point of the program.
    Validates the command-line argument and prints line count of the Python file. 

    """


    parser = argparse.ArgumentParser(description= "Count line of code in python file")

    parser.add_argument(
        "filename",
        help="Path to the Python (.py) file"
    )

    args = parser.parse_args()


    if not args.filename.endswith(".py"):
        logging.error("only python(.py) files are allowed")
        sys.exit("only python(.py) files are allowed")
    elif not os.path.isfile(args.filename):
        logging.error(f"Error: File {args.filename} not found")
        sys.exit(f"Error: File {args.filename} not found")
        

    count = count_lines(args.filename)
    logging.info(f"{args.filename} contains {count} lines of code.") # info was lower case because for logging in a message, we use info, but when setting in the logger we use INFO like in line 15



def count_lines(file_path):
    """ 
    counts the number of non-blank, non - comment lines in python file
    Arg: lines that are actual code(not comment or blank space)
        file_path(str): the path to python(.py) file
    Returns:
        int: the number of 
    """
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            elif stripped == "":
                continue
            count += 1
    return count



if __name__ == "__main__":
    main()





