from random import seed
from random import randint

seed(1)

wordlist = ["pseudonym", "sunshine", "bicycle", "serendipity", "tornado", "raspberry", "harmony", "fragrance", "telescope", "chocolate", "adventure"]
randword = wordlist[randint(0,9)]
randword2 = wordlist[randint(0,9)]

def hangman(word):
    print(word)
    wordl = list(word)
    a = 0
    wrong = 0
    wordg = word
    dash = []
    lenw = len(word)
    
    for _ in range(lenw):
        dash.append("_")
    
    print(dash)
    
    while dash != wordl:
        guess = input("What's your guess? ")
        wordf = word.find(guess)
        
        if wordf != -1:
            dash[wordf] = guess
            wordg = wordg.replace(guess, "-", 1)
            print(wordg)
            
            while wordg.find(guess) != -1:
                wordf = wordg.find(guess)
                dash[wordf] = guess
                wordg = wordg.replace(guess, "-", 1)
                print(wordg)
            
            print(dash)
        else:
            wrong = wrong + 1
            if wrong == 7:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
                print("  /\ ")
                print("You lose!!!!")
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
    print("Congrats, the word was", randword, "!!!")
    hangman (randword2)
hangman(randword)
