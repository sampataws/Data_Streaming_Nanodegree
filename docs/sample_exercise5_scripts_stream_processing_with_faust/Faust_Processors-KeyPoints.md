##Faust Processors - Key Points
* [Processors are functions that take a value and return a value and can be added in a pre-defined list of callbacks to your stream declarations](https://faust.readthedocs.io/en/latest/userguide/streams.html#id2)
* Processors promote reusability and clarity in your code
* Processors may execute synchronously or asynchronously within the context of your code
* All defined processors will run, in the order they were defined, before the final value is generated.