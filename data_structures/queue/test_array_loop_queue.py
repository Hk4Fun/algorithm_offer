__author__ = 'Hk4Fun'
__date__ = '2018/9/24 18:35'

import pytest
from array_loop_queue import ArrayLoopQueue
from exceptions import EmptyError, FullError


class TestArrayLoopQueue:
    def test_empty_queue(self):
        queue = ArrayLoopQueue(0)
        assert queue.is_empty() == True
        assert queue.is_full() == True
        assert queue.capacity == 0
        assert queue.__repr__() == 'ArrayLoopQueue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()
        with pytest.raises(FullError):
            queue.enqueue(1)

        queue = ArrayLoopQueue(3)
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

    def test_queue(self):
        queue = ArrayLoopQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [1,2] tail'
        assert len(queue) == 2
        assert queue.front() == 1

        queue.enqueue(3)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [1,2,3] tail'
        assert len(queue) == 3
        assert queue.front() == 1
        with pytest.raises(FullError):
            queue.enqueue(4)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [3] tail'
        assert len(queue) == 1
        assert queue.front() == 3

        assert queue.dequeue() == 3
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

        queue.enqueue(4)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [4] tail'
        assert len(queue) == 1
        assert queue.front() == 4

        queue.enqueue(5)
        queue.enqueue(6)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'ArrayLoopQueue: front [4,5,6] tail'
        assert len(queue) == 3
        assert queue.front() == 4
        with pytest.raises(FullError):
            queue.enqueue(7)
