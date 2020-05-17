###Glossary of Key Terms You Will Learn in this Lesson
* ```RDD (Resilient Distributed Dataset)``` : The fundamental data structure of the Spark Core component. An immutable distributed collection of objects.
* ```DataFrame``` : A data structure of the Spark SQL component. A distributed collection of data organized into named columns.
* ```Dataset``` : A data structure of the Spark SQL component. A distributed collection of data organized into named columns and also strongly typed.
* ```DAG (Directed Acyclic Graph)``` : Each Spark job creates a DAG which consists of task stages to be performed on the clusters.
* ```Logical plan``` : A pipeline of operations that can be executed as one stage and does not require the data to be shuffled across the partitions — for example, map, filter, etc.
* ```Physical plan``` : The phase where the action is triggered, and the DAG Scheduler looks at lineage and comes up with the best execution plan with stages and tasks together, and executes the job into a set of tasks in parallel.
* ```DAG Scheduler``` : DAG scheduler converts a logical execution plan into physical plan.
* ```Task``` : A task is a unit of work that is sent to the executor.
* ```Stage``` : A collection of tasks.
* ```State``` : Intermediary and arbitrary information that needs to be maintained in streaming processing.
* ```Lineage Graph```: A complete graph of all the parent RDDs of an RDD. RDD Lineage is built by applying transformations to the RDD.