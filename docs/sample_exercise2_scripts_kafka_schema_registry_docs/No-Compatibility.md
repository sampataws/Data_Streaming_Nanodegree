###No Compatibility (NONE Compatibility)
* No compatibility disables compatibility checking by Schema Registry.
  * In this mode, Schema Registry simply becomes a schema repository.
  * Use of NONE compatibility is not recommended.
* Schemas will sometimes need to undergo a change that is neither forward nor backward compatible.
  * >Best practice is to create a new topic with the new schema and update consumers to use that new topic.
  * Managing multiple incompatible schemas within the same topic leads to runtime errors and code that is difficult to maintain.