'''
Find out how many films are rated as either 'PG' or ‘PG-13’, use ‘.show()’ to output your 
result, your columns’ name and order should look EXACTLY like: 
|count|
'''

from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q3_a").getOrCreate()

films = spark.read.csv('film.csv', header=True)
film_rdd_a = films[(films.rating=='PG') | (films.rating=='PG-13')].agg(fc.count('*').alias('count'))[['count']].rdd
res = film_rdd_a.map(lambda x: (x['count'])).collect()

#film_rdd_a = film.rdd
#res = film_rdd_a.filter(lambda r: (r['rating']=='PG') or (r['rating']=='PG-13')).count()

for count in res:
	print(count)