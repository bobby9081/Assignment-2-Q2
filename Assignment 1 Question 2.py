#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program that accepts a word from the user and reverse it.


# In[1]:


a=[]
b=input('enter the word') 
for i in range(len(b)-1,-1,-1):
    a.append(b[i])
a=''.join(a)
print(a)

