from random import seed
from random import randint

seed(1)

wordlist = ["Pseudonym", "Sunshine", "Bicycle", "Serendipity", "Tornado", "Raspberry", "Harmony", "Fragrance", "Telescope", "Chocolate", "Adventure"]

def hangman(word):
    word = word.lower()  # Convert the word to lowercase
    wordl = list(word)
    a = 0
    wrong = 0
    dash = ["_"] * len(word)
    print(dash)
    while "_" in dash:
        answer = input("What's your guess? ").lower()  # Convert the user input to lowercase
        if len(answer) != 1:
            print("Please enter only one letter.")
            continue
        if answer in word:
            for i, letter in enumerate(word):
                if letter == answer:
                    dash[i] = answer
            print(dash)
        else:
            wrong += 1
            if wrong == 7:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
                print("  /\ ")
                print("You lose!!!!")
                break
            elif wrong == 6:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
                print("  /\ ")
            elif wrong == 5:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
            elif wrong == 4:
                print("  O  ")
                print(" /|\ ")
            elif wrong == 3:
                print("  O  ")
                print("  |\ ")
            elif wrong == 2:
                print("  O  ")
                print("  | ")
            elif wrong == 1:
                print("  O  ")
    print("Congrats")

hangman(wordlist[randint(0,9)])
