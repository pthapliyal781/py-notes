
# coding: utf-8

# In[1]:

import twitter


# In[2]:

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


# In[3]:

home_timeline_data = twitter_api.statuses.home_timeline()
import json
with open('data.json', 'w') as outfile:
    json.dump(home_timeline_data, outfile, indent=4)


# In[10]:

#home_timeline_data[0] # only compile if needed


# In[12]:

home_timeline_data[0]['user']['screen_name']
home_timeline_data[0]['text']


# In[6]:

len(home_timeline_data)


# In[14]:

import numpy
import pandas as pd
user_screen_name =[]
text_data = []
for item in range(0, len(home_timeline_data)):
    user_screen_name.append(home_timeline_data[item]['user']['screen_name'])
    text_data.append(home_timeline_data[item]['text'])


# In[15]:

user_screen_name = pd.DataFrame(user_screen_name)
text_data


# In[9]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt







