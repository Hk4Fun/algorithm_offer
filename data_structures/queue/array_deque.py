__author__ = 'Hk4Fun'
__date__ = '2018/9/24 23:03'

from deque import Deque
from array_queue import ArrayQueue


class ArrayDeque(Deque, ArrayQueue):
    def _push_front(self, e):
        self._data.insert(0, e)

    def _pop_tail(self):
        return self._data.pop()

    def _get_tail(self):
        return self._data[-1]
