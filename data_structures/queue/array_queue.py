__author__ = 'Hk4Fun'
__date__ = '2018/9/24 17:35'

from queue import Queue
from dynamic_array import DynamicArray


class ArrayQueue(Queue):
    def __init__(self, capacity=None):
        super().__init__(capacity)

    def __repr__(self):
        return '{}: front [{}] tail'.format(type(self).__name__, ','.join(map(str, self._data)))

    def _init_data(self):
        if self._capacity:
            return DynamicArray(capacity=self._capacity)
        else:
            return DynamicArray()

    def _enqueue(self, e):
        self._data.append(e)

    def _dequeue(self):
        return self._data.pop(0)

    def _get_front(self):
        return self._data[0]
