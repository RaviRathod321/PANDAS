#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


groceries = pd.Series(data =[30, 6, 'yes', 'no'], index=['eggs', 'apples','milk', 'bread'])
print(groceries)


# In[3]:


groceries.shape


# In[4]:


groceries.ndim


# In[5]:


groceries.size


# In[6]:


groceries.index


# In[7]:


groceries.values


# In[8]:


#checking if the value exists in the list

x = 'bananas' in groceries
print(x)


# In[9]:


#checking if bread exist in the grocery list
y = 'bread' in groceries
print(y)


# # How do we modify or access its elements?
# # We access elements in Groceries using index labels:
# # We use a single index label

# In[10]:


print('How many eggs do we need to buy:', groceries['eggs'])
print()


# In[11]:


print('Do we need milk and bread:\n', groceries[['milk', 'bread']])
print()


# In[12]:


# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
print()


# In[13]:


# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]]) 
print()


# In[14]:


groceries[[0, 1]]


# In[15]:


#here loc means location 

groceries.loc[['eggs', 'apples']]


# In[16]:


#here iloc means integer location, means we are particulary looking for an integer

groceries.iloc[[2, 3]]


# In[17]:


groceries


# In[19]:


#Data mofification, this updates the data available in our groceries list
groceries['eggs'] = 14
print(groceries)


# In[ ]:




