__author__ = 'Hk4Fun'
__date__ = '2018/9/28 3:10'

import pytest
from linked_list_deque import LinkedListDeque
from exceptions import EmptyError, FullError

class TestLinkedListDeque:
    def test_inf_empty_deque(self):
        deque = LinkedListDeque()
        assert deque.is_empty() == True
        assert deque.is_full() == False
        assert deque.capacity == float('inf')
        assert deque.__repr__() == 'LinkedListDeque: front [] tail'
        assert len(deque) == 0
        with pytest.raises(EmptyError):
            deque.front()
        with pytest.raises(EmptyError):
            deque.tail()
        with pytest.raises(EmptyError):
            deque.pop_front()
        with pytest.raises(EmptyError):
            deque.pop_tail()

    def test_inf_deque(self):
        deque = LinkedListDeque()
        deque.push_tail(1)
        deque.push_front(2)
        deque.push_front(3)
        deque.push_tail(4)
        assert deque.is_empty() == False
        assert deque.is_full() == False
        assert deque.capacity == float('inf')
        assert deque.__repr__() == 'LinkedListDeque: front [3,2,1,4] tail'
        assert len(deque) == 4
        assert deque.front() == 3
        assert deque.tail() == 4

        assert deque.pop_front() == 3
        assert deque.pop_tail() == 4
        assert deque.is_empty() == False
        assert deque.is_full() == False
        assert deque.capacity == float('inf')
        assert deque.__repr__() == 'LinkedListDeque: front [2,1] tail'
        assert len(deque) == 2
        assert deque.front() == 2
        assert deque.tail() == 1

        assert deque.pop_tail() == 1
        assert deque.pop_front() == 2
        assert deque.is_empty() == True
        assert deque.is_full() == False
        assert deque.capacity == float('inf')
        assert deque.__repr__() == 'LinkedListDeque: front [] tail'
        assert len(deque) == 0
        with pytest.raises(EmptyError):
            deque.front()
        with pytest.raises(EmptyError):
            deque.tail()
        with pytest.raises(EmptyError):
            deque.pop_front()
        with pytest.raises(EmptyError):
            deque.pop_tail()

    def test_fix_len_empty_deque(self):
        deque = LinkedListDeque(0)
        assert deque.is_empty() == True
        assert deque.is_full() == True
        assert deque.capacity == 0
        assert deque.__repr__() == 'LinkedListDeque: front [] tail'
        assert len(deque) == 0
        with pytest.raises(EmptyError):
            deque.front()
        with pytest.raises(EmptyError):
            deque.tail()
        with pytest.raises(EmptyError):
            deque.pop_front()
        with pytest.raises(EmptyError):
            deque.pop_tail()

        deque = LinkedListDeque(3)
        assert deque.is_empty() == True
        assert deque.is_full() == False
        assert deque.capacity == 3
        assert deque.__repr__() == 'LinkedListDeque: front [] tail'
        assert len(deque) == 0
        with pytest.raises(EmptyError):
            deque.front()
        with pytest.raises(EmptyError):
            deque.tail()
        with pytest.raises(EmptyError):
            deque.pop_front()
        with pytest.raises(EmptyError):
            deque.pop_tail()

    def test_fix_len_deque(self):
        deque = LinkedListDeque(4)
        deque.push_tail(1)
        deque.push_front(2)
        assert deque.is_empty() == False
        assert deque.is_full() == False
        assert deque.capacity == 4
        assert deque.__repr__() == 'LinkedListDeque: front [2,1] tail'
        assert len(deque) == 2
        assert deque.front() == 2
        assert deque.tail() == 1

        deque.push_tail(3)
        deque.push_front(4)
        assert deque.is_empty() == False
        assert deque.is_full() == True
        assert deque.capacity == 4
        assert deque.__repr__() == 'LinkedListDeque: front [4,2,1,3] tail'
        assert len(deque) == 4
        assert deque.front() == 4
        assert deque.tail() == 3

        with pytest.raises(FullError):
            deque.push_front(1)
        with pytest.raises(FullError):
            deque.push_tail(2)

        assert deque.pop_front() == 4
        assert deque.pop_front() == 2
        assert deque.pop_tail() == 3
        assert deque.pop_tail() == 1
        assert deque.is_empty() == True
        assert deque.is_full() == False
        assert deque.capacity == 4
        assert deque.__repr__() == 'LinkedListDeque: front [] tail'
        assert len(deque) == 0
        with pytest.raises(EmptyError):
            deque.front()
        with pytest.raises(EmptyError):
            deque.tail()
        with pytest.raises(EmptyError):
            deque.pop_front()
        with pytest.raises(EmptyError):
            deque.pop_tail()