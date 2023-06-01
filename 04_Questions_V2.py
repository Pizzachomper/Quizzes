import random
import math

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

#Define values
choose_error = "Please answer the question correctly"
low = 0
high = 100
guesses_allowed = 2

#Start loop
end_game = "no"
while end_game == "no":

    #Generate random numbers for the questions
    
    secret = random.randint(1, 100)
    secret2 = random.randint(1, 100)    
    secret3 = random.randint(1, 100)  
    secret4 = random.randint(1, 100)

    guesses_left = guesses_allowed

    #Questions

    question_1 = F"What is {secret} / {secret2} + {secret3}? "
    question_2 = F"What is {secret} * {secret2} - {secret3}? "
    question_3 = F"What is X if {secret}X - {secret2} = {secret3}X + {secret4}? "
    question_4 = F"What is X if {secret}(X + {secret2}) = 0"
    question_5 = F"If the length of the rectangle is {secret} and the width is the square root of the length, then what is the area"


    #Create different questions that users will get
    question_list = [
    question_1, question_2, question_3, question_4, question_5
                    ]

    #get computer choice
    comp_choice = random.choice(question_list)
    print()
    print(comp_choice)

    if comp_choice == question_1:
        answer = secret / secret2 + secret3

    if comp_choice == question_2:
        answer = secret * secret2 - secret3

    if comp_choice == question_3:
        answer = secret - secret2

    if comp_choice == question_4:
        answer = secret + secret2

    if comp_choice == question_5:
        answer = math.sqrt(secret) * secret

    guess = ""
    # Start Round!!
    while guess != answer and guesses_left >= 1:
        
        #Ask user for their guess
        guess = int_check("What is your guess (1 - 100): ", low, high, "xxx")
        print("you guessed", guess)
        print()

        #Take away user guesses for each go
        guesses_left -= 1
