__author__ = 'Hk4Fun'
__date__ = '2018/9/28 2:05'

from abc import ABCMeta, abstractmethod
from exceptions import EmptyError, FullError


class Queue(metaclass=ABCMeta):
    def __init__(self, capacity=None):
        self._capacity = capacity
        self._data = self._init_data()

    @abstractmethod
    def __repr__(self):
        pass

    def __len__(self):
        return len(self._data)

    @abstractmethod
    def _init_data(self):
        pass

    @property
    def capacity(self):
        if self._capacity is not None:
            return self._capacity
        return float('inf')

    def enqueue(self, e):
        if self.is_full():
            raise FullError('{} is full'.format(type(self).__name__))
        self._enqueue(e)

    @abstractmethod
    def _enqueue(self, e):
        pass

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._dequeue()

    @abstractmethod
    def _dequeue(self):
        pass

    def front(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._get_front()

    @abstractmethod
    def _get_front(self):
        pass

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) == self.capacity
