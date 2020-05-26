###Scenario 1
Given problem: We're given a hypothetical Spark streaming application. This application receives data from Kafka. Every 2 minutes, you can see that Kafka is producing 60000 records. But at its maximum load, the application takes between 2 minutes for each micro-batch of 500 records. How do we improve the speed of this application?

We can tweak the application's algorithm to speed up the application.

1. Let's say the application's algorithm is tweaked - how can you check if most or all of the CPU cores are working?
   * In a Spark Streaming job, Kafka partitions map 1:1 with Spark partitions. So we can increase Parallelism by increasing the number of partitions in Kafka, which then will increase Spark partitions.

2. We can check if the input data was balanced/unbalanced, skewed or not. We can check the throughput of each partition using Spark UI, and how many cores are consistently working. You can also use the ```htop``` command to see if your cores are all working (if you have a small cluster).
   * Increase driver and executor memory: Out-of-memory issues can be frequently solved by increasing the memory of executor and driver. Always try to give some overhead (usually 10%) to fit your excessive applications.

3. You could also set ```spark.streaming.kafka.maxRatePerPartition``` to a higher number and see if there is any increase in data ingestion.