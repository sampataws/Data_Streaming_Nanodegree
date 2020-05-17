##Table Creation
* Creating Tables from an underlying topic requires you to specify column names and their types
  * You must also specify the serialization format as one of ```JSON```, ```AVRO```, or ```DELIMITED (csv)```
  * You must also specify the underlying topic name
  * You may create a table from another existing stream or table with ```CREATE STREAM <stream_name> AS SELECT …```
  * [KSQL Key Requirements Documentation](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#ksql-key-requirements)
  * [KSQL Create Table Documentation](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#create-table)
  * [KSQL Create Table from SELECT documentation](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#create-table-as-select)