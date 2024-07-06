#a function to find the maximum number value in a list of numbers, pls include a list of numbers only
def findMax(numberList):
            currentMax = 0
            for number in numberList:
            #if the current number is greater than or equal the number stored in currentMax,
                if number >= currentMax:
                    # assign that number to currentMax
                    currentMax = number
                #return the currentMax number
            return currentMax
