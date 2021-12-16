#!/usr/bin/env python
# coding: utf-8

# In[65]:


import lxml
from lxml import etree
import sys
import pandas as pd

arg = sys.argv[1]

def pattern1(arg):
    i = arg[0].upper()
    i2 = arg[1:].lower()
    arg = i + i2
    
    with open('main.xml') as f:
        tree = etree.parse(f)
        
    #find category_id in category_table
    category_id = tree.xpath("//category[name=$val]/@category_id", val=arg)  
    
    if category_id:
        #use category_id to find film_id in film_category_table
        film_id = []
        for element in tree.xpath("//film_category[@category_id=$val]/@film_id", val=category_id[0]):  
            film_id.append(element)
        
        #use film_id to find needed info in film_table
        film_info = []
        for filmid in film_id:  
            title = tree.xpath("//film[@film_id=$val]/title/text()", val=filmid)
            release_year = tree.xpath("//film[@film_id=$val]/release_year/text()", val=filmid)
            rating = tree.xpath("//film[@film_id=$val]/rating/text()", val=filmid)
            rental_rate = tree.xpath("//film[@film_id=$val]/rental_rate/text()", val=filmid)
            rental_duration = tree.xpath("//film[@film_id=$val]/rental_duration/text()", val=filmid)
            info = tuple(title + release_year + rating + rental_rate + rental_duration)
            film_info.append(info)
        
        #print
        for i in film_info:
            print(i)
    else:
        print('No results found.')

#execute
pattern1(arg)

