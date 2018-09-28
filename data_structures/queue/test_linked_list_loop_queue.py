__author__ = 'Hk4Fun'
__date__ = '2018/9/28 14:36'

import pytest
from linked_list_loop_queue import LinkedListLoopQueue
from exceptions import EmptyError, FullError

class TestLinkedListLoopQueue:
    def test_empty_queue(self):
        queue = LinkedListLoopQueue(0)
        assert queue.is_empty() == True
        assert queue.is_full() == True
        assert queue.capacity == 0
        assert queue.__repr__() == 'LinkedListLoopQueue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()
        with pytest.raises(FullError):
            queue.enqueue(1)

        queue = LinkedListLoopQueue(3)
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

    def test_queue(self):
        queue = LinkedListLoopQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [1,2] tail'
        assert len(queue) == 2
        assert queue.front() == 1

        queue.enqueue(3)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [1,2,3] tail'
        assert len(queue) == 3
        assert queue.front() == 1
        with pytest.raises(FullError):
            queue.enqueue(4)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [3] tail'
        assert len(queue) == 1
        assert queue.front() == 3

        assert queue.dequeue() == 3
        assert queue.is_empty() == True
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [] tail'
        assert len(queue) == 0
        with pytest.raises(EmptyError):
            queue.front()
        with pytest.raises(EmptyError):
            queue.dequeue()

        queue.enqueue(4)
        assert queue.is_empty() == False
        assert queue.is_full() == False
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [4] tail'
        assert len(queue) == 1
        assert queue.front() == 4

        queue.enqueue(5)
        queue.enqueue(6)
        assert queue.is_empty() == False
        assert queue.is_full() == True
        assert queue.capacity == 3
        assert queue.__repr__() == 'LinkedListLoopQueue: front [4,5,6] tail'
        assert len(queue) == 3
        assert queue.front() == 4
        with pytest.raises(FullError):
            queue.enqueue(7)