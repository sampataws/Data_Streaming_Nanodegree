###Glossary of Key Terms You Will Learn in this Lesson
* Kafka Connect - A web server and framework for integrating Kafka with external data sources such as SQL databases, log files, and HTTP endpoints.
* JAR - Java **AR**chive. Used to distribute Java code reusably in a library format under a single file.
* Connector - A JAR built on the Kafka Connect framework which integrates to an external system to either source or sink data from Kafka
* Source - A Kafka client putting data into Kafka from an external location, such as a data store
* Sink - A Kafka client removing data from Kafka into an external location, such as a data store
* JDBC - Java Database Connectivity. A Java programming abstraction over SQL database interactions.
* Task - Responsible for actually interacting with and moving data within a Kafka connector. One or more tasks make up a connector.
* Kafka REST Proxy - A web server providing APIs for producing and consuming from Kafka, as well as fetching cluster metadata.