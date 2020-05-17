###REST Proxy Producer
* **POST** [data to](https://docs.confluent.io/current/kafka-rest/api.html#post--topics-(string-topic_name)) ```/topics/<topic_name>``` [to produce data](https://docs.confluent.io/current/kafka-rest/api.html#post--topics-(string-topic_name))
* The Kafka data may be POSTed in Binary, JSON, or Avro
* When sending Avro data you must always include the schema data as a string
* [Always check your Content-Type header to ensure that it is correctly configured](https://docs.confluent.io/current/kafka-rest/api.html#content-types)
  * Content-Type is in the format ```application/vnd.kafka[.embedded_format].[api_version]+[serialization_format]```
  * ```embedded_format``` is how the data destined for Kafka is formatted. Must be one of ```binary```, ```json```, or ```avro```
  * ```api_version``` is the API version for REST Proxy -- this should always be ```v2``` as of this writing
    * ```serialization_format``` has nothing to do with your Kafka data, this is how the actual data being sent to REST proxy is serialized. Only ```json``` is supported for now -- so always set this to ```json```!
* When using REST Proxy, always start by ensuring that the ```Content-Type``` is correctly set before running your code. A misconfigured ```Content-Type``` can lead to confusing and hard-to-debug errors.