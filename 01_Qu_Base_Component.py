import math
import random

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

def int_check(question, low=None, high=None, exit_code=None):
    
    #Check if user has entered a number between 1 - 100
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"
    
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        
        try:
            response =  int(response)
        
            # check that integer is valid (ie: not too low / too hig etc)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response
                    
            elif situation == "low only":
                if response >= low:
                    return response
            
            #Print out errors
            print(error)     
            print()       
        
        except ValueError:
            print(error)
            print()

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

#Set values for each variable    
rounds_played = 0
rounds_won = 0
rounds_lost = 0
score = 0

low_number = 1
high_number = 100

guesses_allowed = 2

mode = "regular"

#Ask user how many rounds
rounds = int_check("How many rounds will you play?: ", 1, exit_code = "")
print()

#Infinite mode code
if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = "no"
while end_game == "no":
    
    already_guessed = []

    guesses_left = guesses_allowed

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (continues mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        
    print(heading)
        
    rounds_played += 1

    guess = ""
    secret = 24
    # Start Round!!
    while guess != secret and guesses_left >= 1:
        
        #Ask user the question
        guess = int_check("What is 40 / 2 + 4? ", low_number, high_number, "xxx")
        print("you guessed", guess)  
        print() 
        
        #check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You already guessed that number 😡! Please try again, You still have {guesses_left} guesses left.")
            print()
            continue

        already_guessed.append(guess)

        #Take away user guesses for each go
        guesses_left -= 1

        if guess == "xxx":
            end_game = "yes"
            break    

        if guess == secret:
            rounds_won += 1
            break
        
    # check if we are out of rounds
    if rounds_played >= rounds:
        break
        