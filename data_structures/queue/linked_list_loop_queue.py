__author__ = 'Hk4Fun'
__date__ = '2018/9/28 14:17'

from single_list import Node
from exceptions import EmptyError, FullError


class LinkedListLoopQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._front = self._tail = Node()
        self._init_loop_queue()

    def _init_loop_queue(self):
        cur = self._front
        for _ in range(self._capacity):
            cur._next = Node()
            cur = cur.next
        cur._next = self._front # circular singly linked list

    def __repr__(self):
        cur = self._front
        s = ''
        while cur is not self._tail:
            s += str(cur.val) + ','
            cur = cur.next
        return '{}: front [{}] tail'.format(type(self).__name__, s[:-1])

    def __len__(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity

    def front(self):
        if self.is_empty():
            raise EmptyError('{} is empty'.format(type(self).__name__))
        return self._front.val

    def enqueue(self, e):
        if self.is_full():
            raise FullError('{} is full'.format(type(self).__name__))
        self._tail.val = e
        self._tail = self._tail.next
        self._size += 1

    def dequeue(self):
        front = self.front()
        self._front = self._front.next
        self._size -= 1
        return front

    def is_empty(self):
        return self._front is self._tail

    def is_full(self):
        return self._tail.next is self._front
