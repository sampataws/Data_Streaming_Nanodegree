###Kafka Topic Naming Conventions:

* The only enforced rules for topic names are that they must be less than 256 characters, consist only of alphanumeric characters (a-z, A-Z, 0-9), “.”, “_”, or “-”.

* There is no idiomatic or universally correct naming convention.

* Naming conventions can help reduce confusion, save time, and even increase reusability.

* Example of a naming convention:
  * Consider starting with a namespace, like **com.udacity**
  * Consider segmenting on schema or model type, like __com.udacity.lesson__, where lesson is the model
  * Consider segmenting on event type, like __com.udacity.lesson.quiz_complete__, where quiz_complete is the event