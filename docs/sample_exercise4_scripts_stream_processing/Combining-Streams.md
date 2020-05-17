##Combining Streams
* Combining, or joining, streams is the action of taking one or more streams and creating a single new output stream.
* Joined streams always share some common attribute across the data in all of the streams. For example, we might use a ```user_id``` to merge user streams.
* State must be kept as events flow through the join calculation, until all of the related data has arrived. Once this happens, the new event can be emitted, and the state can be flushed
  * If the related data never fully arrives, at some point the data in memory should be cleared
  * This process is typically accomplished through windowing, which is covered in a later section of this lesson.