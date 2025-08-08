# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. Once the user has inputted at least 50 cents, output 
# how many cents in change the user is owed. Assume that the user will only input integers, and ignore any 
# integer that isn’t an accepted denomination.


valid_coins = [25, 10, 5]
cost = 50
total = 0

while True:
    try:
        ask = int(input("Insert a coin: "))
        if ask not in valid_coins:
            continue
        else:
            total += ask
        if total < cost:
            diff = cost - total
            print(f"The amount due: {diff}")
        elif total == cost:
            print("Thank you")
            break
        elif total > cost:
            diff = total - cost   
            print(f"Amount owed: {diff}")
            break
    except ValueError:
        print("Input numbers in ", valid_coins)
        continue


    

            



# prompt the user
# inform the amount due
# loop
