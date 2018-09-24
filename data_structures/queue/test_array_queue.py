__author__ = 'Hk4Fun'
__date__ = '2018/9/24 18:10'

import pytest
from array_queue import ArrayQueue
from exceptions import EmptyError, FullError


class TestQueue:

    def test_inf_empty_queue(self):
        queue = ArrayQueue()
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == float('inf')
        assert queue.__repr__() == 'Queue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

    def test_inf_queue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == float('inf')
        assert queue.__repr__() == 'Queue: front [1,2] tail'
        assert len(queue) == 2
        assert queue.front() == 1

        assert queue.dequeue() == 1
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == float('inf')
        assert queue.__repr__() == 'Queue: front [2] tail'
        assert len(queue) == 1
        assert queue.front() == 2

        assert queue.dequeue() == 2
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == float('inf')
        assert queue.__repr__() == 'Queue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

    def test_fix_len_empty_queue(self):
        queue = ArrayQueue(0)
        assert queue.is_empty() == True
        assert queue.is_full() == True
        assert queue.capacity == 0
        assert queue.__repr__() == 'Queue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()
        with pytest.raises(FullError):
            queue.enqueue(1)

        queue = ArrayQueue(3)
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'Queue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

    def test_fix_len_queue(self):
        queue = ArrayQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'Queue: front [1,2] tail'
        assert len(queue) == 2
        assert queue.front() == 1

        queue.enqueue(3)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'Queue: front [1,2,3] tail'
        assert len(queue) == 3
        assert queue.front() == 1
        with pytest.raises(FullError):
            queue.enqueue(4)

        assert queue.dequeue() == 1
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'Queue: front [2,3] tail'
        assert len(queue) == 2
        assert queue.front() == 2
