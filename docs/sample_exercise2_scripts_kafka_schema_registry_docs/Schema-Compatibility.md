##Schema Compatibility
* The process of schema change is known as Schema Evolution
* Schema Evolution is caused by a modification to an existing data schema
  * Adding or removing a field
  * Making a field optional
  * Changing a field type
* Schema Registry can track schema compatibility between schemas
  * Compatibility is used to determine whether or not a particular schema version is usable by a data consumer
  * Consumers may opt to use this compatibility information to preemptively refuse to process data that is incompatible with its current configuration
  * Schema Registry supports [four categories of compatibility](https://docs.confluent.io/current/schema-registry/avro.html)
  * Backward / Backward Transitive
  * Forward / Forward Transitive
  * Full / Full Transitive
  * None
* Managing compatibility requires both producer and consumer code to determine the compatibility of schema changes and send those updates to Schema Registry