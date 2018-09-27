__author__ = 'Hk4Fun'
__date__ = '2018/9/26 19:56'

from single_list import SingleList, Node
from exceptions import EmptyError


class LinkedListStack:
    def __init__(self):
        self._data = SingleList()

    def __repr__(self):
        return 'Stack: bottom [{}] top'.format(','.join(map(lambda node: str(node.val), self._data)))

    def __len__(self):
        return len(self._data)

    def push(self, e):
        self._data.add_last(Node(e))

    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data.pop().val

    def top(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data[-1].val

    def is_empty(self):
        return len(self) == 0
