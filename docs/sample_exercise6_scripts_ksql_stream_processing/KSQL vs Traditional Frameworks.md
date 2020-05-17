##KSQL vs. Traditional Frameworks
**Pros**
* It is often simpler to use KSQL and SQL than to build and deploy an entire application
* KSQL is typically a better fit for rapid experimentation and exploration than a full stream processing application
* KSQL doesn’t require a particular programming language, like Python for Faust, or Java for Kafka Streams
* KSQL already comes bundled with standard logs, metrics, and tooling for you to use, so you don’t have to build it yourself

**Cons**

* SQL does not always best capture certain types of data manipulation or remapping scenarios
* Can’t just use whatever other libraries you want like you can with Faust
  * However, KSQL does allow User Defined Functions (UDFs), written in Java