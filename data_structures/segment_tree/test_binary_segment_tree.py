__author__ = 'Hk4Fun'
__date__ = '2018/10/2 11:08'

import pytest
from binary_segment_tree import SegmentTree


class TestSegmentTree:
    def test_init(self):
        tree = SegmentTree([], lambda x, y: x + y)
        assert repr(tree) == 'SegmentTree([])'

        tree = SegmentTree([1], lambda x, y: x + y)
        assert repr(tree) == 'SegmentTree([1])'

        tree = SegmentTree([1, 2], lambda x, y: x + y)
        assert repr(tree) == 'SegmentTree([3,1,2])'

        tree = SegmentTree([1, 2, 3], lambda x, y: x + y)
        assert repr(tree) == 'SegmentTree([6,3,3,1,2])'

        tree = SegmentTree([1, 2, 3, 4], lambda x, y: x + y)
        assert repr(tree) == 'SegmentTree([10,3,7,1,2,3,4])'

        tree = SegmentTree([1, 2, 3, 4, 5], lambda x, y: x + y)
        assert repr(tree) == 'SegmentTree([15,6,9,3,3,4,5,1,2])'

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
        assert repr(tree) == 'SegmentTree([14,7,7,5,2,3,4])'

        tree[3] = -1
        assert repr(tree) == 'SegmentTree([9,7,2,5,2,3,-1])'

        with pytest.raises(IndexError):
            tree[4] = 4
