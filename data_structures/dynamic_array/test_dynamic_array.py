__author__ = 'Hk4Fun'
__date__ = '2018/9/22 19:53'

import pytest

from dynamic_array import DynamicArray


class TestDynamicArray:
    def test_init_repr(self):
        arr = DynamicArray()
        assert arr.__repr__() == '[]'
        arr = DynamicArray([])
        assert arr.__repr__() == '[]'
        arr = DynamicArray([1, 2, 3])
        assert arr.__repr__() == '[1,2,3]'
        arr = DynamicArray({1, 2, 3})
        assert arr.__repr__() == '[1,2,3]'
        arr = DynamicArray((1, 2, 3))
        assert arr.__repr__() == '[1,2,3]'
        with pytest.raises(TypeError):
            DynamicArray(1)

    def test_length(self):
        arr = DynamicArray()
        assert len(arr) == 0
        arr = DynamicArray([])
        assert len(arr) == 0
        arr = DynamicArray([1, 2, 3])
        assert len(arr) == 3
        arr.append(1)
        assert len(arr) == 4

    def test_getitem(self):
        arr = DynamicArray()
        with pytest.raises(IndexError):
            tmp = arr[0]
        arr = DynamicArray(list(range(10)))
        for i in range(10):
            assert arr[i] == i
        with pytest.raises(IndexError):
            tmp = arr[10]

    def test_setitem(self):
        arr = DynamicArray()
        with pytest.raises(IndexError):
            arr[0] = 0
        arr = DynamicArray([1])
        arr[0] = 1
        assert arr[0] == 1
        with pytest.raises(IndexError):
            arr[1] = 2

    def test_contains(self):
        arr = DynamicArray()
        assert (0 in arr) is False
        arr = DynamicArray([1, 2])
        assert (1 in arr) is True
        assert (2 in arr) is True
        assert (3 in arr) is False

    def test_capacity(self):
        arr = DynamicArray()
        assert arr.capacity == 0
        arr.append(0)
        assert arr.capacity == 1
        arr.append(1)
        assert arr.capacity == 2
        arr.append(2)
        assert arr.capacity == 4
        arr.append(3)
        assert arr.capacity == 4
        arr.append(4)
        assert arr.capacity == 8
        arr.extend([5, 6, 7, 8])
        assert arr.capacity == 16
        arr = DynamicArray([1, 2, 3])
        assert arr.capacity == 4
        arr = DynamicArray([1, 2, 3, 4])
        assert arr.capacity == 4
        arr = DynamicArray([1, 2, 3, 4, 5])
        assert arr.capacity == 8

    def test_clear(self):
        arr = DynamicArray()
        arr.clear()
        assert len(arr) == 0
        assert arr.capacity == 0
        assert arr.__repr__() == '[]'
        arr = DynamicArray([1, 2, 3])
        arr.clear()
        assert len(arr) == 0
        assert arr.capacity == 0
        assert arr.__repr__() == '[]'

    def test_count(self):
        arr = DynamicArray([])
        assert arr.count(1) == 0
        arr.append(1)
        assert arr.count(1) == 1
        assert arr.count(0) == 0
        arr.append(1)
        assert arr.count(1) == 2

    def test_extend(self):
        arr = DynamicArray()
        arr.extend([1, 2, 3])
        assert arr.__repr__() == '[1,2,3]'
        arr = DynamicArray()
        arr.extend([])
        assert arr.__repr__() == '[]'
        arr = DynamicArray([1, 2, 3])
        with pytest.raises(TypeError):
            arr.extend(1)
        arr.extend([1, 2, 3])
        assert arr.__repr__() == '[1,2,3,1,2,3]'

    def test_index(self):
        arr = DynamicArray([])
        with pytest.raises(ValueError):
            arr.index(0, 0, len(arr))
        arr = DynamicArray([1, 2, 3, 2])
        assert arr.index(2) == 1
        assert arr.index(2, -1, 10) == 1
        assert arr.index(2, 1, 2) == 1
        assert arr.index(2, 2, 10) == 3
        assert arr.index(2, 3, 10) == 3
        with pytest.raises(ValueError):
            arr.index(2, 0, 1)
        with pytest.raises(ValueError):
            arr.index(2, 2, 1)
        with pytest.raises(ValueError):
            arr.index(4, 0, 3)
        with pytest.raises(ValueError):
            arr.index(2, 1, 1)

    def test_insert(self):
        arr = DynamicArray()
        arr.insert(0, 0)
        assert arr.__repr__() == '[0]'
        arr = DynamicArray()
        arr.insert(-10, 0)
        assert arr.__repr__() == '[0]'
        arr = DynamicArray()
        arr.insert(100, 0)
        assert arr.__repr__() == '[0]'
        arr = DynamicArray([1, 2, 3])
        arr.insert(0, 0)
        assert arr.__repr__() == '[0,1,2,3]'
        arr.insert(-10, 1)
        assert arr.__repr__() == '[1,0,1,2,3]'
        arr.insert(len(arr), 0)
        assert arr.__repr__() == '[1,0,1,2,3,0]'
        arr.insert(len(arr) + 1, 1)
        assert arr.__repr__() == '[1,0,1,2,3,0,1]'
        arr.insert(3, 5)
        assert arr.__repr__() == '[1,0,1,5,2,3,0,1]'

    def test_append(self):
        arr = DynamicArray()
        arr.append(1)
        assert arr.__repr__() == '[1]'
        arr.append('')
        assert arr.__repr__() == '[1,'']'
        arr.append([])
        assert arr.__repr__() == '[1,'',[]]'
        arr.append(())
        assert arr.__repr__() == '[1,'',[],()]'
        arr.append({})
        assert arr.__repr__() == '[1,'',[],(),{}]'
        arr.append(set())
        assert arr.__repr__() == '[1,'',[],(),{},set()]'

    def test_pop(self):
        arr = DynamicArray([1, 2, 3])
        assert arr.pop() == 3
        assert arr.pop() == 2
        assert arr.pop() == 1
        with pytest.raises(IndexError):
            arr.pop()
        arr.extend([1, 2, 3])
        with pytest.raises(IndexError):
            arr.pop(-1)
        with pytest.raises(IndexError):
            arr.pop(len(arr))
        assert arr.pop(1) == 2
        assert arr.pop(0) == 1
        assert arr.pop() == 3
        arr.extend([1, 2, 3, 4])
        arr.pop()
        assert arr.capacity == 4
        arr.pop()
        assert arr.capacity == 4
        arr.pop()
        assert arr.capacity == 2

    def test_remove(self):
        arr = DynamicArray()
        with pytest.raises(ValueError):
            arr.remove(0)
        arr.extend([1, 2, 3])
        arr.remove(1)
        assert arr.__repr__() == '[2,3]'
        arr.remove(3)
        assert arr.__repr__() == '[2]'
        with pytest.raises(ValueError):
            arr.remove(0)

    def test_reverse(self):
        arr = DynamicArray()
        arr.reverse()
        assert arr.__repr__() == '[]'
        arr.append(1)
        arr.reverse()
        assert arr.__repr__() == '[1]'
        arr = DynamicArray([1, 2, 3])
        arr.reverse()
        assert arr.__repr__() == '[3,2,1]'
