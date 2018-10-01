__author__ = 'Hk4Fun'
__date__ = '2018/10/1 11:12'

import pytest
from max_heap import MaxHeap
from exceptions import EmptyError


class TestMaxHeap:
    def test_heapify(self):
        heap = MaxHeap()
        assert repr(heap) == 'MaxHeap([])'

        heap = MaxHeap(capacity=10)
        assert repr(heap) == 'MaxHeap([])'

        heap = MaxHeap([3, 2, 1])
        assert repr(heap) == 'MaxHeap([3,2,1])'

        heap = MaxHeap([1, 2, 3])
        assert repr(heap) == 'MaxHeap([3,2,1])'

        heap = MaxHeap([4, 3, 2, 1])
        assert repr(heap) == 'MaxHeap([4,3,2,1])'

        heap = MaxHeap([1, 2, 3, 4])
        assert repr(heap) == 'MaxHeap([4,2,3,1])'

        heap = MaxHeap([1, 2, 3, 4, 5, 6, 7])
        assert repr(heap) == 'MaxHeap([7,5,6,4,2,1,3])'

    def test_size(self):
        heap = MaxHeap()
        assert heap.size == 0

        heap = MaxHeap(capacity=10)
        assert heap.size == 0

        heap = MaxHeap([3, 2, 1])
        assert heap.size == 3

        heap.push(0)
        assert heap.size == 4

        heap.pop()
        assert heap.size == 3

        heap.pushpop(0)
        assert heap.size == 3

        heap.replace(0)
        assert heap.size == 3

    def test_is_empty(self):
        heap = MaxHeap()
        assert heap.is_empty() is True

        heap = MaxHeap(capacity=10)
        assert heap.is_empty() is True

        heap.push(0)
        assert heap.is_empty() is False

        heap.pop()
        assert heap.is_empty() is True

    def test_max(self):
        heap = MaxHeap()
        with pytest.raises(EmptyError):
            tmp = heap.max

        heap = MaxHeap([1])
        assert heap.max == 1

        heap = MaxHeap([1, 2, 3])
        assert heap.max == 3

        heap = MaxHeap([1, 9, 4, 7, 2, 5, 4])
        assert heap.max == 9

    def test_push(self):
        heap = MaxHeap()
        assert repr(heap) == 'MaxHeap([])'

        heap.push(10)
        assert repr(heap) == 'MaxHeap([10])'

        heap.push(5)
        assert repr(heap) == 'MaxHeap([10,5])'

        heap.push(11)
        assert repr(heap) == 'MaxHeap([11,5,10])'

        heap.push(20)
        assert repr(heap) == 'MaxHeap([20,11,10,5])'

    def test_pop(self):
        heap = MaxHeap()
        with pytest.raises(EmptyError):
            heap.pop()

        heap.push(1)
        assert heap.pop() == 1

        heap.push(1)
        heap.push(2)
        heap.push(3)
        assert heap.pop() == 3

        heap = MaxHeap([1, 2, 3])
        assert heap.pop() == 3
        assert heap.pop() == 2
        assert heap.pop() == 1
        with pytest.raises(EmptyError):
            heap.pop()

    def test_pushpop(self):
        heap = MaxHeap()
        assert heap.pushpop(1) == 1
        assert heap.size == 0

        heap = MaxHeap([1, 2, 3])
        assert heap.pushpop(0) == 3
        assert repr(heap) == 'MaxHeap([2,0,1])'

        assert heap.pushpop(3) == 3
        assert repr(heap) == 'MaxHeap([2,0,1])'

        assert heap.pushpop(2) == 2
        assert repr(heap) == 'MaxHeap([2,0,1])'

        heap = MaxHeap([1, 2, 3, 4, 5])
        assert heap.pushpop(0) == 5
        assert repr(heap) == 'MaxHeap([4,2,3,1,0])'

        assert heap.pushpop(4) == 4
        assert repr(heap) == 'MaxHeap([4,2,3,1,0])'

        assert heap.pushpop(1) == 4
        assert repr(heap) == 'MaxHeap([3,2,1,1,0])'

    def test_replace(self):
        heap = MaxHeap()
        with pytest.raises(EmptyError):
            heap.replace(0)

        heap = MaxHeap([1, 2, 3])
        assert heap.replace(4) == 3
        assert repr(heap) == 'MaxHeap([4,2,1])'

        assert heap.replace(4) == 4
        assert repr(heap) == 'MaxHeap([4,2,1])'

        assert heap.replace(3) == 4
        assert repr(heap) == 'MaxHeap([3,2,1])'

        heap = MaxHeap([1, 2, 3, 4, 5])
        assert heap.replace(6) == 5
        assert repr(heap) == 'MaxHeap([6,4,3,1,2])'

        assert heap.replace(0) == 6
        assert repr(heap) == 'MaxHeap([4,2,3,1,0])'
