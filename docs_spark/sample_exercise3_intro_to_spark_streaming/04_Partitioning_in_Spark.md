###Partitioning in Spark
By default in Spark, a partition is created for each block of the file in HDFS (128MB is the default setting for Hadoop) if you are using HDFS as your file system. If you read a file into an RDD from AWS S3 or some other source, Spark uses 1 partition per 32MB of data. There are a few ways to bypass this default upon creation of an RDD, or reshuffling the RDD to resize the number of partitions, by using ```rdd.repartition(<the partition number you want to repartition to>)```. For example, ```rdd.repartition(10)``` should change the number of partitions to 10.

In local mode, Spark uses as many partitions as there are cores, so this will depend on your machine. You can override this by adding a configuration parameter ```spark-submit --conf spark.default.parallelism=<some number>.```

So hypothetically, if you have a file of 200 MB and if you were to load this into an RDD, how many partitions will this RDD have? If this file is on HDFS, this will produce 2 partitions (each of them being 128MB). If the file is on AWS S3 or some other file system, it will produce 7 partitions.

####Hash Partitioning
Hash partitioning in Spark is not different than the normal way of using a hash key in the data world to distribute data across partitions uniformly.

Usually this is defined by

```partition = key.hashCode() % numPartitions```

This mode of partitioning is used when you want to evenly distribute your data across partitions.

####Range Partitioning
Range partitioning is another well-known partitioning method in the data world. Range partitioning divides each partition in a continuous but non-overlapping way.

Let's pretend there is a table called ```employees```, and it has the following schema:
```csv
CREATE TABLE employees (
    employee_id INT NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    ...
)
```
Range partitioning would come into play where you partition the ```employees table``` by ```employee_id```, like this:
```csv
PARTITION BY RANGE (employee_id) (
    PARTITION p0 VALUES LESS THAN (11),
    PARTITION p0 VALUES LESS THAN (21),
    PARTITION p0 VALUES LESS THAN (31),
    ...
)
```
In reality, you'd want to use range partition over a timestamp, but this example gives you a rough idea of what range partitioning means.

You can use the ```partitionByRange()``` function to partition your data into some kind of group. Range partitioning in Spark ensures that every range is contained in a single partition. This becomes useful when you want to reduce shuffles across machines, for example when you know for sure all your parent RDDs need to stay in the same partition.