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


question_list = [
"What is 40 / 2 + 4?", 
"What is X if 3x - 12 = 2x + 3? ", 
"If Matt is 21 and his birthday is janurary 15th and next year Tim will be half matts age and his Birthday Feburary 15 how old is tim today?",
"What is X if 3(-2x + 20) = 0",
"If Valorant is a 5 out of 10, Roblox is 3 lower than Valorant, D2 is quadruple Roblox, and halo mcc  is 2 more than D2. What is Halo Mcc",
"If christmas is on the 25th of december, how long until easter, If easter is christmas times 4 - 31",
"If the length of the rectangle is 9 and the width is the square root of the length, then what is the area"   
               ]

# Question answers
# 24
# 15
# 10
# 10
# 9
# 69

choose_error = "Please answer the question correctly"
low = 0.1
high = 100

#compare user choice and computer choice
#get computer choice
comp_choice = random.choice(question_list)
print(comp_choice)
                                                                                                                                       