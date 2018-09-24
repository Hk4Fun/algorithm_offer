__author__ = 'Hk4Fun'
__date__ = '2018/9/24 23:03'

from dynamic_array import DynamicArray
from exceptions import EmptyError, FullError


class ArrayDeque:
    def __init__(self, capacity=None):
        self._data = DynamicArray()
        self._capacity = capacity

    def __repr__(self):
        return 'ArrayDeque: front [{}] tail'.format(','.join(map(str, self._data)))

    def __len__(self):
        return len(self._data)

    @property
    def capacity(self):
        if self._capacity is not None:
            return self._capacity
        return float('inf')

    def push_front(self, e):
        if self.is_full():
            raise FullError('Deque is full')
        self._data.insert(0, e)

    def push_tail(self, e):
        if self.is_full():
            raise FullError('Deque is full')
        self._data.append(e)

    def pop_front(self):
        if self.is_empty():
            raise EmptyError('Deque is empty')
        return self._data.pop(0)

    def pop_tail(self):
        if self.is_empty():
            raise EmptyError('Deque is empty')
        return self._data.pop()

    def front(self):
        if self.is_empty():
            raise EmptyError('Deque is empty')
        return self._data[0]

    def tail(self):
        if self.is_empty():
            raise EmptyError('Deque is empty')
        return self._data[-1]

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) == self.capacity
