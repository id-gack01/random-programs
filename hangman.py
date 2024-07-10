import random
def main():

    #A simple hangman game for the command prompt

    # HiddenWord is an empty string that will hold the underscores
    HiddenWord = ""

    Words = ['Apple', 'Banana', 'Cherry']
    #Words = ['Apple']
    # Select a random word from the array bank, started with a guaranteed word to simplify development

    # GuessWord is the word to be guessed by the player, all lower case, remember 0 based indexing
    GuessWord = Words[random.randint(0, len(Words) - 1)].lower()

    # HiddenWord is the GuessWord converted into an string of underscores
    for i in range(0, len(GuessWord)):
        HiddenWord += "_"

    # set a boolean for checking completeness
    isComplete = False
    # make a counter to keep track of the tries
    TryCounter = 0

    # split the HiddenWord into a list
    # i used the unpack method : [*string] where string is a string or a variable holding a string
    HiddenWordList = [*HiddenWord]

    # a bug I ran into is below
    # HiddenWordList is outputting ['_ _ _ _ _'] when it should go ['_', '_', '_' , '_' , '_']
    #HiddenWordList = HiddenWord.split()  #hiddenwordlist has one list item when it should have multiple items
    #the unpack method is the way

    #print("HiddenWordList: ", HiddenWordList)

    while not isComplete:

        #print out the obfuscated word
        print(*HiddenWordList, end="\n")

        # create a variable to take user input for a letter
        #take a letter as input, removes white space and lowercases it to make it easier
        LetterGuess = str(input("Enter a single letter: ")).strip().lower()

        # preliminary checks
        if not len(LetterGuess) == 1 or not LetterGuess.isalpha:
            print("Enter a single letter... please ")
            continue

        # if the guessed Letter is present in the guess word
        if LetterGuess in GuessWord:
            # iterate over the letters in the guessWord
            for i in range(0, len(GuessWord)):
                # where LetterGuess is same as the value of GuessWord at index i
                if LetterGuess == GuessWord[i]:
                    # update that index number at the corresponding list index with the LetterGuess letter
                    HiddenWordList[i] = LetterGuess
                    # print(*HiddenWordList, end="\n")
        else:
            TryCounter = TryCounter + 1
            print("Try Again please. " + str(TryCounter) + " wrong tries")
            continue

        print("\n")
        # join the list HiddenWord into a string again with nothing in between
        HiddenWord = "".join(HiddenWordList)

        if HiddenWord == GuessWord:
            isComplete = True
            print("You got it! It's:", HiddenWord.capitalize())

        #iterate over the letters in the GuessWord

        print("********")


main()
