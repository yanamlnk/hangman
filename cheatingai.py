def isVowel(char):
    return char.lower() in "aeiou"

def getSuggestedChar(secretWord, word):
    for i, c in enumerate(word):
        if isVowel(c) and secretWord[i] == "_":
            return c
        
    for i, c in enumerate(word):
        if secretWord[i] == "_":
            return c    

def printGuess(secretWord, word):
    if secretWord.count("_") == 2 and len(word) > 5:
        return f"(Suggested word: {word})"
    elif secretWord.count("_") == 1 and len(word) <= 5:
        return f"(Suggested word: {word})"
    else:
        return f"(Suggested letter: {getSuggestedChar(secretWord, word).upper()})"
    
