from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q2_d").getOrCreate()

df1 = spark.read.csv('film.csv', header=True)

df1[df1.length >= 60].groupby('rating').agg(fc.round(fc.avg('rental_rate'),2).alias('avg_rate'), fc.count('*').alias('cnt')).filter('cnt >= 160')[['rating', 'avg_rate']].show()