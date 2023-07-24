import random
#Generate random numbers for the questions
    
secret = random.randint(1, 100)
secret2 = random.randint(1, 10)    
secret3 = random.randint(1, 50)  
secret4 = random.randint(1, 20)

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

print(comp_choice)