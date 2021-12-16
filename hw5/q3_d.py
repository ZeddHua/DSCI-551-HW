'''
SELECT rating, avg(rental_rate)
FROM film
where length >= 60
group by rating
having count(*) >= 160 
use ‘.show()’ to output your result, and round ‘avg_rate’ to 2 decimal with 
pyspark.sql.functions.round (aka. fc.round)
your columns’ name and order should look EXACTLY like: 
|rating|avg_rate|
'''

from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q3_d").getOrCreate()

df1 = spark.read.csv('film.csv', header=True)

film_rdd_d = df1[df1.length >= 60].groupby('rating').agg(fc.avg('rental_rate').alias('avg_rate'), fc.count('*').alias('cnt')).filter('cnt >= 160')[['rating', 'avg_rate']].rdd
res = film_rdd_d.collect()

for rating, avg in res:
	print(rating, "{:.2f}".format(avg))
