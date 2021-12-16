from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q2_a").getOrCreate()

films = spark.read.csv('film.csv', header=True)

films[(films.rating=='PG') | (films.rating=='PG-13')].agg(fc.count('*').alias('count'))[['count']].show()
