import random

#something to help someone make a decision

#insert choices into a prompt and return a random value to help you pick

#take an input and convert into string
choice_input = str(input("Enter your options separated by comma here: "))

choices = choice_input.split(",")

print("Try... " + choices[random.randint(0, len(choices) -1)])
