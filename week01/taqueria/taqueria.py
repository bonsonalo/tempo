# In a file called taqueria.py, implement a program that enables a user to place an order, 
# prompting them for items, one per line, until the user inputs control-d (which is a common 
# way of ending one’s input to a program). After each inputted item, display the total cost 
# of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal 
# places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume 
# that every item on the menu will be titlecased.


#rule 1: prompts(title cased)(2 decimal place) a user in while loop
#rule 2: display the total cost as inputted key and ignore if not in the dict
#rule 3: 


costs = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.0
while True:
    try:
        food = input("Food: ").title()
        if food in costs:
            total_cost += costs[food]
            print(f"${total_cost:.2f}")
        else:
            continue
    except EOFError:
        print("Thanks")
        break

        
        
