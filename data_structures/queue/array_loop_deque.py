__author__ = 'Hk4Fun'
__date__ = '2018/9/25 0:54'

from array_loop_queue import ArrayLoopQueue
from array_deque import ArrayDeque


class ArrayLoopDeque(ArrayLoopQueue, ArrayDeque):
    def _push_front(self, e):
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = e
        self._size += 1

    def _pop_tail(self):
        tail = self.tail()
        self._tail = (self._tail - 1) % self._capacity
        self._size -= 1
        return tail

    def _get_tail(self):
        return self._data[self._tail - 1]
