__author__ = 'Hk4Fun'
__date__ = '2018/9/28 14:40'

from single_list import Node as N
from linked_list_loop_queue import LinkedListLoopQueue
from linked_list_deque import LinkedListDeque


class Node(N):
    def __init__(self, val=None, next=None, pre=None):
        super().__init__(val, next)
        self._pre = pre

    @property
    def pre(self):
        return self._pre


class LinkedListLoopDeque(LinkedListLoopQueue, LinkedListDeque):
    def _init_loop_queue(self):
        self._front = self._tail = Node()  # which has 'pre' attribute
        cur = self._front
        for i in range(self._capacity):
            cur._next = Node(pre=cur)
            cur = cur.next
        cur._next = self._front
        self._front._pre = cur  # circular doubly linked list

    def _push_front(self, e):
        self._front = self._front.pre
        self._front.val = e
        self._size += 1

    def _pop_tail(self):
        tail = self.tail()
        self._tail = self._tail.pre
        self._size -= 1
        return tail

    def _get_tail(self):
        return self._tail.pre.val
