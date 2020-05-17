###Intro to Spark UI/DAGs
Spark UI is a web interface that gets created when you submit a Spark job. It's a convenient resource for the developer to monitor the status of the job execution. The developer can inspect jobs, stages, storages, environment, and executors in this page, as well as the visualized version of the DAGs (Directed Acyclic Graph) of the Spark job.


###Spark DAGs
At any level, when an action is called on the RDD, Spark generates a DAG. One different thing to note about DAGs is that, unlike Hadoop MapReduce, which creates a Map stage and a Reduce stage, DAGs in Spark can contain many stages.

The DAG scheduler divides operators into stages of tasks, and also puts operators together in the most optimized way.