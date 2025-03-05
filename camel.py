"""
# In a file called camel.py, implement a program that prompts the user for the name of a
# variable in camel case and outputs the corresponding name in snake case. Assume that the 
# user’s input will indeed be in camel case.

def camel_to_snake(camel_case_str):

    

    
    # we assign the snake_case to "" first
    snake_case = ""

    for char in camel_case_str:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

# prompt the user to answer the question

my_prompt = input("what is the name of the variable? ")

print(camel_to_snake(my_prompt))

"""

# In a file called camel.py, implement a program that prompts the user for the name of a
# variable in camel case and outputs the corresponding name in snake case. Assume that the 
# user’s input will indeed be in camel case.

# prompt for question

"""
question =  input("what is the variable: ")

def camel_to_snake(camel_case):
    snake_case = ""       # we start with snake_case as ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    
    return snake_case


print(camel_to_snake(question))


"""




""""
#using while loop
i = 0
while i <  3:
    print("Miaw")
    i += 1 
    """
"""
# for loop
for i in range(3):
    print("meow")
"""
"""
print("meow\n" * 3, end= "")
"""

"""
#using while loop with for loop!


while True:
    n = int(input("what is n?  "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

"""
"""
#using while loop with for loop with FUNCTION!
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")

main()

"""

"""
# loops: list
students =["niny", "hary", "bo"]

for i in range(len(students)):
    print(i + 1, students[i])
    """

"""
# loop: dictionary

# below, if there are different catagories,
# we put coma after } and open another ditionary  
# which is {. 
# But we should include all dictionaries{} in list[]
students = {
    "he": "g",
    "ha": "g",
    "ron": "g",
    "dr": "s",
} 

# in dictionary as opposed to in using list, we have 
# to name the actual name of the word we want to get. eg: ["he"]
#print(students["he"])

for student in students:
    print(student, students[student], sep = ": ") 

    """


"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)


main()
"""
"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end = "")
        print()

main()
"""

"""
               #OR
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)
            

main()
"""

# print("meow\n" * 3, end="")



"""
user= input("What is in camel case? ") 

def pp(Ask):
    snake = ""
    for char in Ask:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


pp(user)

"""

"""



             # Assignments for Loop section




               ASSIBNMENT FOR CAMEL CASE TO SNAKE CASE
question = input("what is your varibale: ")

def camel_to_snake(camel):
    snake = ""
    lst=[]
    for char in camel: 
        lst.append(char)
    if lst[0].isupper():
            snake+=lst[0]
    else:
        snake += lst[0]
    for i in range(1, len(lst)):
        
        if lst[i].isupper():
            snake += "_" + lst[i].lower()
        else:
            snake += lst[i]
    print(snake)

camel_to_snake(question)

"""

"""
def coke():
    total = 0
    while total < 50:
        response = int(input("insert the coin: "))
        if response not in [5, 25, 10]:
            print("please insert valid number")
            continue
        total += response

        if total < 50:
            due = 50 - total
            print(f"Amount Due: {due}")
        elif total >= 50:
            owe = total - 50
            print(f"amount owed: {owe} ")
            break
coke()

"""
"""
   # twttr project
def twitter():
    ask = input("give a string: ")
    for char in ask:
        if char not in ["a", "e", "i", "o", "u"]:
            print(char, end="")
        else:
            print("", end="")
    print(f)

twitter()

"""



     #  Plates assignment
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # rule 1: must start with at least two letters
    if not s[0: 2].isalpha():
        return False
    # rule 2: contain a maximum of 6 characters and minimum 2 char
    if not (2 <= len(s) <= 6):
        return False
    # rule 3: 
        # Numbers cannot be used in the middle of a plate; 
        # they must come at the end.
        # The first number used cannot be a ‘0’.”
        # No periods, spaces, or punctuation marks are allowed.
    is_num = False
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            is_num = True
            count += 1
        # The first number used cannot be a ‘0’.”
        if count == 1 and s[i] == "0":
            return False
        # Numbers cannot be used in the middle of a plate; 
        elif count > 0 and s[i].isalpha():
            return False
        # No periods, spaces, or punctuation marks are allowed.
        if not s[i].isalnum():
            return False
    return True




main()

"""

                  #  EXCEPTION

"""
while True:
    try:
        x = int(input("what is x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
"""

"""
#           better way of saying the above code
def main():
    x = get_int("What is x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            

main()

"""
"""
       # Exception problem set 3

    # Fuel Gauge

#rule 1: prompts the user for a fraction(x/y)
# I will use while loop to keep prompting if the input is not the desired input.
# try else statement helps us to try the things thatg we want but at the same
# time to catch any error that maight come up upfront

while True:
    try:
        # prompt the user
        response = input("Fraction: ")


        # rule 2: each of X and Y is an integer
        x, y = response.split("/")
        x = int(x)
        y = int(y)


        # rule 3: outputs, as a percentage rounded to the nearest integer
        def conv_to_perc(x, y):
            return round((x / y) * 100)

        percentage = conv_to_perc(x, y)

        # to reprompt when x > y

        if x > y:
            continue

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break   # to tell the code to get out of the loop if the above inputs are inputed

    except ValueError:
        # if there is value error, it will print the below and reprompt hthe questkion
        print("please only insert integer number")
        continue       # to tell the code to keep the loop going( to reprompt)
    except ZeroDivisionError:
        pass   # to tell the code to reprompt but here i didnt specifically printed anything in return it will just reprompt without a reply from the code

"""


                      # Libraries

import random # this imports all the things in the random module
"""from random import choice"""  # this imports only the choice function


"""
coin = random.choice(["heads", "tails"])   # the comma says that there are 2 choices and the [] says that they are a list. and the {} belong to the choice function. if we use "from random import choice", we ommit the random that we use in this line before choice.
print(coin)
"""


        # random.randint(a, b)
""" 
number = random.randint(1, 10)  # this one gets you random integer between the range 1 and 10 . IT INCLUDES 1 AND 10
print(number)
"""
      # random.shuffle(x)
"""
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
"""

      # statistics
"""
import statistics

print(statistics.mean([100, 90]))
"""
     # sys
import sys

# sys.argv   argument Vector- the list of all of the word that the human typed in before hitting enter

if len(sys.argv) < 2:
    sys.exit("too few arguments") # sys.exit allows to exit if it meets the condition. unleass it will also run the below code while maintaining  this condition leading to index error
for arg in sys.argv[1:]: # here what i did is introduced "Slice"-is a list of data structure like a list. so [1:] means starts from the 1st element or index and continues till the end. that's why after colon there was no number
    print("hello, my name is", sys.argv[1]) # then when I run the code I should write personally on the terminal and say the name I want also in the terminal since this is comman line prompt. the [1] indicates it is the 1st index. so the name of the file is index 0 then the name we write next is index 1


      # package - is a module hat is implemented in folder but not file
                # is a 3rd party library that we can install in our pc to access what other peopl eimplemented for us


     # PyPI - python package index
     #cowsay
     #pip- allow to install packages on your pc
     #API- application Programming Interface- helps get information mostly from third party libraries
     #JSON- language agnostic data exchanging between computers
"""
import requests # installed using pip
import sys
if len(sys.argv) != 2:
. . . . sys. exit ()
response = requests. get ("https: //itunes. apple. com/search?entity=song&limit=1&term=" + sys. argv []
print ( response. json ( ) )
"""

"""
import json # so this json is added in this one
import requests
import sys # to access command line argument
if len(sys.argv) != 2:
. . . . sys. exit ()
response = requests.get ("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv|
o = response. json ()
for result in o["results"] :
12 . . . . print (result ["trackName"] )
"""
"""
. . . . goodbye ("world")
6 def hello(name) :
. . . . print ( f"hello, {name}")
10 def goodbye(name) :
. . . . print(f"goodbye, {name}")
14 if__name__== " __main__ ":  # this means if taken as a library for other file. this wont run. unless we want to run this file
. . . . main()
"""