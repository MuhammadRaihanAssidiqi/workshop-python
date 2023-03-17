#!/usr/bin/env python
# coding: utf-8

# In[3]:


2 + 2


# In[4]:


50 - 5*6


# In[5]:


(50 - 5*6) / 4


# In[6]:


8 / 5


# In[7]:


17 / 3


# In[8]:


17 // 3


# In[9]:


17 % 3


# In[11]:


5 * 3 + 2


# In[12]:


5 ** 2


# In[13]:


2 ** 7


# In[14]:


width = 20
height = 5 * 9
width * height


# In[15]:


n


# In[16]:


4 * 3.75 - 1


# In[18]:


tax = 12.5 / 100
price = 100.50
price * tax


# In[19]:


price + _


# In[20]:


round(_,2)


# In[21]:


'"Isn\'t," they said.'


# In[22]:


print('"Isn\'t," they said.')


# In[23]:


s = 'First line.\nSecond line.'
s


# In[24]:


print(s)


# In[25]:


print('C:\some\name')


# In[26]:


print(r'C:\some\name')


# In[27]:


print("""Usage: thingy [OPTIONS]
    -h
    -H
""")


# In[28]:


3 * 'un' + 'ium'


# In[29]:


'Py' 'thon'


# In[30]:


text = ('Put several strings within parenthese '
        'to have them joined together.')
text


# In[34]:


prefix = 'Py'


# In[35]:


prefix 'thon'


# In[38]:


('un' * 3) 'ium'


# In[39]:


prefix + 'thon'


# In[40]:


word = 'Python'
word[0]


# In[41]:


word[5]


# In[42]:


word[-1]


# In[43]:


word[-2]


# In[44]:


word[-6]


# In[45]:


word[0:2]


# In[46]:


word[2:5]


# In[47]:


word[:2]


# In[48]:


word[4:]


# In[49]:


word[-2:]


# In[51]:


word[:2] + word[2:]


# In[52]:


word[:4] + word[4:]


# In[53]:


+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0   1   2   3   4   5   6
-6 -5  -4  -3  -2  -1


# In[54]:


word[42]


# In[55]:


word[4:24]


# In[56]:


word[42:]


# In[57]:


word[0] = 'J'


# In[59]:


word[2:] + 'py'


# In[60]:


'J' + word[1:]


# In[61]:


word[:2] + 'py'


# In[62]:


s = 'supercalifragilisticexpialidocious'
len(s)


# In[63]:


squares = [1, 4, 9, 16, 25]
squares


# In[64]:


squares[0]


# In[65]:


squares[-1]


# In[66]:


squares[-3:]


# In[67]:


squares[:]


# In[68]:


squares + [36, 49, 64, 81, 100]


# In[69]:


cubes = [1, 8, 27, 65, 125]
4 ** 3


# In[70]:


cubes[3] = 64
cubes


# In[72]:


cubes.append(216)
cubes.append(7 ** 3)
cubes


# In[73]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters


# In[74]:


letters[2:5] = ['C', 'D', 'E']
letters


# In[75]:


letters[2:5] = []
letters


# In[77]:


letters[:] = []
letters


# In[78]:


letters = ['a', 'b', 'c', 'd']
len(letters)


# In[79]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x


# In[80]:


x[0]


# In[81]:


x[0][1]


# In[82]:


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# In[83]:


i = 256*256
print('The value of i is' , i)


# In[84]:


a, b = 0,1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


# In[ ]: