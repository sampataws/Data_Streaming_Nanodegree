##Consumer Groups - Key Points

* All Kafka Consumers belong to a Consumer group
  * The ```group.id``` [parameter](https://docs.confluent.io/current/installation/configuration/consumer-configs.html#) is required and identifies the globally unique consumer group
  * Consumer groups consist of one or more consumers

* Consumer groups increase throughput and processing speed by allowing many consumers of topic data. However, only one consumer in the consumer group receives any given message.

*If your application needs to inspect every message in a topic, create a consumer group with a single member

* Adding or removing consumers causes Kafka to rebalance
  * During a rebalance, a broker group coordinator identifies a consumer group leader
  * The consumer group leader reassigns partitions to the current consumer group members
  * During a rebalance, messages may not be processed or consumed