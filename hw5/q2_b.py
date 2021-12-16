from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
spark = SparkSession.builder.appName("q2_b").getOrCreate()

df1 = spark.read.csv('film.csv', header=True)
df2 = spark.read.csv('film_actor.csv', header=True)
df3 = spark.read.csv('actor.csv', header=True)

df1.join(df2, df1.film_id==df2.film_id).join(df3, df2.actor_id==df3.actor_id)[df1.title=='ANONYMOUS HUMAN'][['first_name', 'last_name']].show()

