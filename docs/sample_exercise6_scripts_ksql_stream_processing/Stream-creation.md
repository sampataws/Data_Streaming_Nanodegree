##Stream Creation
* Creating Streams from an underlying topic requires you to specify column names and their types
* You must also specify the serialization format as one of ```JSON```, ```AVRO```, or ```DELIMITED (csv)```
* You must also specify the underlying topic name
* You may create a stream from another existing stream with ```CREATE STREAM <stream_name> AS SELECT …```
* [KSQL Create Stream Documentation](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#create-stream)
* [KSQL Create Stream from SELECT documentation](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#create-stream-as-select)