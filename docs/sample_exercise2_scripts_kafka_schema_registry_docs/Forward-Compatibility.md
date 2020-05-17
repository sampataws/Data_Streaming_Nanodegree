##Forward Compatibility
* [Forward compatibility](https://docs.confluent.io/current/schema-registry/avro.html#forward-compatibility) means that consumer code developed against the previous version of an Avro Schema can consume data using the newest version of a schema without modification
  * The deletion of an optional field or the addition of a new field are forward compatible changes
  * Producers need to be updated before consumers
* The ```FORWARD``` compatibility type indicates that data produced with the latest schema (N) is usable by consumers using the previous schema version (N-1)
* The ```BACKWARD_TRANSITIVE``` compatibility type indicates that data produced with the latest schema (N) is usable by all consumers using any previous schema version (1 → N-1)