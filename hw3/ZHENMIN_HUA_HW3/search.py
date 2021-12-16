#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector

db = mysql.connector.connect(user='dsci551', password='Dsci-551', host='127.0.0.1', database='sakila')
cur = db.cursor()

sql1 = "SELECT COUNT(*) FROM nicer_but_slower_film_list WHERE actors LIKE '%Temple%'"
cur.execute(sql1)
result1 = cur.fetchall() #return list of tuples
print(str(result1[0][0])+' films in total.')

print()

sql2 = "SELECT title, FID, actors FROM nicer_but_slower_film_list WHERE actors LIKE '%Temple%'"
cur.execute(sql2)
result2 = cur.fetchall()
lst = [list(i) for i in result2]  #[['','',''],...]
for i in lst:
    i[2] = i[2].split(', ')
    for name in i[2].copy():
        if 'Temple' not in name:
            i[2].remove(name)
for row in lst:
    if len(row[2])>1:
        print(' and '.join(row[2])+' play '+row[0]+'('+str(row[1])+')')
    else:
        print(row[2][0]+' plays '+row[0]+'('+str(row[1])+')')

cur.close()
db.close()

