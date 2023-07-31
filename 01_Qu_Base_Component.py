#Quiz base component
import math
import random

#Functions go here
#Yes/no checker
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

#Instructions
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

#Rounds
def check_rounds():
    
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                #If infinite mode not chosen, check response
                response = int(response)

                #Start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response
           
#Int checker
def int_check(response, low, high):
    
    #Check if the answer is an integer
    try:
        responseinteger = int(response)

    #Solve for value error
    except ValueError as ex:
        print()
        print("Your text is not an integer")
        return -999

    #Make sure the user enters between low and high
    if low <= responseinteger <= high:
        return responseinteger
    
    #Otherwise output an error
    else:
        error = f"Please enter an integer between {low} and {high}"
        print()
        print(error)
        return -999


#Main component
#Instructions component
#Ask user if they have played before, If yes, show instructions
played_before = yes_no("Have you played this game before? ")
print(F"You choose {played_before}")

if played_before == "no":
    instructions()


#Looping component
#Variables go here    
questions_played = 0
questions_right = 0
questions_wrong = 0
score = 0
guesses_allowed = 2

low = 1
high = 100

#Ask user for # of rounds, enter for INFINITE MODE
rounds = check_rounds()
end_game = "no"


#Rounds loop
end_game = "no"
while end_game == "no":
    
    #Make a list of already guessed results that the user cant guess twice.
    already_guessed = []
    guesses_left = guesses_allowed


    #Questions component
    #Generate random numbers for the questions
    secret = random.randint(1, 100)
    secret2 = random.randint(1, 10)    
    secret3 = random.randint(1, 50)  
    secret4 = random.randint(1, 20)
    secret7 = secret + secret3
    secret9 = random.randint(2, 6)
    secret8 = secret7 * secret9 
    secret6 = secret8 - secret4
    secret10 = secret2 * secret9
    
    #Questions
    question_1 = F"What is {secret10} / {secret2} + {secret3}? "
    question_2 = F"What is {secret} * {secret2} - {secret3}? "
    question_3 = F"What is X if -{secret6}X + {secret} = {secret4}X - {secret3}? "
    #question_4 = F"What is X if {secret2}({secret4}X - {secret3}) = {secret10}"
    question_5 = F"If the length of the rectangle is {secret2 * secret2} and the width is the square root of the length. What is the width?"
    question_6 = F"if As age will be double Bs age next year and Bs age is {secret2} less than Cs age and Cs age is {secret4}. How old is A?"

    #Create different questions that users will get
    question_list = [
    question_1, question_2, question_3, question_5, question_6
    ]

    #get computer choice
    comp_choice = random.choice(question_list)

    #Use correct math rules to create the right question for the right task
    #Easy
    if comp_choice == question_1:
        answer = secret10 / secret2 + secret3

    if comp_choice == question_2:
        answer = secret * secret2 - secret3

    #Medium
    if comp_choice == question_3:
        answer = secret8 / secret7

    if comp_choice == question_5:
        answer = secret2

    #Hard
    #if comp_choice == question_4:
        #answer = (((secret10 / secret2) + secret3) * secret4) / secret4
        
    if comp_choice == question_6:
        answer = (secret4 - secret2 + 1) * 2


    #Start Round
    if 100 > answer > 0:
        #Start of game Play Loop
        #Rounds heading
        if rounds == "":
            heading = f"Continous Mode: Round {questions_played + 1}"
        else:
            heading = f"Round {questions_played + 1} of {rounds}"
        print(heading)

        while guesses_left >= 1:
            
            #Print the computer choice
            print(comp_choice)

            #Ask user for their guess

            response = input("What is your guess (1 - 100): ").lower()

            #Check user hasn't entered the same number again or exit code
            if response == "xxx":
                end_game = "yes"
                break
            
            #Get the users guess
            guess = int_check(response, low, high)

            #Int checker error
            if guess == -999:
                print("try again")
                print()

            else:
                #repeat the users guess    
                print("you guessed", guess)
                print()

                #Take away user guesses for each go
                guesses_left -= 1

                #already_guessed.append(guess)

                #Check guess has the correct answer
                if guess in already_guessed:
                    print(f"You already guessed that number 😡! Please try again, You still have {guesses_left} guesses left.")
                    print()
                    continue
                
                #Compare guess to secret number
                #Too low or too high
                if guess < answer:
                    print(F"Too low! try a higher number. Guesses left {guesses_left}")
                elif guess > answer:
                    print(F"Too high! try a lower number. Guesses left {guesses_left}")

                #Correctly guessed secret
                if guess == answer:
                    questions_played += 1
                    questions_right += 1
                    print("You got it! 🎊")
                    print()
                    score += 100
                    break

                #User runs out of guesses
                if guesses_left <=0:
                    questions_played += 1
                    questions_wrong += 1
                    print("You lost! 😭")
                    print(F"Answer: {answer}")
                    print()
                    break
        
        # check if we are out of rounds
        if questions_played == rounds:
            end_game = "yes"
            break

if questions_played > 0:

    #Endgame component
    #Calculate Game Stats
    percent_right = questions_right / questions_played * 100
    percent_wrong = questions_wrong / questions_played * 100

    #Displays game stats with % values to the nearest whole number
    print()
    print("*** Game Statistics ***")
    print(f"Questions right: {questions_right}, {percent_right:.0f}% \nQuestions wrong: {questions_wrong}, {percent_wrong:.0f}% \nQuestions played: {questions_played}")
    print(f"Score: {score} pts")
    print("Thank you for playing my game 🙃")
    print()

else:
    print()
    print("you did not play any rounds.  🐔")