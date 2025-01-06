#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, 
#outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


def main():
    ask = input("Great Question of Life, the Universe and Everything?").strip().lower()
    if ask == "42":
        print ("Yes")
    elif ask == "forty-two":
        print ("Yes")
    elif ask == "forty two":
        print("Yes")
    else:
        print ("No")
    

main()



