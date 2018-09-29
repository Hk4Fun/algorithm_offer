__author__ = 'Hk4Fun'
__date__ = '2018/9/28 16:44'

import pytest
from bst import BST


class TestBST:
    def test_empty_tree(self):
        bst = BST()
        assert bst.root is None
        assert bst.is_empty() is True
        assert bst.size == 0
        assert bst.levels == 0
        assert bst.__repr__() == "BST(serialize='')"
        assert bst.serialize() == ''
        assert bst.level_order() == []
        assert bst.pre_order() == []
        assert bst.in_order() == []
        assert bst.post_order() == []
        assert bst == BST()

    def test_add(self):
        bst = BST()
        bst.add(10)
        assert bst.root.val == 10
        assert bst.is_empty() is False
        assert bst.size == 1
        assert bst.levels == 1
        assert bst.serialize() == '10'
        assert bst.level_order() == [[10]]
        assert bst.pre_order() == [10]
        assert bst.in_order() == [10]
        assert bst.post_order() == [10]
        assert bst == BST(serialize='10')

        bst.add(1)
        assert bst.root.val == 10
        assert bst.is_empty() is False
        assert bst.size == 2
        assert bst.levels == 2
        assert bst.serialize() == '10,1,#'
        assert bst.level_order() == [[10], [1]]
        assert bst.pre_order() == [10, 1]
        assert bst.in_order() == [1, 10]
        assert bst.post_order() == [1, 10]

        bst.add(20)
        assert bst.root.val == 10
        assert bst.is_empty() is False
        assert bst.size == 3
        assert bst.levels == 2
        assert bst.serialize() == '10,1,20'
        assert bst.level_order() == [[10], [1, 20]]
        assert bst.pre_order() == [10, 1, 20]
        assert bst.in_order() == [1, 10, 20]
        assert bst.post_order() == [1, 20, 10]

        bst.add(5)
        bst.add(15)
        assert bst.root.val == 10
        assert bst.is_empty() is False
        assert bst.size == 5
        assert bst.levels == 3
        assert bst.serialize() == '10,1,20,#,5,15,#'
        assert bst.level_order() == [[10], [1, 20], [5, 15]]
        assert bst.pre_order() == [10, 1, 5, 20, 15]
        assert bst.in_order() == [1, 5, 10, 15, 20]
        assert bst.post_order() == [5, 1, 15, 20, 10]

    def test_contains(self):
        bst = BST()
        assert 1 not in bst
        bst.add(10)
        assert 10 in bst
        bst.add(20)
        bst.add(15)
        bst.add(5)
        assert 20 in bst
        assert 5 in bst
        assert 15 in bst
        assert 11 not in bst

    def test_minimum_maximum(self):
        bst = BST()
        assert bst.minimum() is None
        assert bst.maximum() is None
        bst.add(10)
        assert bst.minimum() == 10
        assert bst.maximum() == 10
        bst.add(20)
        bst.add(15)
        bst.add(5)
        bst.add(7)
        assert bst.minimum() == 5
        assert bst.maximum() == 20

    def test_remove_min(self):
        bst = BST()
        assert bst.remove_min() is None
        assert bst.is_empty() is True
        bst.add(10)
        assert bst.remove_min() == 10
        assert bst.is_empty() is True
        bst.add(10)
        bst.add(20)
        bst.add(15)
        bst.add(5)
        bst.add(7)
        assert bst.remove_min() == 5
        assert bst.remove_min() == 7
        assert bst.remove_min() == 10
        assert bst.root.val == 20
        assert bst.size == 2
        assert bst.remove_min() == 15
        assert bst.remove_min() == 20
        assert bst.is_empty() is True

    def test_remove_max(self):
        bst = BST()
        assert bst.remove_max() is None
        assert bst.is_empty() is True

        bst.add(10)
        assert bst.remove_max() == 10
        assert bst.is_empty() is True

        bst.add(10)
        bst.add(20)
        bst.add(15)
        bst.add(5)
        bst.add(7)
        assert bst.remove_max() == 20
        assert bst.remove_max() == 15
        assert bst.remove_max() == 10
        assert bst.root.val == 5
        assert bst.size == 2
        assert bst.remove_max() == 7
        assert bst.remove_max() == 5
        assert bst.is_empty() is True

    def test_remove(self):
        bst = BST()
        with pytest.raises(ValueError):
            bst.remove(0)

        bst.add(10)
        with pytest.raises(ValueError):
            bst.remove(0)
        bst.remove(10)
        assert bst.is_empty() is True

        bst.add(10)
        bst.add(20)
        bst.add(15)
        bst.add(5)
        bst.add(7)
        bst.remove(10)
        assert bst.serialize() == '15,5,20,#,7,#,#'
        assert bst.size == 4
        assert bst.root.val == 15

        bst.remove(5)
        assert bst.serialize() == '15,7,20'
        assert bst.size == 3
        assert bst.root.val == 15

        bst.add(18)
        bst.remove(20)
        assert bst.serialize() == '15,7,18'
        assert bst.size == 3
        assert bst.root.val == 15

        bst.remove(7)
        assert bst.serialize() == '15,#,18'
        assert bst.size == 2
        assert bst.root.val == 15

        bst.remove(15)
        assert bst.serialize() == '18'
        assert bst.size == 1
        assert bst.root.val == 18

    def test_add_values(self):
        bst = BST()
        bst.add_values([1, 2, 3])
        assert bst.root.val == 1
        assert bst.is_empty() is False
        assert bst.size == 3
        assert bst.levels == 3
        assert bst.serialize() == '1,#,2,#,#,#,3'

        bst.add_values([1, 2, 3])
        assert bst.root.val == 1
        assert bst.is_empty() is False
        assert bst.size == 3
        assert bst.levels == 3
        assert bst.serialize() == '1,#,2,#,#,#,3'

        bst.add_values([-3, -2, -1])
        assert bst.root.val == 1
        assert bst.is_empty() is False
        assert bst.size == 6
        assert bst.levels == 4
        assert bst.serialize() == '1,-3,2,#,-2,#,3,#,#,#,-1,#,#,#,#'
