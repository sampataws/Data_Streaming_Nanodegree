"""
Exercise: Generate Progress Report
Requirements:

* Add and change the value of maxRatePerPartition in your option
* Change the value of trigger
* Change the value of startingOffsets
* Again, you can use any Kafka library (pykafka, kafka, kafka-confluent, etc). \
But if you wish to use a library other than kafka-confluent or kafka-python, you will have to reinstall the library each time you wake up workspace (or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button). The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server.


"""

import logging
from pyspark.sql import SparkSession


def run_spark_job(spark):
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:<your port>") \
        .option("subscribe", "<your topic name>") \
        .option("startingOffsets", "earliest") \
        .option("maxOffsetsPerTrigger", 10) \
        .option("maxRatePerPartition", 10) \
        .option("stopGracefullyOnShutdown", "true") \
        .load()

    # Show schema for the incoming resources for checks
    df.printSchema()

    agg_df = df.count()

    # play around with processingTime to see how the progress report changes
    query = agg_df \
        .writeStream \
        .trigger(processingTime="<change this>") \
        .outputMode('Complete') \
        .format('console') \
        .option("truncate", "false") \
        .start()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("StructuredStreamingSetup") \
        .getOrCreate()

    logger.info("Spark started")

    run_spark_job(spark)

    spark.stop()
