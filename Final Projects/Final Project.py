#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Knowledge competition

print( "---Welcome to our Python Competition---")

q1 = "Is Python case-sensitive?"
a1 = "Yes"
q2 = "Which method would you use to convert a string into lowercase?"
a2 = "lower()"
q3 = "Which method would you use to capitalize the first letter of a string?"
a3 = "capitalize()"
q4 = "Which method would you use to reverse a list?"
a4 = "reverse()"
q5 = "Which method would you use to remove a duplicate element from a list?"
a5 = "set()"
q6 = "Which method would you use to take input from the user?"
a6 = "input()"
q7 = "Is indentation required in Python?"
a7 = "Yes"
q8 = "What are Python iterators?"
a8 = "Iterators are objects which can be traversed though or iterated upon"
q9 = "Which module would you use to generate random numbers in Python?"
a9 = "random.random"
q10 = "Which character would you use to write comments in Python?"
a10 = "#"

questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
answers = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]

def question(id):
    print(questions[id])
    ans = input("Please enter your answer:")
    if ans.lower() == answers[id].lower():
        return True
    else:
        return False

#Main code: 

score = 0
for i in range(10):
    correct = question(i)
    if correct:
        score += 10
        print('Correct!')
        print('Score '+str(score)+"\n")
    else:
        print('Incorrect!')
        print("Score "+str(score)+ "\n")

print('Your score is '+str(score)+'/100')

if score <= 50:
    print("You are unsuccessful. Try again!")
else:
    print("You did it! Congratulations!")
    


# In[ ]:




