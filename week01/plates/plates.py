# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an 
# acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of 
# the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure 
# your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
# Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one 
# function per requirement).



#rule 1: length
#rule 2: first 2 letters
#rule 3: numbers only in the last
#rule 4: no space, punctuation, period


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    idx = None
    for i in range(len(s)):
        if s[i].isdigit():
            idx = i
            break
    if idx is not None:
        if s[idx] == "0":
            return False
        if not s[idx:].isdigit():
            return False
    return True



main()










# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     mark = ""
#     #len from 2 untill 6
#     for i in s:
#         while len(s) in range(2, 7):
#     # must start with atleast 2 letter
#             if s[:2].isalpha():
#                 mark += i
#             elif i.isdigit() and i != 0:
#                 mark += i
#         if i.isalpha():
#             continue
            
#     #number not used in middle of letters
#     #number after 2nd letter cannot start with 0
#     # no period, spaace, punctuation allowed 


# main()

        
        
                