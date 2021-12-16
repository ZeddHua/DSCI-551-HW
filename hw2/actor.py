#!/usr/bin/env python
# coding: utf-8

# In[9]:


import lxml
from lxml import etree
import sys
import pandas as pd

arg = sys.argv[1]

def pattern2(arg):
    arg = arg.upper()
    namelist = arg.split()
    firstname = namelist[0]
    lastname = namelist[1]
    
    with open('main.xml') as f:
        tree = etree.parse(f)
        
    #use actor name to find actor_id in actor_table
    actor_id = tree.xpath("//actor[first_name=$val1 and last_name=$val2]/@actor_id", val1=firstname, val2=lastname)
    
    if actor_id:
        #use actor_id to find film_id in film_actor_table
        film_id = []
        for element in tree.xpath("//film_actor[@actor_id=$val]/@film_id", val=actor_id[0]):
            film_id.append(element)
    
        #use film_id to find related info in film_table
        film_info = []
        for filmid in film_id:
            title = tree.xpath("//film[@film_id=$val]/title/text()", val=filmid)
            release_year = tree.xpath("//film[@film_id=$val]/release_year/text()", val=filmid)
            info = tuple(title + release_year)
            film_info.append(info)
    
        #print
        for i in film_info:
            print(i)
    else:
        print('No results found.')    

#execute
pattern2(arg)

