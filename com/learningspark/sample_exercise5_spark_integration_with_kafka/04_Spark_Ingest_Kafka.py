"""Exercise: Kafka Source Provider
Using the Kafka Producer Server you created in the previous exercise,
 we can now ingest data from the Kafka Producer Server to a Structured Streaming application.
 First you’ll need to set up the entry point for the stream.

Requirements:

* Set up the entry point
* Use appropriate configurations in the options to ingest the Kafka stream
* Do a df.printSchema() to explore the schema of the default Kafka ingestion
* You can use any Kafka library (pykafka, kafka, kafka-confluent, etc). \
  But if you wish to use a library other than kafka-confluent or kafka-python, \
  you will have to reinstall the library each time you wake up workspace \
 (or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button).
  The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server."""
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
        .option("stopGracefullyOnShutdown", "true") \
        .load()

    # Show schema for the incoming resources for checks
    df.printSchema()


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
