###Performance Considerations - Summary

* Monitoring Kafka Consumers, Producers, and Brokers for performance is an important part of using Kafka. There are many metrics by which to measure your Kafka cluster. Focus on these key metrics to get started:
  * Consumer Lag: The difference between the latest offset in the topic and the most recently committed consumer offset
  * Producer Response Rate: The rate at which the broker is responding to the producer indicating message status
  * Producer Request Latency: The length of time a producer has to wait for a response from the broker after sending a message
  * Broker Disk Space
  * Broker Elections
  
  
 ###Further Research
* [DataDog blog post on monitoring Kafka](https://www.datadoghq.com/blog/monitoring-kafka-performance-metrics)
* [Confluent article on monitoring Kafka](https://docs.confluent.io/current/kafka/monitoring.html)
* [New Relic article on monitoring Kafka](https://blog.newrelic.com/engineering/new-relic-kafkapocalypse/)
 