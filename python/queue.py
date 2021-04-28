"""
  It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue.
  It needs the item and returns nothing.
* dequeue() removes the front item from the queue.
  It needs no parameters and returns the item. The queue is modified.
* isEmpty() tests to see whether the queue is empty.
  It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue.
  It needs no parameters and returns an integer.
* peek() returns the front element of the queue.
"""

# example https://github.com/keon/algorithms/blob/master/algorithms/queues/queue.py

class Queue():
    def __init__(self):
        self.queue = []

if __name__ == "__main__":
    a = Queue()
    print(a)