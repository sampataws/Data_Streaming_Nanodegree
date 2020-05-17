###Example of Spark UI, DAGs, stages and code
This is the code that was used to generate the image below.

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .config('spark.ui.port', 3000) \
        .master("local[2]") \
        .appName("data exploration") \
        .getOrCreate()

spark.conf.set('spark.executor.memory', '3g')
spark.conf.set('spark.executor.cores', '3g')

df = spark.read.csv('AB_NYC_2019.csv', header=True)
df1 = df.select('neighbourhood', 'price').distinct()
import pyspark.sql.functions
df1.rdd.getNumPartitions()
df1.repartition(10).agg({"price": "max"}).collect()
```
This will give you some nonsense data at the end, but we can take a closer look at how the tasks were split.

Since the code annotates ```local[2]```, it's using 2 partitions at the beginning. ```local[*]``` means ```local[{Runtime.getRuntime.availableProcessors()}]```. And then depending on the data, there are 200 tasks. Then there is ```repartition(10)``` which brought down the number of tasks to 10. Finally the last ```collect()``` has 1 task.
![Image description](/Users/sampatbudankayala/PycharmProjects/UdacityStreaming/docs_spark/sample_exercise3_intro_to_spark_streaming/Dag.png)
![Image description](/Users/sampatbudankayala/PycharmProjects/UdacityStreaming/docs_spark/sample_exercise3_intro_to_spark_streaming/QueryPlan.png)



