#!/usr/bin/env python
# coding: utf-8

# In[25]:


import imapclient, pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)
conn.login ('insert email here', 'insert password here')
conn.select_folder("Inbox", readonly = True)
Messages  = conn.search (['SINCE', '05-Jun-2020'])
Messages
raw_message = conn.fetch([2869],['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(raw_message[2869][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.text_part.get_payload().decode('UTF-8')


# In[29]:


conn.select_folder("Inbox", readonly = False)
Test_emails = conn.search(["SUBJECT", 'Test Email'])
conn.delete_messages(Test_emails)


# In[ ]:




