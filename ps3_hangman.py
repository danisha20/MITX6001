# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for letter in secretWord:
      if letter in lettersGuessed:
        count += 1 
    if count == len(secretWord):
      return True
    else: 
      return False
  

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ''
    lowerGuessed= [i.lower() for i in lettersGuessed]
    for letter in secretWord:
      if letter in lowerGuessed:
        guessed = guessed + letter
      else: 
        guessed += '_ '
    return guessed.lower()

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = string.ascii_lowercase
    unguessed = ''
    
    for letter in available: 
      if letter not in lettersGuessed: 
        unguessed = unguessed + letter
    return unguessed
  
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    
    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersLeft = []
    lettersinSecret = len(secretWord)
    Guessed = []
    gameOver = False
    guessesRemaining = 8
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a world that is ' + str(lettersinSecret) + ' letters long.')
    print ('-----------')
    
    while gameOver == False:
      lettersLeft = getAvailableLetters(Guessed)
      print('You have ' + str(guessesRemaining) + ' guesses left.')
      print('Available letters: ' + lettersLeft)

      user_guess = (input('Please guess a letter: ')).lower()
      if user_guess in Guessed: 
        print('Oops! You have already guessed that letter.')
      elif user_guess not in Guessed:
        Guessed.append(user_guess)
      
      
      gameOver = isWordGuessed(secretWord,Guessed)
        
      if gameOver == True: 
        display = getGuessedWord(secretWord,Guessed)
        print('Well done: ' + display)
        print('-----------')
        print('Congratulations, you won!')
        break
      elif user_guess in secretWord:
        display = getGuessedWord(secretWord,Guessed)
        print('Good guess: ' + display)
        print('-----------')
      elif user_guess not in secretWord:
        if guessesRemaining > 1: 
          guessesRemaining -= 1
          display = getGuessedWord(secretWord,Guessed)
          print('Oops! That letter is not in my word: ' + display)
          print('-----------')
        else: 
          display = getGuessedWord(secretWord,Guessed)
          print('Oops! That letter is not in my word: ' + display)
          print('-----------')
          print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
          break
          
secretWord = chooseWord(wordlist)
hangman(secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
