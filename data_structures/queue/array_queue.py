__author__ = 'Hk4Fun'
__date__ = '2018/9/24 17:35'

from dynamic_array import DynamicArray
from exceptions import EmptyError, FullError


class ArrayQueue:
    def __init__(self, capacity=None):
        self._capacity = capacity
        self._data = DynamicArray()

    def __repr__(self):
        return 'Queue: front [{}] tail'.format(','.join(map(str, self._data)))

    def __len__(self):
        return len(self._data)

    @property
    def capacity(self):
        if self._capacity is not None:
            return self._capacity
        return float('inf')

    def enqueue(self, e):
        if self.is_full():
            raise FullError('Queue is full')
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('Queue is empty')
        return self._data.pop(0)

    def front(self):
        if self.is_empty():
            raise EmptyError('Queue is empty')
        return self._data[0]

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) == self.capacity
