##Sliding Window
* Similar to Hopping Window, except the increment is not directly configurable and updates in real-time
  * A sliding window of the last 12 hours always includes all of the last 12 hours of data. Data is expired as soon as it reaches the 12-hour threshold, and new data is added as soon as it is received.
* Sliding Windows have no gaps between windows
* Sliding Windows do overlap