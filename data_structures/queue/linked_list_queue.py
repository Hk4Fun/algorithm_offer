__author__ = 'Hk4Fun'
__date__ = '2018/9/28 1:55'

from queue import Queue
from single_list import SingleList, Node


class LinkedListQueue(Queue):
    def __init__(self, capacity=None):
        super().__init__(capacity)

    def __repr__(self):
        return '{}: front [{}] tail'.format(type(self).__name__, ','.join(map(lambda node: str(node.val), self._data)))

    def _init_data(self):
        return SingleList()

    def _enqueue(self, e):
        self._data.add_last(Node(e))

    def _dequeue(self):
        return self._data.pop(0).val

    def _get_front(self):
        return self._data[0].val