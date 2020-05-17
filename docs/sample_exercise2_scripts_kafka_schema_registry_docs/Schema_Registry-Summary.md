##Schema Registry - Summary
* Provides an HTTP REST API for managing Avro schemas
* Many Kafka clients natively support Schema Registry interactions for you
* Reduces network overhead, allowing producers and consumers to register schemas one time
* Simplifies using Avro, reducing the barrier to entry for developers
* Uses a Kafka topic to store state
* Deployed as one or more web servers, with one leader
* Uses ZooKeeper to manage elections


##Schema Registry - Optional Further Research
* ```confluent_kafka_python``` [Avro and Schema Registry support](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=partition#module-confluent_kafka.avro)
* [Schema Registry Overview](https://docs.confluent.io/current/schema-registry/index.html)
* [Schema Registry HTTP API Documentation](https://docs.confluent.io/current/schema-registry/develop/api.html)