__author__ = 'Hk4Fun'
__date__ = '2018/9/25 0:54'

import pytest
from array_loop_deque import ArrayLoopDeque
from exceptions import EmptyError, FullError


class TestArrayLoopDeque:
    def test_empty_queue(self):
        queue = ArrayLoopDeque(0)
        assert queue.is_empty() == True
        assert queue.is_full() == True
        assert queue.capacity == 0
        assert queue.__repr__() == 'ArrayLoopDeque: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.tail()
        with pytest.raises(FullError):
            queue.push_tail(1)
        with pytest.raises(FullError):
            queue.push_front(1)
        with pytest.raises(EmptyError):
            queue.pop_tail()
        with pytest.raises(EmptyError):
            queue.pop_front()

        queue = ArrayLoopDeque(3)
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.tail()
        with pytest.raises(EmptyError):
            queue.pop_tail()
        with pytest.raises(EmptyError):
            queue.pop_front()

    def test_queue(self):
        queue = ArrayLoopDeque(3)
        queue.push_front(1)
        queue.push_tail(2)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [1,2] tail'
        assert len(queue) == 2
        assert queue.front() == 1
        assert queue.tail() == 2

        queue.push_tail(3)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [1,2,3] tail'
        assert len(queue) == 3
        assert queue.front() == 1
        assert queue.tail() == 3
        with pytest.raises(FullError):
            queue.push_front(4)

        assert queue.pop_front() == 1
        assert queue.pop_tail() == 3
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [2] tail'
        assert len(queue) == 1
        assert queue.front() == 2
        assert queue.tail() == 2

        assert queue.pop_front() == 2
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.tail()
        with pytest.raises(EmptyError):
            queue.pop_tail()
        with pytest.raises(EmptyError):
            queue.pop_front()

        queue.push_tail(4)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [4] tail'
        assert len(queue) == 1
        assert queue.front() == 4
        assert queue.tail() == 4

        queue.push_tail(5)
        queue.push_front(6)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopDeque: front [6,4,5] tail'
        assert len(queue) == 3
        assert queue.front() == 6
        assert queue.tail() == 5
        with pytest.raises(FullError):
            queue.push_front(7)
