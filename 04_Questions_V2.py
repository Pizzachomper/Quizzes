import random
import math

#Int checker
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
score = 0

#Start loop
end_game = "no"
while end_game == "no":

    #Generate random numbers for the questions
    
    secret = random.randint(1, 100)
    secret2 = random.randint(1, 10)    
    secret3 = random.randint(1, 50)  
    secret4 = random.randint(1, 20)

    guesses_left = guesses_allowed

    #Questions

    question_1 = F"What is {secret} / {secret2} + {secret3}? "
    question_2 = F"What is {secret} * {secret2} - {secret3}? "
    question_3 = F"What is X if {secret2}X + {secret} = {secret4}X + {secret3}? "
    question_4 = F"What is X if {secret}({secret4}X + {secret2}) + {secret3} = 0"
    question_5 = F"If the length of the rectangle is {secret2 * secret2} and the width is the square root of the length, then what is the perimiter"


    #Create different questions that users will get
    question_list = [
    question_1, question_2, question_3, question_4, question_5
                    ]

    #get computer choice
    comp_choice = random.choice(question_list)
    
    #Use correct math rules to create the right question for the right task
    #Easy
    if comp_choice == question_1:
        answer = secret / secret2 + secret3

    if comp_choice == question_2:
        answer = secret * secret2 - secret3

    #Medium
    if comp_choice == question_3:
        secret5 = secret4 - secret2
        answer = (secret - secret3) / secret5

    if comp_choice == question_4:
        secret5 = (secret * secret4)
        secret6 = (secret * secret2) + secret3
        answer = -(secret6 / secret5)
    #Hard
    if comp_choice == question_5:
        secret5 = math.sqrt(secret2 * secret2)
        answer = (2 * secret5) + 2 * (secret2 * secret2)

    guess = ""
    # Start Round!!
    if (100 > answer > 1): 
        while guess != answer and guesses_left >= 1:
            
            print(comp_choice)

            #Ask user for their guess
            guess = int_check("What is your guess (1 - 100): ", low, high, "xxx")
            print("you guessed", guess)
            print()

            #Take away user guesses for each go
            guesses_left -= 1

            # Check user hasn't entered the same number again or exit code

            if guess == "xxx":
                end_game = "yes"
                break
            
            #Compare guess to secret number
            #Too low or too high
            if guess < answer:
                print(F"Too low, try a higher number. Guesses left {guesses_left}")
            elif guess > answer:
                print(F"Too high, try a lower number. Guesses left {guesses_left}")

            print()

            #Correctly guessed secret
            if guess == answer:
                print("You got it 🎊")
                print()
                score += 100
                break

            #User runs out of guesses
            if guesses_left <=0:
                print("You lost😭")
                print(F"Answer: {answer}")
                print()
                break
    
print(score)