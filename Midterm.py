from random import seed
from random import radint
seed (1)
wordlist = ["Pseudonym", "Sunshine", "Bicycle", "Serendipity", "Tornado", "Raspberry", "Harmony", "Fragrance", "Telescope", "Chocolate", "Adventure"]
def hangman (word):
    wordl = list(word)
    a = 0
    wrong = 0
    dash = []
    lenw = len(word)
    while a != (len(word)-1):
        a = a+1
        for a in range(lenw):
            dash.append("_")
    print (dash)
    while dash != wordl:
        answer = input("What's your first guess? ")
        wordf = word.find(answer)
        if wordf != -1:
            dash[wordf] = answer
            del word[wordf]
            while wordf != 1:
                dash[wordf] = answer
                del word[wordf]
        else:
            wrong = wrong + 1
            if wrong == 7:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
                print("  /\ ")
                print ("You lose!!!!")
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
        print(dash)
    print ("Congrats")
hangman (wordlist[randint(0,9)])
