#!/usr/bin/env python
# coding: utf-8

# In[7]:


Even_num = list(range(0,20,2)) #Creating even number list.
Odd_num = list(range(1,20,2)) #Creating odd number list.

print(Even_num)
print(Odd_num)

# Merged even number list and odd number list with multply every element with two.
Merged_num = [i*2 for i in Even_num] + [i*2 for i in Odd_num] 

print(Merged_num)

#Loop for print data types of values in merged list.
for i in Merged_num:
    print(type(i))


# In[ ]:



