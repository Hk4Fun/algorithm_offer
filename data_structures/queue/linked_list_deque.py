__author__ = 'Hk4Fun'
__date__ = '2018/9/28 1:59'

from deque import Deque
from linked_list_queue import LinkedListQueue, Node

class LinkedListDeque(Deque, LinkedListQueue):
    def _push_front(self, e):
        self._data.insert(0, Node(e))

    def _pop_tail(self):
        return self._data.pop().val

    def _get_tail(self):
        return self._data[-1].val
