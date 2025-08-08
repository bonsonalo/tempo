# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs 
# the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


def main():
    mark = []
    ask = input("Input a string in camel case: ")
    for i in ask:
        if i.islower():
            mark+= i
        elif i.isupper():
            i = "_" + i
            mark+= i.lower()
    final_answer = "".join(mark)
    print(final_answer)

main()




