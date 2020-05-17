###Retrieving Data from Kafka - Key Points

* Most Kafka Consumers will have a “poll” loop which loops infinitely and ingests data from Kafka
* Here is a sample poll loop:
    ```
    while True:
    message = c.poll(1.0)
    if message is None:
        print("no message received by consumer")
    elif message.error() is not None:
        print(f"error from consumer {message.error()}")
    else:
        print(f"consumed message {message.key()}: {message.value()}")
  ```
* It is possible to use either ```poll``` or ```consume```, but ```poll``` is slightly more feature rich
* Make sure to call ```close()``` on your consumer before exiting and to consume any remaining messages
  * Failure to call ```close``` means the Kafka Broker has to recognize that the consumer has left the consumer group, which takes time and failed messages. Try to avoid this if you can.