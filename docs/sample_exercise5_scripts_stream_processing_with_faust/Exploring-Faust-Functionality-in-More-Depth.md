##Exploring Faust Functionality in More Depth
* [See the Faust documentation for in-depth documentation of how Faust works](https://faust.readthedocs.io/en/latest/introduction.html)
* Every Faust application has an ```App``` [which instantiates the top-level Faust application](https://faust.readthedocs.io/en/latest/userguide/application.html#what-is-an-application)
* The application must be assigned a ```topic``` [to subscribe to](https://faust.readthedocs.io/en/latest/userguide/application.html#app-topic-create-a-topic-description)
* An output ```Table``` or stream receives the output of the processing
* An asynchronous function is decorated with an ```agent``` which register the function as a callback for the application when data is received