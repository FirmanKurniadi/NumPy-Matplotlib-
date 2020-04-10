#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt


# In[11]:


import numpy as np


# In[12]:


x = np.linspace(1,5,11)


# In[13]:


y = x ** 2


# In[14]:


x


# In[15]:


y


# In[7]:


plt.plot(x,y,'r')


# In[8]:


plt.xlabel('x Axis')


# In[9]:


plt.xlabel('X Axis')


# In[10]:


plt.ylabel('Y Axis')


# In[11]:


plt.title('Data Contoh')


# In[12]:


plt.show


# In[13]:


plt.show()


# In[14]:


plt.plot(x,y,'r')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Data Contoh')
plt.show()


# In[15]:


plt.subplot(1,2,1)
plt.plot(x,y, 'r--')
plt.subplot(1,2,2)
plt.plot(y, x, 'b*-')


# In[16]:


fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y, 'b')
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Contoh Judul')


# In[18]:


fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y,'b')
axes1.set_xlabel('X utama')
axes1.set_ylabel('Y utama')
axes1.set_title('Plot utama')

axes2.plot(y, x, 'r')
axes2.set_xlabel('x dalam')
axes2.set_ylabel('Y dalam')
axes2.set_title('plot dalam');


# In[19]:


fig = plt.figure(figsize=(8,4), dpi=100)


# In[20]:


fig, axes = plt.subplots(figsize=(8,4))

axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');


# In[22]:


axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');


# In[23]:


fig, axes = plt.subplots(figsize=(8,4))

axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');


# In[24]:


fig, axes = plt.subplots(figsize=(8,4))

axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

fig.savefig("contoh.png", dpi=200)


# In[25]:


fig, axes = plt.subplots(figsize=(8,4))

axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

fig.savefig("contoh.png", dpi=200)


# In[26]:


fig, axes = plt.subplots(figsize=(8,4))

axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

fig.savefig("contoh.png", dpi=200)


# In[17]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="Data x pangkat 2")
ax.plot(x, x**3, label="Data x pangkat 3")

ax.legend(loc=0)


# In[19]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)


# In[20]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')


# In[21]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5,5,15,5])


# In[22]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')


# In[26]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=10)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
       


# In[27]:


from random import sample
data = sample(range(1, 1000), 10)
plt.hist(data)


# In[ ]:




