from ps4a import *
import time

# Computer chooses a word

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        
        print("Current Hand: ", end=' ')
        displayHand(hand)
        
        word = compChooseWord(hand, wordList, n)
        
        if word == None:
            # End the game (break out of the loop)
            break
            
        
        else :
            
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            
            else :
                
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                
                hand = updateHand(hand, word)
                print()
    
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    print("Welcome to the Word Scramble Game 'You Vs Computer'!!!\n")
    previoushand={}
    gameplayedflag=0
    
    while True:
        prompt=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        if prompt not in 'ner':
          print("Invalid input, Please Try again")
          continue
        if prompt=='e':
          break
        if prompt=='n':
          gameplayedflag=1
          while True:
            whoplays_prompt=input("Enter u to have yourself play, c to have the computer play: ")
            if whoplays_prompt not in "uc":
              print("Invalid Entry,only u and c response allowed")
              continue
            else:
              break
          if whoplays_prompt=="u":
            hand=dealHand(HAND_SIZE)
            previoushand=hand.copy()
            playHand(hand,wordList,HAND_SIZE)
          elif whoplays_prompt=="c":
            hand=dealHand(HAND_SIZE)
            previoushand=hand.copy()
            compPlayHand(hand,wordList,HAND_SIZE)
          else:
            print("invalid Entry")
            continue

        if prompt=='r':
            if gameplayedflag==0:
              print("You have not played a hand yet. Please play a new hand first!")
              print()
              continue
            hand=previoushand
            while True:
              whoplays_prompt=input("Enter u to have yourself play, c to have the computer play: ")
              if whoplays_prompt not in "uc":
                print("Invalid Entry,only u and c response allowed")
                continue
              else:
                break
            if whoplays_prompt=="u":
                playHand(hand,wordList,HAND_SIZE)
            elif whoplays_prompt=="c":
                compPlayHand(hand,wordList,HAND_SIZE)

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


