# enter a string and convert to an acronym

StringInput = input("Enter a few words: ")
#StringInput = "Random Access Memory"
#print(StringInput) 

# a stringaslist is first converted to upper, then split
StringAsList = StringInput.upper().split()
#print(StringAsList)

#empty string to put first letters into
acronym = ""
for i in StringAsList:

    #iterates over the StringAsList, taking the 0th to 1st index of each list item
    # because they're strings, i, which represents a string, can be sliced... [0:1]
    acronym += i[0:1]


print(acronym)
