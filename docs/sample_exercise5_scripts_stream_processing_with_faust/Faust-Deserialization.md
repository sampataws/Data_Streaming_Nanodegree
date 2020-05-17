##Faust Deserialization
Topic deserialization in Faust is a simple and painless process. Similar to how you might specify a schema for key and value to ```confluent_kafka```, with Faust you can provide key and value types. These value types may be primitives such as ```int``` or ```str```, or complex types represented as objects.

##Faust Deserialization - Key Points
* All data model classes must inherit from the **faust.Record** [class](https://faust.readthedocs.io/en/latest/userguide/models.html#records) if you wish to use them with a Faust topic.
* It is a good idea to specify the **serializer** [type on your](https://faust.readthedocs.io/en/latest/userguide/models.html#serialization-deserialization) so that Faust will deserialize data in this format by default.
* It is a good practice to set **validation=True** [on your data models](https://faust.readthedocs.io/en/latest/userguide/models.html#model-validation). When set to true, Faust will enforce that the data being deserialized from Kafka matches the expected type.
  * E.g., if we expect a ```str``` for a field, but receive an ```int```, Faust will raise an error.
* [Use Faust](https://faust.readthedocs.io/en/latest/userguide/models.html#codec-registry) **codecs** [to build custom serialization and deserialization](https://faust.readthedocs.io/en/latest/userguide/models.html#codec-registry)