#Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

def instructions():
    #Write the instructions here
    print('''
^*^ How to Play Quizzers ^*^

This is a Quiz game made in python. 
Answer with how many rounds you will play or type enter for infinite mode. 

Please type a respectfull response
The computer will respond if your answer is correct or incorrect

You have only 2 attempts to guess the answer. But if you dont want to play anymore type xxx or x to quit, 
you can see your game summary at the end of your game and how many rounds you have won
Enjoy 😆
    ''')

    return ""

#Print the name of the game

print()
print("^-^ Welcome to Quizzers ^-^")
print()

#Ask user if they have played before
#If yes, show instructions
played_before = yes_no("Have you played this game before? ")
print(F"You choose {played_before}")

if played_before == "no":
    instructions()
