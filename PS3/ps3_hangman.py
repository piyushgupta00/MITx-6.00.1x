# Hangman game


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)





def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag=1
    for char in secretWord:
       if char in lettersGuessed:
         continue
       else: 
         flag=0
         return False
    if flag==1:
      return True
       
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    part_guess_word=[]
    for char in secretWord:
      if char in lettersGuessed:
        part_guess_word.append(char)
        part_guess_word.append(' ')
      else:
        part_guess_word.append(' _ ')
    return ''.join(part_guess_word)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabetlist=list(alphabet)
    donecheck=len(lettersGuessed)
    i=0
    donecount=0
    
    while donecount<donecheck:
      if alphabetlist[i] in lettersGuessed:
        char=alphabetlist[i]
        alphabetlist.remove(char)
        donecount+=1
        
      else:
       i+=1
       continue
    return ''.join(alphabetlist)


#THE FINAL CORE CODE HERE...
wordlist = loadWords()    

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
    #secretWord=chooseWord(wordlist)
    print("welcome to the Hangman Game!!")
    print("i'm thinking about a ",len(secretWord)," letter long word!!")
    print("you are allowed to make only one guess(letter) per round\n")
    
    #loop starts here for a total guess count of 8
    letter_guessed=[]
    guessleft=8
    flag=0
    validguesses='abcdefghijklmnopqrstuvwxyz'

    while guessleft!=0:
      
      print("you have", guessleft, "guesses left")
      print("Available letters: ",getAvailableLetters(letter_guessed))


      user_guess=input("Please guess a letter: ")
      if user_guess not in validguesses:
        print("invalid guess, please try again!!")
        print("_ _ _ _ _ _ _ \n")
        continue
      if user_guess in letter_guessed:
        print("oops you have already guessed that letter.",getGuessedWord(secretWord,letter_guessed))
        print("_ _ _ _ _ _ _ \n")
        continue
      letter_guessed.append(user_guess)
      
      if user_guess in secretWord:
        print("correct guess!!",getGuessedWord(secretWord,letter_guessed))
        print("_ _ _ _ _ _ _ \n")
        
        if isWordGuessed(secretWord,letter_guessed)==True:
          print("Congratulations!! you have won..")
          flag=1
          break
        continue
      
      
      
      else:
        print("Sorry! that letter is not in my word..",getGuessedWord(secretWord,letter_guessed))
        print("_ _ _ _ _ _ _ \n")
        guessleft=guessleft-1
        continue

    if flag==0:
      print("All guesses exhaused! You lose")
      print("the secret word was", secretWord)
    



#Running the hangman game with a secret word chosen randomly
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

