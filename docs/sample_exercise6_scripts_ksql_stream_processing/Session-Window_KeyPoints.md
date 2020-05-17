##Session Windowing - Key Points
* Keeps track of differences between the time a key was last seen and the current key arrival time.
* If the difference between the time a key was last seen and the current key arrival time, for two records with the same key, is larger than the session window length defined, a new window is started.
* If the difference between the time a key was last seen and the current key arrival time, for two records with the same key, is less than the session window length, the record is added to the current window, and the session expiration time is started anew.
  * Session expiration denotes that the full session period begins again
* [KSQL Session window documentation](https://docs.confluent.io/current/ksql/docs/concepts/time-and-windows-in-ksql-queries.html#session-window)