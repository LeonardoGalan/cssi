chosenWord= "programming"

def initboard(word):
    temp =[]
    for i in (word):
        temp.append('_')
    return temp

def printBoard(board,guessList):
    print " ".join(board)
    print "Guesses: " + " ".join(guessList)

def addGuess(board,word,guess):
    for i in range(len(word)):
        if guess == word[i]:
            board[i] = guess
def game():
    chosenWord = "programming".lower()
    guesses = []
    board = initboard(chosenWord)

    while '_' in board:
        printBoard(board,guesses)
        guess = raw_input('enter a letter: ').lower()

        if len(guess) == 1:
            if guess in chosenWord:
                addGuess(board,chosenWord,guess)

            guesses.append(guess)
        else:
            print "sorry your guess has to be one letter"

    print "".join(board)
    print "Congrats you win nothing and completely wasted your time guessing"

game()
