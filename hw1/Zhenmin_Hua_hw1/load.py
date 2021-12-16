#!/usr/bin/env python
# coding: utf-8

# In[21]:


# -*- coding: UTF-8 -*- 
import requests
import pandas as pd
import json

film = pd.read_csv("film.csv",sep=';')
actor = pd.read_csv("actor.csv",sep=';')
film_actor = pd.read_csv("film_actor.csv",sep=';')
category = pd.read_csv("category.csv",sep=';')
film_category = pd.read_csv("film_category.csv",sep=';')

#df1
film_category_merge = pd.merge(film_category,category, on='category_id', how='left')
film_category_all = pd.merge(film,film_category_merge, on='film_id', how='left')
#df2
df1 = pd.merge(film_actor,actor,on='actor_id',how='left')
film_actor_all = pd.merge(df1,film,on='film_id',how='left')

#turn to json
film_category_all_json = film_category_all.to_json()
film_actor_all_json = film_actor_all.to_json()

#upload
url1 = 'https://new-project-aa32e-default-rtdb.firebaseio.com/film_category_all.json'
response1 = requests.put(url1,film_category_all_json)
url2 = 'https://new-project-aa32e-default-rtdb.firebaseio.com/film_actor_all.json'
response2 = requests.put(url2,film_actor_all_json)

