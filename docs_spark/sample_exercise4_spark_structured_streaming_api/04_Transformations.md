###Transformations
Transformations are one of the two types of Apache Spark RDD operations. Let’s look at a demonstration of how they work.

###Transformations - Key Points
* Transformations in Spark build RDD lineage.
* Transformations are expressions that are lazily evaluated and can be chained together. Then, as we discussed in the previous lesson, Spark Catalyst will use these chains to define stages, based on its optimization algorithm.
* There are two types of transformations - wide and narrow. Narrow transformations have the parent RDDs in the same partition, whereas parent RDDs of the wide transformations may not be in the same partition.