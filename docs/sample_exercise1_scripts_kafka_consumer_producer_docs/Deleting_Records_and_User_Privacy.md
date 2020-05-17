###Deleting Records and User Privacy

* Privacy regulations like GDPR and CCPA are increasingly common and require applications to give users the right to be forgotten
* You can accomplish this with message expiration on topics that is of shorter duration than your requirement
* You may also use log compaction with null messages to delete data
* The best approach is to use [Daniel Lebrero’s Encrypted User Keys strategy](https://danlebrero.com/2018/04/11/kafka-gdpr-event-sourcing/)


###Optional Further Research - Removing Records and Data Privacy

* [Confluent blog post on GDPR and the right to be forgotten](https://www.confluent.io/blog/handling-gdpr-log-forget/)
* [Daniel Lebrero’s Encrypted User Keys strategy](https://danlebrero.com/2018/04/11/kafka-gdpr-event-sourcing/)