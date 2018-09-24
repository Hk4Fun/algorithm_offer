__author__ = 'Hk4Fun'
__date__ = '2018/9/24 17:19'

import pytest
from array_stack import ArrayStack
from exceptions import EmptyError


class TestArrayStack:
    def test_stack(self):
        stack = ArrayStack()
        assert stack.__repr__() == 'Stack: bottom [] top'
        assert stack.is_empty() == True
        stack.push(1)
        assert stack.is_empty() == False
        assert stack.__repr__() == 'Stack: bottom [1] top'
        stack.push(2)
        assert len(stack) == 2
        assert stack.__repr__() == 'Stack: bottom [1,2] top'
        assert stack.top() == 2
        assert stack.pop() == 2
        assert len(stack) == 1
        assert stack.__repr__() == 'Stack: bottom [1] top'
        assert stack.top() == 1
        assert stack.pop() == 1
        assert stack.__repr__() == 'Stack: bottom [] top'
        with pytest.raises(EmptyError):
            stack.top()
        with pytest.raises(EmptyError):
            stack.pop()
