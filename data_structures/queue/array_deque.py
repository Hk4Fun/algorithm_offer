__author__ = 'Hk4Fun'
__date__ = '2018/9/24 23:03'

from array_queue import ArrayQueue
from exceptions import EmptyError, FullError


class ArrayDeque(ArrayQueue):
    def push_front(self, e):
        if self.is_full():
            raise FullError('{} is full'.format(type(self).__name__))
        self._data.insert(0, e)

    def push_tail(self, e):
        self.enqueue(e)

    def pop_front(self):
        return self.dequeue()

    def pop_tail(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._data.pop()

    def tail(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._data[-1]
