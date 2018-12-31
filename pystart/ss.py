#!/usr/bin/env python
# coding: utf-8

# In[32]:


import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


# In[33]:


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


# In[8]:


[x*x for x in range(10)]


# In[37]:


var1=3
var2=4
var3=var1+var2
var4=3**3
print(var4)


# In[45]:


from sys import *
print(argv)


# In[ ]:




