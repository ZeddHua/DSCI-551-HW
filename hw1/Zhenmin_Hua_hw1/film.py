#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: UTF-8 -*-   
import pandas as pd
import requests
import json
import sys
arg = sys.argv[1] 

url = 'https://new-project-aa32e-default-rtdb.firebaseio.com/film_category_all.json'
response = requests.get(url)
json_film_category_all = response.text
dic = json.loads(json_film_category_all)
df = pd.DataFrame(dic)

def pattern1(arg):
    #filtering data
    i = arg[0].upper()
    i2 = arg[1:].lower()
    arg = i + i2
    df_sub = df[df.name==arg]
    df_sub = df_sub[['title','release_year','rating','rental_rate','rental_duration']].sort_values(by='title').applymap(str)
    #transform data from df to tuple
    df_sub_tuple = [tuple(x) for x in df_sub.values]
    #print out
    if df_sub.empty==False:
        for i in df_sub_tuple:
            print(i)
    else:
        print('No results found.')

if __name__ == '__main__':
    pattern1(arg)

