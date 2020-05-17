##Backward Compatibility - Key Points
* [Backward compatibility](https://docs.confluent.io/current/schema-registry/avro.html#backward-compatibility) means that consumer code developed against the most recent version of an Avro Schema can use data using the prior version of a schema without modification.
  * The deletion of a field or the addition of a new optional field are backward compatible changes.
  * Update consumers before updating producers to ensure that consumers can handle the new data type

* The ```BACKWARD``` compatibility type indicates compatibility with the current version ```(N)``` and the immediately prior version ```(N-1)```
  * Unless you specify otherwise, Schema Registry always assumes that changes are BACKWARD compatible

* The ```BACKWARD_TRANSITIVE``` compatibility type indicates compatibility with all prior versions ```(1 → N)```