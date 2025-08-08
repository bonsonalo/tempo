# When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
# as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, 
# implement a program that prompts the user for a str of text and then outputs that same text but 
# with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    ask = input("Input a string: ")
    output = convert(ask)
    print(output)

def convert(text):
    to_be_removed = ["a", "e", "i", "o", "u"]
    # final = ""
    # for i in text:
    #     if i.lower() not in to_be_removed:
    #         final += i

    return "".join(i for i in text if i.lower() not in to_be_removed )
        
    # return final

main()



