# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "/Users/dannygc/Documents/Documents/MCC/MCCi2/Python/Exercises/6001x/Week6/PS6/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print ("  ", len(wordList), "words loaded.")
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("/Users/dannygc/Documents/Documents/MCC/MCCi2/Python/Exercises/6001x/Week6/PS6/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
import string
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.

    caesar = {}
    for letter in string.ascii_uppercase:
        id = string.ascii_uppercase.index(letter)
        if (id + shift) > 22: 
            id = id - 26
        other = id + shift
        newLetter = string.ascii_uppercase[other]
        caesar[letter] = newLetter
    for letter in string.ascii_lowercase:
        id = string.ascii_lowercase.index(letter)
        if (id + shift) > 22: 
            id = id - 26
        other = id + shift
        newLetter = string.ascii_lowercase[other]
        caesar[letter] = newLetter
    return caesar

# a shorter way 
    '''
    u = string.ascii_uppercase
    l = string.ascii_lowercase
    du = dict(zip(u ,(u[shift:26]+ u[0:shift])))
    dl = dict(zip(l, (l[shift:26]+ l[0:shift])))
    res = dict(du, **dl)
    return res 
    '''
def applyCoder(text,coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    encript = ''
    for i in text: 
        if i in coder.keys(): 
            encript += coder[i]
        else: 
            encript += i
    return encript

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    dict = buildCoder(shift)
    res = ''
    for i in text: 
        if i in dict.keys():
            res += dict[i]
        else:
            res += i
    return res
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    #1Start with base case, shifting 0
    shift = 0
    #2Set the maximum number of real words found to 0. 
    realWords = 0
    #3Set the number of validWords to 0 
    validWords = 0
    #4For each possible shift from 0 to 26.
    for shifts in range(0,26):
        #5Shift the entire text by this shift
        shiftText = applyShift(text,shift)
        #6Split the text up into a list of words
        listOfWords = shiftText.split(' ')
        #7Count every valid word in the list:
        for word in listOfWords :
            if isWord(wordList,word):
                validWords += 1
        #8If the number of valid words is bigger than the number of realWords found
        if validWords > realWords:
            #9Record the number of valid words
            realWords = validWords
            validWords = 0
            #10Set the best shift to the current shift
            bestShift = shift
        shift += 1
    return bestShift


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    story = getStoryString()
    bestShift = findBestShift(wordList,story)
    print(bestShift)
    return applyShift(story,bestShift)
        
    
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print(decryptStory())
