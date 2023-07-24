import random
import math

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

#Define values
low = 0
high = 100
guesses_allowed = 2
score = 0

#Start loop
end_game = "no"
while end_game == "no":

    #Create list of already guessed
    already_guessed = []
    guesses_left = guesses_allowed

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
    question_5 = F"If the length of the rectangle is {secret2 * secret2} is the square root of the length?"
    question_6 = F"if As age will be double Bs age next year and Bs age is {secret2} less than Cs age and Cs age is {secret4}?"

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
                    print("You got it! 🎊")
                    print()
                    score += 100
                    break

                #User runs out of guesses
                if guesses_left <=0:
                    print("You lost! 😭")
                    print(F"Answer: {answer}")
                    print()
                    break

#Print the score
print(score)