#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating a function that calculates passingGrades
def Grade(grades):
    
    passingGrade = grades[0] * (0.3) + grades[1] * (0.3) + grades[2] * (0.4)
    return passingGrade
    
students = {} #dictionary for all students info

#for loop to allows users to enter their info
for i in range(5):
    name = str(input("Please enter your name:"))
    midterm = int(input("Please enter your midterm grade:"))
    project = int(input("Please enter your project grade:"))
    final = int(input("Please enter your final grade:"))
    
    students[name] = [midterm,project,final] # to put informations in the studnets dictionary
    
final_grades = {} # dictionary to keep final grades together

for stname in students:
    final_grades[stname] = Grade(students[stname]) # put students final grades and their names into the dictionary
 
print(sorted(final_grades.items(), key=lambda k:k[1], reverse=True)) # sorted dictionary values decs order


# In[ ]:




