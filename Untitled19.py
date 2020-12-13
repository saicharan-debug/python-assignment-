#!/usr/bin/env python
# coding: utf-8

# # Question-1

# In[23]:


abc = open("text.txt",'w')
abc.write("I Love Letsupgrade")
abc.close()


# In[2]:


abc = open("text.txt",'r')
x = abc.read()
abc.close()


# In[24]:


abc = open("text.txt",'a')
abc.write("Because it teach us very good")
abc.close()


# # Question-2

# In[25]:


def fact():
    n = 6
    fact = 1
    for i in range(1,n+1):
        fact = fact * 1
fact()


# In[19]:


n = 23
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("The factorial of 23 is : ",end="") 
print (fact) 


# In[ ]:




