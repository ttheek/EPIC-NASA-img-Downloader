#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
import json
import os


# In[9]:


api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  #Your api
date = 'YYYY/MM/DD' #Date that you want
url=(f'https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}')
pkg = r.json()
for i in pkg:
    img=i['image']
    link = f'https://epic.gsfc.nasa.gov/archive/natural/{date}/jpg/{img}.jpg'
    with open(img +'.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)
    print('Done')    


# In[ ]:




