###State Store Recap
State management became important when we entered the streaming realm. You always want to save the metadata and data for the state for many purposes - like logging, metrics, metadata about your data, etc.

Storing the location of your state also became important - where would you want to save these data so that you can retrieve them later?

We’ll begin looking at strategies of using checkpointing and proper state storage next.

###State Management in DStream and Structured Streaming
Since DStream is built on top of Spark RDD, we can operate transformation and action functions on DStream like we do on Spark RDD. Now that we're dealing with interval, another concept in transformation is introduced - stateless transformation and stateful transformation. We'll go over what is considered "state" in Spark Streaming in future lessons.

Stateless transformations are like map(), filter(), and reduceByKey(). As previously stated, each DStream is a continuous stream of RDDs. This type of transformation is applied to each RDD.

Stateful transformations track data across time. This means that the stateful transformation requires some shuffles between keys in key/value pair. The two main types of shuffles are windowed operations:

* ```updateStateByKey()``` - Used to track state across events for each key. ```updateStateByKey()``` iterates over all incoming batches and affects performance when dealing with a large dataset.
* ```mapWithState()``` - Only considers a single batch at a time and provides timeout mechanism.

Further optional reading on stateful transformations: https://databricks.com/blog/2016/02/01/faster-stateful-stream-processing-in-apache-spark-streaming.html