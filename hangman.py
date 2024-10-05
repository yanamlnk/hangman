import random
import time
import argparse
from cheatingai import printGuess
from hangmanicon import getHangmanIcon

easy = ["apple", "tree", "bird", "coin", "stone", "water", 
        "light", "desk", "cup", "hand", "sky", "book", "fish", 
        "grape", "chair", "sand", "star", "leaf", "rain", "pen"]

medium = ["computer", "library", "horizon", "mountain", "elephant",
        "picture", "balloon", "keyboard", "sunshine", "holiday", 
        "bicycle", "village", "journey", "diamond", "notebook", 
        "festival", "treasure", "airplane", "mystery", "friendship"]

hard = ["concentration", "imagination", "infrastructure", "unbelievable", 
        "communication", "relationship", "circumference", "contribution", 
        "international", "accommodation", "determination", "entertainment", 
        "comprehensive", "mathematical", "extraordinary", "transmission", 
        "celebration", "responsibility", "optimization", "understanding"]

levels = [easy, medium, hard]

parser = argparse.ArgumentParser(description="Run the Hangman game")
parser.add_argument(
    '-cheat',
    action='store_true',
    help='Enable cheat mode'
)

args = parser.parse_args()
cheatMode = False

if args.cheat:
    print("\nCheat mode is enabled.")
    cheatMode = True
else:
    print("\nRunning normal mode.")

def chooseWord(level):
    word = level[random.randint(0, 19)]
    return word

def makeSecretWord(word):
    return ["_" for _ in word]

def letterInWord(letter, word):
    if letter in word:
        return [index for index, char in enumerate(word) if char == letter]
    return [-1]    

def result(secretWord, letter, indexes):
    for i in indexes:
        secretWord[i] = letter.upper()
    return secretWord    

def generateString(secretWord):
    return " ".join(secretWord)  

def printRules():
    print("________________________________________________________________________________________________________________" +
        "\nThe objective is to guess a word (randomly picked from a list) and stay alive." + 
          "\nYou must suggest a letter at each turn." + 
          "\n\nIf the word contains this letter, all occurrences of the letter are revealed." +
          "\nIf the letter is not in the word, the you receive a mistake, and part of the hangman figure is drawn." +
          "\n\nAt any time, you can propose a full word. If the word is the one to be guessed, you win. Else, you get 2 mistakes." +
          "\n\nYou win if you can correctly guess all the letters in the word before the hangman figure is fully drawn." +
          "\nYou lose if you make too many incorrect guesses (10), and the full hangman figure is completed." +
          "\n________________________________________________________________________________________________________________")
    
    time.sleep(4)    

def interface():
    print("\nHello there, wanna play some Hangman?\n")
    print(" - - -")
    print("|     |")
    print("|    ( )")
    print("|    /|\\")
    print("|    / \\")
    print("|")
    print("\nPlease type a number of a difficulty level you want.")
    while(True):
        try:
            level = input("\n1. Easy\n2. Medium\n3. Hard\n0. Exit\n> ")
            levelInt = int(level)
            if levelInt == 0:
                print("Goodbye!")
                return 
            elif levelInt < 1 or levelInt > 3:
                print("We are a new game, and currently have only 3 levels. Please choose a level from 1 to 3.")   
            else:
                levelArray = levels[levelInt-1]
                randomWord = chooseWord(levelArray)
                break
        except ValueError as e:
            print("Your input should be a number from 1 to 3, please try again.")

        except EOFError as e:
            print("\nIf you want to exit, please type 0 or use Ctrl+C")

        except KeyboardInterrupt:
            print("\nGoodbye!")  
            return 

    print("\nDo you want to read the rules before you start?")

    while(True):
        try: 
            inputRules = input("\n1. Yes\n2. No\n0. Exit\n> ")
            if (inputRules == "2"):
                print("\nAs you wish!")
                time.sleep(1)
                break
            elif (inputRules == "1"):
                printRules()
                break
            elif inputRules == "0":
                print("Goodbye!")
                return     
            else:
                print("Well, you need to type just 1 or 2 as an answer, but since you didn't, I will give you the rules anyway! \n\n")
                printRules() 

        except EOFError:
            print("\nIf you want to exit, please type 0 or use Ctrl+C")

        except KeyboardInterrupt:
            print("\nGoodbye!")  
            return 

    print("\nGood luck!\n")

    mistakes = 0
    secretWordArray = makeSecretWord(randomWord)
    while(True):
        print(getHangmanIcon(mistakes))
        print(f"     {generateString(secretWordArray)}\n")

        if mistakes == 10:
            print("\nGame over X_X")
            break
        elif not "_" in secretWordArray:
            print("\nYou have guessed the word! Congrats!")
            break
       
        print("For exit, type 0 or use Ctrl+C")

        cheat = ""
        if cheatMode:
            cheat = printGuess(secretWordArray, randomWord)
        
        try:
            pInput = input(f"{cheat} > ")

            playerInput = pInput.lower()
        
            if playerInput == "0":
                print("Goodbye!")
                return
            elif len(playerInput) > 1:
                print("Looks like you are trying to guess the whole word. Let's see...\n")
                time.sleep(1)
                if playerInput == randomWord:
                    print(f"You have guessed the word! Congrats!")
                    break
                else:
                    mistakes += 2
            elif len(playerInput) == 0:
                print("\nYou need to type a letter or a whole word.\n")
            else:
                indexes = letterInWord(playerInput, randomWord)
                if indexes[0] == -1:
                    mistakes += 1
                else:
                    secretWordArray = result(secretWordArray, playerInput, indexes)

        except EOFError:
            print("\nIf you want to exit, please type 0 or use Ctrl+C")

        except KeyboardInterrupt:
            print("\nGoodbye!")  
            return 

interface()