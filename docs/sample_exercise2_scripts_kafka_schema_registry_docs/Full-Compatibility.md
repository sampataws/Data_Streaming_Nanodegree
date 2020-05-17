##Full Compatibility
* [Full compatibility](https://docs.confluent.io/current/schema-registry/avro.html#full-compatibility) means that consumers developed against the latest schema can consume data using the previous schema, and that consumers developed against the previous schema can consume data from the latest schema as well. In other words, full compatibility means that a schema change is both forward and backward compatible.
  * Changing the default value for a field is an example of a full compatible change.
  * The order in which producers or consumers are updated does not matter.
* The ```FULL``` compatibility type indicates that data produced is both forward and backward compatible with the current (N) and previous (N-1) schema.
* The ```FULL_TRANSITIVE``` compatibility type indicates that data produced is both forward and backward compatible with the current (N) and all previous (1 → N-1) schemas.