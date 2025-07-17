#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input("enter"))
t=n
sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10
if t%sum==0:
    print("the given number is niven")    
else:
    print("not an nivens nmuber")
"""n=18
   1+8=9
   18%9==0
   n=19
   1+9=10
   19%10!=0"""


# In[ ]:




