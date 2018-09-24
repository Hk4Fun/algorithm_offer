__author__ = 'Hk4Fun'
__date__ = '2018/9/24 16:26'

from dynamic_array import DynamicArray
from exceptions import EmptyError

class ArrayStack:
    def __init__(self):
        self._data = DynamicArray()

    def __repr__(self):
        return 'Stack: bottom [{}] top'.format(','.join(map(str, self._data)))

    def __len__(self):
        return len(self._data)

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data[-1]

    def is_empty(self):
        return len(self) == 0
