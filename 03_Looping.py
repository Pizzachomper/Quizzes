#Functions go here
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
           
#Set values for each variable    
rounds_played = 0
rounds_won = 0
rounds_lost = 0
score = 0

low = 1
high = 100

guesses_allowed = 2

#Ask user for # of rounds, enter for INFINITE MODE

rounds = check_rounds()
end_game = "no"

# rounds loop
end_game = "no"
while end_game == "no":
    
    #Make a list of already guessed results that the user cant guess twice.
    already_guessed = []

    guesses_left = guesses_allowed

    #Start of game Play Loop
    #Rounds heading
    print()
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
    
    print(heading)
    
    guess = ""
    secret = 24
    # Start Round!!
    while guesses_left >= 1:
        
        #Ask user the question
        response = input("What is 40 / 2 + 4? ")
        
        #Check if exit code has been entered
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
            print("you guessed", guess)
            print()
            
            #Take away user guesses for each go
            guesses_left -= 1
            #already_guessed.append(guess)

            #check that guess is not a duplicate
            if guess in already_guessed:
                print(f"You already guessed that number 😡! Please try again, You still have {guesses_left} guesses left.")
                print()
                continue
            
            #Check guess has the correct answer
            if guess == secret:
                rounds_played += 1
                rounds_won += 1
                print("Correct")
                print()
                break
            
            if guesses_left <=0:
                rounds_played += 1
                rounds_lost += 1
                print("You lost! 😭")
                print(F"Answer: {secret}")
                print()
                break

    # check if we are out of rounds
    if rounds_played == rounds:
        end_game = "yes"
        break
        