###Kafka Data Source
KafkaSource is the data source for Apache Kafka in Spark Structured Streaming. It's part of kafka-0-10-sql library in Spark (source code: https://github.com/apache/spark/blob/4513f1c0dc450e9249d43fdad618fdcaf8d399b6/external/kafka-0-10-sql/src/main/scala/org/apache/spark/sql/kafka010/KafkaSource.scala). A couple important functions to note in this source are:

* ```getOffset()```, which uses the KafkaOffsetReader to get the latest available offset
* ```getBatch()```, which returns a DataFrame from the start to end of an offset.

You should define spark-sql-kafka-0-10 module as part of the execution of your project. 
For Spark environments using shell script, we'll be using the following command to submit Spark jobs:

```./bin/spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:2.3.4```

What we’re actually doing here is including an external package to allow us to use Kafka (broker version 0.10), and the correct version of Spark we have installed (compiled with Scala 2.12 and Spark version 2.3.4). org.apache.spark:spark-sql-kafka-0-10_<scala_version>:<spark_version>.


###KafkaSourceProvider Code Reference
KafkaSourceProvider requires these options

* subscribe, subscribepattern, or assign
* kafka.bootstrap.server

```python
kafka_df = spark.readStream.\
  format("kafka").\ # set data ingestion format as Kafka
  option("subscribe", "<topic_name>").\ #This is required although it says option.
  option("kafka.bootstrap.servers", "localhost:9092").\ #You will also need the url and port of the bootstrap server
  load()
```

```Reference```: https://github.com/apache/spark/blob/master/external/kafka-0-10-sql/src/main/scala/org/apache/spark/sql/kafka010/KafkaSourceProvider.scala