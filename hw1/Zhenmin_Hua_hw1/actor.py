#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: UTF-8 -*-   
import requests
import json
import pandas as pd
import sys
arg = sys.argv[1] 


url = 'https://new-project-aa32e-default-rtdb.firebaseio.com/film_actor_all.json'
response = requests.get(url)
json_film_actor_all = response.text
dic = json.loads(json_film_actor_all)
df = pd.DataFrame(dic)

def pattern2(arg):
    arg = arg.upper()
    list_name = arg.split()
    df_sub = df[(df.first_name==list_name[0]) & (df.last_name==list_name[1])]
    df_sub = df_sub[['title','release_year']].sort_values(by='title').applymap(str)
    df_sub_tuple = [tuple(x) for x in df_sub.values]
    if df_sub.empty==False:
        for i in df_sub_tuple:
            print(i)
    else:
        print('No results found.')
        
if __name__ == '__main__':
    pattern2(arg)

