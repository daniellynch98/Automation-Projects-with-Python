#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openpyxl, os, re
os.chdir('/Users/daniellynch/Downloads/')

wb = openpyxl.load_workbook('/Users/daniellynch/Downloads/Excelcolumns.xlsx')
sheet = wb.active
content = []

for foldername, subfolders, filenames in os.walk('/Users/daniellynch/Downloads/pythonTest'):
            for file in filenames:
                if file.endswith('.txt'):
                    print(file)
                    with open(os.path.join(foldername, file)) as f:
                        contentreader = f.readlines()
                        content.append(contentreader)
                        
content1 = content[0]
content2 = content[1]
content3 = content[2]
content4 = content[3]
for row in zip(content1, content2, content3, content4):
    sheet.append(row)

wb.save("Column work book.xlsx")


# In[ ]:




