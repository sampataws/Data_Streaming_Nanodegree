##Consumer Offsets - Key Points

* Kafka keeps track of what data a consumer has seen with offsets
  * Kafka stores offsets in a private internal topic
  * Most client libraries automatically send offsets to Kafka for you on a periodic basis
  * You may [opt to commit offsets yourself](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html#confluent_kafka.Consumer.commit), but it is not recommended unless there is a specific use-case.
  * Offsets may be sent synchronously or asynchronously
  * Committed offsets determine where the consumer will start up
    * If you want the consumer to start from the first known message, [set ```auto.offset.reset to earliest```]
    * This will only work the first time you start your consumer. On subsequent restarts it will pick up wherever it left off
    * If you always want your consumer to start from the earliest known message, you must [manually assign your consumer to the start of the topic on boot](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=serializer#confluent_kafka.Consumer.assign)