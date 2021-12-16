'''
Find name of actor who has played in the most number of films, use ‘.show()’ to output your 
result, your columns’ name and order should look EXACTLY like: 
|first_name|last_name|
'''

from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q3_c").getOrCreate()

df1 = spark.read.csv('film.csv', header=True)
df2 = spark.read.csv('film_actor.csv', header=True)
df3 = spark.read.csv('actor.csv', header=True)

film_rdd_c = df2.groupby(['actor_id']).count().orderBy('count', ascending=False).limit(1).join(df3, df2.actor_id==df3.actor_id)[['first_name', 'last_name']].rdd
res = film_rdd_c.take(1)

for first, last in res:
	print(first, last)