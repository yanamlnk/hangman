## Hangman

```
Hello there, wanna play some Hangman?

 - - -
|     |
|    ( )
|    /|\
|    / \
|
```

Well, everybody knows Hangman game, and it is exactly what it looks like. 

### Want to play it?
Oh, I am so happy! ❤️ 
- clone this repository with `git clone`
- go to the folder to which you cloned this project
- start game with command `python hangman.py`
- enjoy!

Make sure you have Python installed in your machine. Check by running `python --version` command. If you see a version - all set!

## Gameplay
My version of game is pretty small, but it does the job. It is CLI application. 

1. Choose difficulty level. **Easy** are at most 5 characters words, **medium** - up to 10 characters, and **hard** - more than 10 characters.
2. Next you have an option to read the rules. You can skip them if you want.
```
________________________________________________________________________________________________________________
The objective is to guess a word (randomly picked from a list) and stay alive.
You must suggest a letter at each turn.

If the word contains this letter, all occurrences of the letter are revealed.
If the letter is not in the word, the you receive a mistake, and part of the hangman figure is drawn.

At any time, you can propose a full word. If the word is the one to be guessed, you win. Else, you get 2 mistakes.

You win if you can correctly guess all the letters in the word before the hangman figure is fully drawn.
You lose if you make too many incorrect guesses (10), and the full hangman figure is completed.
________________________________________________________________________________________________________________
```
3. Now you can either type letter by letter, or try the full word.
4. You can always exit from the game by typing `0`, or with `Control + C` command.
5. Want to try cheating mode? 🤫 Start your game with additional option `-cheat`:
```
python hangman.py -cheat
```
6. Try not to loose! 🤞
```
     - - -
    |     |
    |   (x x)
    |    /|\
    |    / \
    |
```
