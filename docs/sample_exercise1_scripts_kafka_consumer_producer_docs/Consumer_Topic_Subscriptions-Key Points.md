##Topic Subscriptions - Key Points

* You subscribe to a topic by specifying its name
  * If you wanted to subscribe to ```com.udacity.lesson.views```, you would simply specify the full name as ```”com.udacity.lesson.views”```
  * Make sure to set ```allow.auto.create.topics``` to **false** so that the topic isn’t created by the consumer if it does not yet exist

* One consumer can subscribe to multiple topics by using a regular expression
  * The format for the regular expression is slightly different. If you wanted to subscribe to ```com.udacity.lesson.views.lesson1``` and ```com.udacity.lesson.views.lesson2``` you would specify the topic name as ```”^com.udacity.lesson.views.*”```
  * The topic name must be prefixed with ”^” for the client to recognize that it is a regular expression, and not a specific topic name
  * Use ```regexp``` to specify your regular expressions.
  * See the ```confluent_kafka_python subscribe()``` documentation for more information