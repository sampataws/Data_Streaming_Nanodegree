###Recovery of State
The accumulating result of the state should be stored in a fault-tolerant state store of your choice.

The purpose of state store is to provide a reliable place in your services so that the application (or the developer) can read the intermediary result of stateful aggregations. Even in the case of driver or worker failures, Spark is able to recover the processing state at the point right before the failure. The state stored is supported by HDFS compatible file system. To guarantee recoverability, Spark recovers the two most recent versions. If batch number 10 fails, then the batch number 9 and 8 are both recovered.

We can implement the state store by implementing org.apache.spark.sql.execution.streaming.state.StateStore properties.

###Sample Code for Checkpointing
We are providing the code here rather than in a workspace, because checkpoint requires a HDFS-compatible file system but our classroom workspaces do not currently offer HDFS-compatible file systems.