# In a file called grocery.py, implement a program that prompts the user for items, 
# one per line, until the user inputs control-d (which is a common way of ending one’s 
# input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically 
# by item, prefixing each line with the number of times the user 
# inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.


# rule 1: prompt the user in a while loop, case insensitive
#rule 2: try except EOFError
# rule 3: after EOFError, print them all together in upper class
                            #alphabetically
                            # have the number of times inputed

collection = {}
while True:
    try:
        item = input("Enter: ").lower()
        if item in collection:
            collection[item] +=1
        else:
            collection[item] = 1
    except EOFError:
        print()
        for key in sorted(collection):
            print(f"{collection[key]} {key.upper()}")
            
        break


