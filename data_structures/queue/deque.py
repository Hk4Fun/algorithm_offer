__author__ = 'Hk4Fun'
__date__ = '2018/9/28 2:45'

from queue import Queue
from abc import ABCMeta, abstractmethod
from exceptions import EmptyError, FullError


class Deque(Queue, metaclass=ABCMeta):
    def push_front(self, e):
        if self.is_full():
            raise FullError('{} is full'.format(type(self).__name__))
        self._push_front(e)

    @abstractmethod
    def _push_front(self, e):
        pass

    def push_tail(self, e):
        self.enqueue(e)

    def pop_front(self):
        return self.dequeue()

    def pop_tail(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._pop_tail()

    @abstractmethod
    def _pop_tail(self):
        pass

    def tail(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._get_tail()

    @abstractmethod
    def _get_tail(self):
        pass
