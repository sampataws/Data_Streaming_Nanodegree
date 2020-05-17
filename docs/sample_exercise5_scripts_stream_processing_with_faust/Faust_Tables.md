##Faust Tables
* [Faust tables are defined with ```app.Table``` and take a table name and default type argument.](https://faust.readthedocs.io/en/latest/userguide/tables.html#basics)
* Tables must be [co-partitioned with the streams they are aggregating](https://faust.readthedocs.io/en/latest/userguide/tables.html#id3). Use the ```group_by``` operation to ensure co-partitioning.
* Tables which are not co-partitioned may lead to inaccurate results.