#!/usr/bin/env python
# coding: utf-8

# In[26]:


import openpyxl, os, re
os.chdir('/Users/daniellynch/Downloads/')

wb = openpyxl.load_workbook('/Users/daniellynch/Downloads/Excelcolumns.xlsx')
sheet = wb.active

for foldername, subfolders, filenames in os.walk('/Users/daniellynch/Downloads/pythonTest'):
            for file in filenames:
                if file.endswith('.txt'):
                    print(file)
                    with open(os.path.join(foldername, file)) as f:
                        contentreader = f.readlines()
                        sheet.append(contentreader)
                        
                        


wb.save("Column work book.xlsx")


# In[ ]:




