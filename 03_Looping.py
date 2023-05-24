#Functions go here
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
        