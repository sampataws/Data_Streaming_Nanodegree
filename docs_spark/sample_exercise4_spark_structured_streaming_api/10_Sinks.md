###What are Sinks?
Spark Structured Streaming uses sinks to add the output of each batch to a destination.

Currently these are the following types of sinks supported:

* File sinks
* Kafka sinks
* Foreach and foreachBatch sinks
* Memory sinks
* Console sinks

####Modes for Using Built-in Output Sinks
There are a few modes for writing to output sinks:

* Append - Only new rows are written to the output sink.
* Complete - All the rows are written to the output sink. This mode is used with aggregations.
* Update - Similar to complete, but only the updated rows will be written to the output sink.

####Which Types of Output Sinks are the Most Useful?
Next let’s discuss which types of output sinks are the most useful