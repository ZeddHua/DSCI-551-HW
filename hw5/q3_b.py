'''
Find first and last name of actors who have played in the film 'ANONYMOUS HUMAN’, use 
‘.show()’ to output your result, your columns’ name and order should look EXACTLY like: 
|first_name|last_name|
'''

from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q3_b").getOrCreate()

df1 = spark.read.csv('film.csv', header=True)
df2 = spark.read.csv('film_actor.csv', header=True)
df3 = spark.read.csv('actor.csv', header=True)

film_rdd_b = df1.join(df2, df1.film_id==df2.film_id).join(df3, df2.actor_id==df3.actor_id).rdd
res = film_rdd_b.filter(lambda r: r['title'] == 'ANONYMOUS HUMAN').map(lambda x: (x['first_name'], x['last_name'])).collect()

for first, last in res:
	print(first, last)