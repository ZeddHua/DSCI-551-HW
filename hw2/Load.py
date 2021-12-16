#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
category = pd.read_csv('category.csv', sep=';')
actor = pd.read_csv('actor.csv', sep=';')
film_actor = pd.read_csv('film_actor.csv', sep=';')
film_category = pd.read_csv('film_category.csv', sep=';')
film = pd.read_csv('film.csv', sep=';')

category_xml = category.to_xml(
    attr_cols=['category_id'],
    elem_cols=['name', 'last_update'],
    root_name='category_table',
    row_name='category',
    index=False,
    xml_declaration=False,
    pretty_print=True)

actor_xml = actor.to_xml(
    attr_cols=['actor_id'],
    elem_cols=['first_name', 'last_name', 'last_update'],
    root_name='actor_table',
    row_name='actor',
    index=False,
    xml_declaration=False,
    pretty_print=True)

film_actor_xml = film_actor.to_xml(
    attr_cols=['film_id', 'actor_id'],
    elem_cols=['last_update'],
    root_name='film_actor_table',
    row_name='film_actor',
    index=False,
    xml_declaration=False,
    pretty_print=True)

film_category_xml = film_category.to_xml(
    attr_cols=['film_id', 'category_id'],
    elem_cols=['last_update'],
    root_name='film_category_table',
    row_name='film_category',
    index=False,
    xml_declaration=False,
    pretty_print=True)

film_xml = film.to_xml(
    attr_cols=['film_id'],
    elem_cols=['title', 'description', 'release_year', 'language_id',
               'original_language_id', 'rental_duration', 'rental_rate', 
               'length','replacement_cost', 'rating', 'special_features', 'last_update'],
    root_name='film_table',
    row_name='film',
    index=False,
    xml_declaration=False,
    pretty_print=True)

merge = '<root>\n' + category_xml + actor_xml + film_actor_xml + film_category_xml + film_xml + '\n</root>'

with open('main.xml', 'w') as f:
    f.write(merge)

