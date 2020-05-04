#!/usr/bin/env python
# coding: utf-8

# In[1]:


#My first Program
#In Python no need to mention the type of value and python can hold any kind of value
var1=10
var2=4.5
var3="Ineuron"
print(var1)
print(var2)
print(var3)


# In[8]:


for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        print(i,end=",")
print('')


# In[48]:


firstname = input("Enter your first name:")
lastname = input("Enter your last name:")
fn = firstname[::-1]
ln = lastname[::-1]  
print (fn,"",ln)


# In[9]:


pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is:',V)


# In[2]:


values = input("Sequence of comma-separated numbers: ")
l = values.split(",")
print(l)


# In[7]:


num=int(input("Enter the number of pattern:"))
for i in range(num):
    for j in range(i):
        print ('* ', end="")
    print('')
    
for i in range(num,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[10]:


word = input("Input a word to reverse:")
print (word[::-1])
#Output which you have provided in the PDF was Wrong.


# In[11]:


print('WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN, !\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens')


# In[ ]:




