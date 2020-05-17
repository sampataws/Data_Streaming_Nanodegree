###Windowing in Faust
* Faust provides two windowing methods: hopping and tumbling. In this section, you will learn how to use these windowing approaches.

###Faust Windowing - Key Points
* Faust supports [Hopping](https://faust.readthedocs.io/en/latest/userguide/tables.html#HoppingWindow) and [Tumbling](https://faust.readthedocs.io/en/latest/userguide/tables.html#HoppingWindow) windows
* Windowing applies only to Tables
* Faust provides [semantics for classifying specifically which pool of data is desired from a window](https://faust.readthedocs.io/en/latest/userguide/tables.html#iterating-over-keys-values-items-in-a-windowed-table), such as ```current()```, ```now()```, ```relative_to_now()```, etc.