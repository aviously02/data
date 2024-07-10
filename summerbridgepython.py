#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3+7


# In[ ]:


print("hello")


# In[ ]:


name= "Avi"
age= 21


# In[ ]:


# This is a comment. It will not run
# You can echovalues without using print in this notebook


# In[ ]:


name


# # Variables and values

# In[ ]:


# Variables can be used in calculations
print(age)
age = age + 3
print (age)


# In[ ]:


# Order of Operations matters!
first = 1
second = first * 5
first = 2
print (first)
print (second)


# In[ ]:


# Values have types. Types affect what you can do with them.
print (5-3)
#print ("hello"-"h")


# In[ ]:


print(len("hello"))
#print(len(6))


# In[ ]:


print (5 // 3)
print (5 / 3)
print (5 % 3)


# # Getting Help

# In[ ]:


# Rounding numbers is built in
round (3.14159)


# In[ ]:


round(3.14159,2)


# In[ ]:


round(3.14159, ndigits=2)


# In[ ]:


# All functions return a new value
rounded_pi=round(3.14159,2)
print(rounded_pi)


# In[ ]:


radiance=1.0
radiance=max(2.1,2.0+min(radiance,1.1*radiance-0.5))
print(radiance)


# In[ ]:


# Break down these operations
radiance = 1.0
min_arg_2= 1.1 * radiance -0.5
print("Min arg2:", min_arg_2)

min_result = min(radiance, min_arg_2)
print("Min result:",min_result)

radiance=max(2.1,2.0 + min_result)
print(radiance)


# # Libraries

# # A Brief Interlude with Git

# In[ ]:





# In[ ]:




