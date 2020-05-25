###Action and Transformation Functions in RDDs and DataFrames
There are two types of Apache Spark RDD operations - transformations and actions. Transformations produce a new RDD from an existing RDD. Actions trigger evaluation of expressions and send data back to the driver.

Transformations build an RDD lineage. For example, this code ```rdd.map().filter().join().repartition()``` builds a lineage of map -> filter -> join -> repartition. You can see this lineage through the ```.explain``` operation or through the Spark UI.

The resulting RDD from a transformation is always different from its parent RDD. It can be smaller or bigger or the same size (e.g. map).

Transformations also have two types of operations - narrow and wide. Narrow is map-like, and wide is reduce-like.

When the action is triggered, the computation is sent back to the driver. You may persist an RDD in memory using the ```persist``` method if there are many transformations and actions applied, so that Spark keeps the RDD around the cluster for faster access the next time.