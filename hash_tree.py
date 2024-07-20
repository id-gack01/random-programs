#draw a tree

#take input for the height variable
height = int(input("enter a number here: "))

#count the number of spaces needed, and have that be the beginning count of spaces
#spaces starts at height - 1, then decrease by 1 afterwards
spaces = height - 1
#count the number of hashes needed, and have that be the beginning count of hashes

#hashes start at 1, then increase by 2  afterwards
hashes = 1
# get a stump space variable to hold for later, it doesn't change after initial creation
stump_space = spaces
#the spaces need a for loop, the hashes need a for loop

#also need the stump spaces as the final for loop
#while loop ends when height is 0 

while height > 0:
    #print the spaces
    for i in range(spaces):
        print(" ", end="")
    #print the hash after
    for i in range(hashes):
        print("#", end="")

    print()
    # decrement the number of spaces by 1 each go around
    spaces = spaces - 1
    # increment the number of hashes by 2 each go around
    hashes = hashes + 2
    #decrement the height counter
    height = height - 1

for i in range(stump_space):
    print(" ", end="")
print("#")
