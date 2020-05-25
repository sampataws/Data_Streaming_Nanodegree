###Recap on JOINs, Aggregation, and Watermark
JOINs, Aggregation, and Watermark are all commonly used Structured Streaming APIs.

* Types of JOINs
In streaming, we have to think about static vs. streaming DataFrames. Inner JOINs can be easily applied to static and streaming DataFrames, regardless of which one is the left or right table. Outer JOINs are much more difficult because we have to think about late arriving data, and to join on late arriving data, the results will be significantly inconsistent.

* Aggregation vs. Stateful Aggregation
You can think of aggregation as a plain ```sum()``` or ```count()``` in a SQL query. Stateful aggregation involves intervals, which means aggregation over certain intervals. We apply the concept of watermark to achieve stateful aggregation.

* Watermark
Watermark addresses two main problems - dealing with late arriving data and stateful aggregation. Watermark decides which data can be dropped or included - this implies that the application doesn’t have to worry about deciding which data should be ingested in the pipeline, rather, watermark already acknowledges which data can be ingested. Also you can achieve stateful aggregation by setting watermark.


NOTE:

Which of these JOINs require Watermark? (may be more than one answer) ?

* Answer) Stream and Stream LEFT OUTER JOIN