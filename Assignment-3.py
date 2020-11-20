#!/usr/bin/env python
# coding: utf-8

# In[1]:


def red_fn(a):
    x=a.__iter__()
    y=next(x)  
    for i in a[1:]:
        y=y+i
    return y


# In[2]:


red_fn([1,2,3,4,5])


# In[3]:


red_fn(['a','z','x','c','v'])


# In[5]:


def fil_fn(x,y):
    return x(y)

        


# In[6]:


def even_num(a):
    x=[i for i in a if i%2==0]
    return x


# In[7]:


a=[1,2,3,4,5]


# In[8]:


fil_fn(even_num,a)


# In[10]:


a=['x','y','z']
print([ a[i]*j for i in range(len(a)) for j in range(1,5) ])


# In[11]:


a=['x','y','z']
print([ a[i]*j  for j in range(1,5) for i in range(len(a))])


# In[15]:


[([x+y] if x!=5 else ([x+y-3,x+y-2,x+y-1,x+y])) for x in range(2,6) for y in range(3)]


# In[19]:


a=[1,2,3] 


# In[20]:


for  i in a:
    for j in a:
         print([j,i])


# In[ ]:




