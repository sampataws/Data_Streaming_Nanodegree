###RDD Key Points
* RDD stands for Resilient Distributed Dataset:
  * Resilient because its fault-tolerance comes from maintaining RDD lineage, so even with loss during the operations, you can always go back to where the operation was lost.
  * Distributed because the data is distributed across many partitions and workers.
  * Dataset is a collection of partitioned data. RDD has characteristics like in-memory, immutability, lazily evaluated, cacheable, and typed (we don't see this much in Python, but you'd see this in Scala or Java).