##Faust Serialization
Serialization in Faust leverages the same ```faust.Record``` rules you just learned about for deserialization. In this section, we’ll learn how Faust manages this process.

##Faust Serialization - Key Points
* Serialization in Faust leverages the same [faust.Record](https://faust.readthedocs.io/en/latest/userguide/models.html#records) that we saw in the deserialization section. Faust runs the serializer in reverse to serialize the data for the output stream.
* [Multiple serialization codecs may be specified for a given model](https://faust.readthedocs.io/en/latest/userguide/models.html#manual-serialization)
  * e.g., ```serialization=”binary|json”```. This means, when serializing, encode to json, then base64 encode the data.