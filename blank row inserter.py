#!/usr/bin/env python
# coding: utf-8

# In[25]:


import openpyxl, os
os.chdir('/Users/daniellynch/Downloads/')
wb = openpyxl.load_workbook("Textworkbook3.xlsx")
ws = wb.active
ws.insert_rows(2)
ws.insert_rows(3)
wb.save("Textworkbookrowmoved.xlsx")


# In[ ]:




