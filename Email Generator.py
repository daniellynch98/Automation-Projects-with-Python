#!/usr/bin/env python
# coding: utf-8

# In[204]:


import random, openpyxl, os
os.chdir("/Users/daniellynch/Downloads/")
wb = openpyxl.load_workbook("EmailSheet.xlsx")
ws = wb.active
digits =  random.randint(105,995)
combination = str(digits)
gender = "Male"
Nationality = "British"
emails_and_names = []
#List of British male names and surnames
names = "Oliver Harry Jack George  Noah Leo Jacob Oscar Charlie  Jackson William Joshua Ethan James Freddie Alfie Logan Lucas Finley Max Alexander Dylan Edward Reuben Louie Samuel  Harrison Joseph Teddy"
first_names = names.split()
sur = "Smith Jones Williams Brown Taylor Davies Wilson Evans Thomas Johnson Roberts Walker Wright Thompson Robinson White Hughes Edwards Hall Green Martin Wood Lewis Harris Clarke Jackson Clark Turner Scott Hill Moore"
surnames = sur.split()
#Loop to create emails and append to spreadsheet
for i, s in zip(first_names, surnames):
    first_name = i
    
    surname = s
    
    emailmaker = first_name + surname + combination + "@gmail.com"
    mini_list =[]
    mini_list.append(i)
    mini_list.append(s)
    mini_list.append(gender)
    mini_list.append(Nationality)
    mini_list.append(emailmaker)
    ws.append(mini_list)

wb.save("EmailSheet.xlsx")
print("Finished Transferring")


# In[ ]:




