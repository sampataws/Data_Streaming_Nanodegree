##Querying Syntax
* ```SELECT``` statements may be run in KSQL CLI, but as soon as the session is terminated, so too is the data calculation.
* Use ```CREATE STREAM <stream_name> AS SELECT…``` and ```CREATE TABLE <table_name> AS SELECT …``` to persist your queries for long-term usage
* [KSQL Querying Syntax Documentation](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#select)
* [See the KSQL documentation for a list of all Scalar functions supported for querying](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#scalar-functions)