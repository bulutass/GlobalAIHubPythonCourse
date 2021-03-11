#!/usr/bin/env python
# coding: utf-8

# In[2]:


#CV Application

#Used pandas library to create table version of the dictionaries
#Created 5 diffirent dictionaries. Keys are name, surname, age, email and occupation. 


import pandas as pd

CV1 = {"Name": "Harry", "Surname": "Potter", "Age": 41, "e-mail": "harrypotter@gmail.com", "Occupation": "Head of the Department of Magical Law Enforcement"}
CV2 = {"Name": "Hermione", "Surname": "Granger", "Age": 42, "e-mail": "hermionegranger@gmail.com", "Occupation": "Minister of Magic"}
CV3 = {"Name": "Ronald", "Surname": "Weasley", "Age": 41, "e-mail": "ronaldweasley@gmail.com", "Occupation": "Co-manager"}
CV4 = {"Name": "Neville", "Surname": "Longbottom", "Age": 41, "e-mail": "nevillelongbottom@gmail.com", "Occupation": "Professor of Herbology"}
CV5 = {"Name": "Luna", "Surname": "Lovegood", "Age": 40, "e-mail": "lunalovegood@gmail.com", "Occupation": "Magizoologist"}



CV_list = [CV1,CV2,CV3,CV4,CV5] #Created a list that contain all CV dictionaries

table = pd.DataFrame(CV_list) #used DataFrame constructor of pandas library

print(table)


# In[ ]:




