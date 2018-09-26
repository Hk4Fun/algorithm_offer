__author__ = 'Hk4Fun'
__date__ = '2018/9/25 0:54'

from loop_queue import LoopQueue
from array_deque import ArrayDeque
from exceptions import EmptyError, FullError


class LoopDeque(LoopQueue, ArrayDeque):
    def push_front(self, e):
        if self.is_full():
            raise FullError('{} is full'.format(type(self).__name__))
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = e
        self._size += 1

    def pop_tail(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        tail = self.tail()
        self._tail = (self._tail - 1) % self._capacity
        self._size -= 1
        return tail

    def tail(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._data[self._tail - 1]
