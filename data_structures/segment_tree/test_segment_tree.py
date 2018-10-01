__author__ = 'Hk4Fun'
__date__ = '2018/10/1 18:17'

import pytest
from segment_tree import SegmentTree
from exceptions import EmptyError


class TestSegmentTree:
    def test_init(self):
        arr = []
        with pytest.raises(EmptyError):
            SegmentTree(arr, lambda x, y: x + y)

        arr = [1]
        tree = SegmentTree(arr, lambda x, y: x + y)
        assert repr(tree) == self._make_repr([1], arr)

        arr = [1, 2]
        tree = SegmentTree(arr, lambda x, y: x + y)
        assert repr(tree) == self._make_repr([3, 1, 2], arr)

        arr = [1, 2, 3]
        tree = SegmentTree(arr, lambda x, y: x + y)
        assert repr(tree) == self._make_repr([6, 3, 3, 1, 2], arr)

        arr = [1, 2, 3, 4]
        tree = SegmentTree(arr, lambda x, y: x + y)
        assert repr(tree) == self._make_repr([10, 3, 7, 1, 2, 3, 4], arr)

        arr = [1, 2, 3, 4, 5]
        tree = SegmentTree(arr, lambda x, y: x + y)
        assert repr(tree) == self._make_repr([15, 6, 9, 3, 3, 4, 5, 1, 2], arr)

    def test_query(self):
        arr = [1, 2, 3, 4]
        tree = SegmentTree(arr, lambda x, y: x + y)
        assert tree.query(0, 0) == 1
        assert tree.query(1, 1) == 2
        assert tree.query(0, 1) == 3
        assert tree.query(2, 2) == 3
        assert tree.query(3, 3) == 4
        assert tree.query(2, 3) == 7
        assert tree.query(1, 2) == 5
        assert tree.query(0, 2) == 6
        assert tree.query(1, 3) == 9
        assert tree.query(0, 3) == 10

        tree = SegmentTree(arr, lambda x, y: x * y)
        assert tree.query(0, 0) == 1
        assert tree.query(1, 1) == 2
        assert tree.query(0, 1) == 2
        assert tree.query(2, 2) == 3
        assert tree.query(3, 3) == 4
        assert tree.query(2, 3) == 12
        assert tree.query(1, 2) == 6
        assert tree.query(0, 2) == 6
        assert tree.query(1, 3) == 24
        assert tree.query(0, 3) == 24
        with pytest.raises(IndexError):
            tree.query(0, 4)
        with pytest.raises(IndexError):
            tree.query(4, 4)

    def test_setitem(self):
        arr = [1, 2, 3, 4]
        tree = SegmentTree(arr, lambda x, y: x + y)
        tree[0] = 5
        assert repr(tree) == self._make_repr([14, 7, 7, 5, 2, 3, 4], arr)

        tree[3] = -1
        assert repr(tree) == self._make_repr([9, 7, 2, 5, 2, 3, -1], arr)

        with pytest.raises(IndexError):
            tree[4] = 4

    def _make_repr(self, tree, arr):
        s1 = ','.join(str(val) for val in tree)
        s2 = ','.join(['None'] * (2 * len(arr) + 1))
        return 'SegmentTree([{},{}])'.format(s1, s2)
