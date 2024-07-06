#a function to find the maximum number value in a list of numbers, pls include a list of numbers only
def FindMax(numberList):
    currentMax = 0

    for number in numberList:
        #if the current number is greater than the number stored in currentMax,
        if number >= currentMax:
            # assign that number to currentMax
            currentMax = number
    #return the currentMax number
    return currentMax
