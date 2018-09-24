__author__ = 'Hk4Fun'
__date__ = '2018/9/24 18:34'

from dynamic_array import DynamicArray
from exceptions import EmptyError, FullError


class LoopQueue:
    def __init__(self, capacity):
        self._capacity = capacity + 1 # important!
        self._data = DynamicArray()
        self._front = self._tail = self._size = 0

    def __repr__(self):
        s = ''
        i = self._front
        while self._front != self._tail:
            s += str(self._data[i]) + ','
        return 'Queue: front [{}] tail'.format(s[:-1])

    def __len__(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity - 1

    def front(self):
        if self.is_empty():
            raise EmptyError('Queue is empty')
        return self._data[self._front]

    def enqueue(self, e):
        if self.is_full():
            raise FullError('Queue is full')
        self._data[self._tail] = e
        self._size += 1
        self._tail = (self._tail + 1) % self._capacity

    def dequeue(self):
        front = self.front()
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return front

    def is_empty(self):
        return self._front == self._tail

    def is_full(self):
        return (self._tail + 1) % self._capacity == self._front
