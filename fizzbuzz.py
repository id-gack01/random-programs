#the famous fizzbuzz program, in the flesh
def fizzbuzz():
    
    #get a number to accept as input
    n = int(input("Enter a number: "))
    #just in case someone wants to get smart
    if n < 1:
        print("Let's make it 1 because you break it otherwise")
        n = 1
    #declare a for loop that starts at 1 and includes the inputted numner    
    for i in range(1, n + 1 ):
        #case for fizzbuzz, modulo needs to be 0 in both cases
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        #need to use elif, otherwise it will double print when the first case happens    
        elif (i % 3 == 0):
            print("Fizz")
        #third case
        elif (i % 5 == 0):
            print("Buzz")
        #otherwise just print the number
        else:
            print(i)
fizzbuzz()
