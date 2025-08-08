# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
# For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
#  and 3/4 indicates that a tank is 75% full.
#In a file called fuel.py, implement a program that prompts 
# the user for a fraction, formatted as X/Y, wherein each of X and Y 
# is a positive integer, and then outputs, as a percentage rounded to 
# the nearest integer, how much fuel is in the tank. If, though, 1% or 
# less remains, output E instead to indicate that the tank is essentially 
# empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, 
# instead prompt the user again. (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.




#rule 1: propmt
#rule 2: convert to percentage
import logging
logging.basicConfig(filename= "feullog.log",
                    filemode= "w",
                    level= logging.DEBUG,
                    format= "%(asctime)s %(levelname)s-%(message)s",
                    datefmt='%Y/%M/%d  %H:%M:%S')
def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percent = convert(fraction)
            print(gauge(percent))
            break
        except ValueError as e:
            logging.warning(f"problem: {e}")
        except ZeroDivisionError:
            logging.warning("Denominator can't be 0")

def convert(numbers):
    if "/" not in numbers:   # this line has to be before splitting by /. 
        raise ValueError("missing '/")
    x, y = numbers.split("/")
    x = int(x)
    y = int(y)
    divide = round(x / y * 100)
    return divide

def gauge(percents):
    if percents <=1:
        return "E"
    elif percents >=99:
        return "F"
    else:
        return f"{percents}%"


main()




# while True:
#     ask = input("Fraction: ") 
#     try:
#         x, y = ask.split("/") 
#         x = int(x)
#         y = int(y)
#         calc = round(x / y * 100)
#         if calc <=1:
#             print("E")
#         elif calc >=99:
#             print("F") 
#         else:
#             print(f"{calc}%")
#     except (ValueError):
#         print("enter integer value")
#     except(ZeroDivisionError):
#         print("denominator can't be 0")
#         continue
#     break

            

            
         
    
