__author__ = 'Hk4Fun'
__date__ = '2018/9/22 19:53'

import pytest

from dynamic_array import DynamicArray


class TestDynamicArray:
    def test_init_repr(self):
        arr = DynamicArray()
        assert arr.__repr__() == 'DynamicArray([])'
        arr = DynamicArray([])
        assert arr.__repr__() == 'DynamicArray([])'
        arr = DynamicArray([1, 2, 3])
        assert arr.__repr__() == 'DynamicArray([1,2,3])'
        arr = DynamicArray({1, 2, 3})
        assert arr.__repr__() == 'DynamicArray([1,2,3])'
        arr = DynamicArray((1, 2, 3))
        assert arr.__repr__() == 'DynamicArray([1,2,3])'
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
        for i in range(1, 11):
            assert arr[-i] == arr[10 - i]
        with pytest.raises(IndexError):
            tmp = arr[10]
        with pytest.raises(IndexError):
            tmp = arr[-11]

        arr = DynamicArray([1, 2, 3])
        assert arr[:] == DynamicArray([1, 2, 3])
        assert arr[1:] == DynamicArray([2, 3])
        assert arr[10:] == DynamicArray([])
        assert arr[-1:] == DynamicArray([3])
        assert arr[:2] == DynamicArray([1, 2])
        assert arr[:-1] == DynamicArray([1, 2])
        assert arr[1:3] == DynamicArray([2, 3])
        assert arr[::-1] == DynamicArray([3, 2, 1])
        assert arr[::1] == DynamicArray([1, 2, 3])
        assert arr[::2] == DynamicArray([1, 3])
        assert arr[1:3:2] == DynamicArray([2])
        with pytest.raises(TypeError):
            tmp = arr[1.4]

    def test_setitem(self):
        arr = DynamicArray()
        with pytest.raises(IndexError):
            arr[0] = 0
        arr = DynamicArray([1])
        arr[0] = 1
        assert arr[0] == 1
        with pytest.raises(IndexError):
            arr[1] = 2

    def test_delitem(self):
        arr = DynamicArray()
        with pytest.raises(IndexError):
            del arr[0]
        arr.append(1)
        del arr[0]
        assert arr == DynamicArray()
        arr.extend([1, 2, 3])
        del arr[1]
        assert arr == DynamicArray([1, 3])

    def test_contains(self):
        arr = DynamicArray()
        assert (0 in arr) is False
        arr = DynamicArray([1, 2])
        assert (1 in arr) is True
        assert (2 in arr) is True
        assert (3 in arr) is False

    def test_equal(self):
        arr1 = DynamicArray()
        arr2 = DynamicArray()
        assert arr1 == arr2
        arr2.append(1)
        assert arr1 != arr2
        assert arr1 != []
        assert arr2 != [1]
        arr1.append(2)
        assert arr1 != arr2
        arr1 = DynamicArray([1, 2, 3])
        arr2 = DynamicArray([3, 2, 1])
        assert arr1 != arr2

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
        assert arr.__repr__() == 'DynamicArray([])'
        arr = DynamicArray([1, 2, 3])
        arr.clear()
        assert len(arr) == 0
        assert arr.capacity == 0
        assert arr.__repr__() == 'DynamicArray([])'

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
        assert arr.__repr__() == 'DynamicArray([1,2,3])'
        arr = DynamicArray()
        arr.extend(DynamicArray())
        assert arr.__repr__() == 'DynamicArray([])'
        arr = DynamicArray([1, 2, 3])
        with pytest.raises(TypeError):
            arr.extend(1)
        arr.extend([1, 2, 3])
        assert arr.__repr__() == 'DynamicArray([1,2,3,1,2,3])'
        arr = DynamicArray([1, 2, 3])
        arr.extend(DynamicArray([4, 5, 6]))
        assert arr == DynamicArray([1, 2, 3, 4, 5, 6])

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
        assert arr.__repr__() == 'DynamicArray([0])'
        arr = DynamicArray()
        arr.insert(-10, 0)
        assert arr.__repr__() == 'DynamicArray([0])'
        arr = DynamicArray()
        arr.insert(100, 0)
        assert arr.__repr__() == 'DynamicArray([0])'
        arr = DynamicArray([1, 2, 3])
        arr.insert(0, 0)
        assert arr.__repr__() == 'DynamicArray([0,1,2,3])'
        arr.insert(-10, 1)
        assert arr.__repr__() == 'DynamicArray([1,0,1,2,3])'
        arr.insert(len(arr), 0)
        assert arr.__repr__() == 'DynamicArray([1,0,1,2,3,0])'
        arr.insert(len(arr) + 1, 1)
        assert arr.__repr__() == 'DynamicArray([1,0,1,2,3,0,1])'
        arr.insert(3, 5)
        assert arr.__repr__() == 'DynamicArray([1,0,1,5,2,3,0,1])'

    def test_append(self):
        arr = DynamicArray()
        arr.append(1)
        assert arr.__repr__() == 'DynamicArray([1])'
        arr.append('')
        assert arr.__repr__() == 'DynamicArray([1,''])'
        arr.append([])
        assert arr.__repr__() == 'DynamicArray([1,'',[]])'
        arr.append(())
        assert arr.__repr__() == 'DynamicArray([1,'',[],()])'
        arr.append({})
        assert arr.__repr__() == 'DynamicArray([1,'',[],(),{}])'
        arr.append(set())
        assert arr.__repr__() == 'DynamicArray([1,'',[],(),{},set()])'

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
        assert arr.__repr__() == 'DynamicArray([2,3])'
        arr.remove(3)
        assert arr.__repr__() == 'DynamicArray([2])'
        with pytest.raises(ValueError):
            arr.remove(0)

    def test_reverse(self):
        arr = DynamicArray()
        arr.reverse()
        assert arr.__repr__() == 'DynamicArray([])'
        arr.append(1)
        arr.reverse()
        assert arr.__repr__() == 'DynamicArray([1])'
        arr = DynamicArray([1, 2, 3])
        arr.reverse()
        assert arr.__repr__() == 'DynamicArray([3,2,1])'

    def test_mutable(self):
        arr1 = DynamicArray([1, 2, 3])
        arr2 = arr1
        arr2[0] = 4
        assert arr1[0] == 4
        arr1[2] = 5
        assert arr2[2] == 5
        arr1.append(6)
        assert arr2[-1] == 6

    def test_copy(self):
        arr1 = DynamicArray()
        arr2 = arr1.copy()
        assert arr2 == arr1
        arr1 = DynamicArray([1, 2, 3])
        arr2 = arr1.copy()
        assert arr1 == arr2
        arr1.append(4)
        assert arr2 != arr1
        arr2[0] = 4
        assert arr2[0] != arr1[0]

    def test_add(self):
        arr1 = DynamicArray()
        arr2 = DynamicArray()
        assert arr1 + arr2 == DynamicArray()
        assert arr1 == DynamicArray()
        assert arr2 == DynamicArray()
        arr1 = DynamicArray([1, 2, 3])
        arr2 = DynamicArray([4, 5, 6])
        assert arr1 + arr2 == DynamicArray([1, 2, 3, 4, 5, 6])
        assert arr2 + arr1 == DynamicArray([4, 5, 6, 1, 2, 3])
        assert arr1 == DynamicArray([1, 2, 3])
        assert arr2 == DynamicArray([4, 5, 6])
        assert arr1 + DynamicArray() == arr1
        with pytest.raises(TypeError):
            arr1 + [1, 2, 3]

    def test_iadd(self):
        arr = DynamicArray()
        id1 = id(arr)
        arr += DynamicArray()
        id2 = id(arr)
        assert id1 == id2
        assert arr == DynamicArray()

        arr = DynamicArray([1, 2, 3])
        id1 = id(arr)
        arr += DynamicArray()
        id2 = id(arr)
        assert id1 == id2
        assert arr == DynamicArray([1, 2, 3])

        arr += DynamicArray([4, 5, 6])
        id3 = id(arr)
        assert id3 == id2
        assert arr == DynamicArray([1, 2, 3, 4, 5, 6])

        arr += 7,
        id4 = id(arr)
        assert id3 == id4
        assert arr == DynamicArray([1, 2, 3, 4, 5, 6, 7])
        with pytest.raises(TypeError):
            arr += 8

    def test_mul(self):
        arr = DynamicArray()
        assert arr * 1 == arr
        assert arr * 10 == arr
        assert arr == DynamicArray()

        arr = DynamicArray([1, 2, 3])
        assert arr * 1 == arr
        assert arr * 2 == DynamicArray([1, 2, 3, 1, 2, 3])
        assert arr == DynamicArray([1, 2, 3])
        assert arr * 0 == DynamicArray()
        assert arr == DynamicArray([1, 2, 3])
        assert arr * -10 == DynamicArray()
        assert arr == DynamicArray([1, 2, 3])

        with pytest.raises(TypeError):
            arr * 1.1

    def test_imul(self):
        arr = DynamicArray()
        id1 = id(arr)
        arr *= 1
        id2 = id(arr)
        assert id1 == id2
        assert arr == DynamicArray()
        arr *= 0
        id2 = id(arr)
        assert id1 == id2
        assert arr == DynamicArray()

        arr = DynamicArray([1, 2, 3])
        id1 = id(arr)
        arr *= 3
        id2 = id(arr)
        assert id1 == id2
        assert arr == DynamicArray([1, 2, 3, 1, 2, 3, 1, 2, 3])
        arr *= -10
        id2 = id(arr)
        assert id1 == id2
        assert arr == DynamicArray()

        with pytest.raises(TypeError):
            arr *= 1.1

    def test_hash(self):
        arr = DynamicArray()
        with pytest.raises(TypeError):
            hash(arr)

    def test_iterator(self):
        arr = DynamicArray([])
        it = iter(arr)
        with pytest.raises(StopIteration):
            next(it)

        arr = DynamicArray([1, 2, 3])
        it = iter(arr)
        assert next(it) == 1
        assert next(it) == 2
        assert next(it) == 3
        with pytest.raises(StopIteration):
            next(it)
        with pytest.raises(StopIteration):
            next(it)
        it = iter(arr)
        assert next(it) == 1

        assert list(arr) == [1, 2, 3]
        assert list(arr) == [1, 2, 3]
