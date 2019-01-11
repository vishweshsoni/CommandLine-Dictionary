# import Library
import json
import difflib
from difflib import get_close_matches

# loading the json data as python dictionary
data = json.load(open("dictionary.json"))


# function for retriving defination
def retrive_defination(word):
    # removing the case sensitivity from the program
    # making all to lowercase because data is in lowercase
    word = word.lower()
    # check for non-existing word
    # 1st elif: to make sure the program return the definition of word that starts with capital later(E.g: Newyork,Delhi,Texas)
    # 2nd elif: to make sure the program return the defination of acronyms(E.g: USA,NATA)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif action == "n":
            return "The word Doesn't exist yet."
        else:
            return "we done understand your entry.Appologies"

    else:
        return "The word Doesn't exist Please Double check it"


# input from the user
word_user = input("Enter a word: ")

print(retrive_defination(word_user))
