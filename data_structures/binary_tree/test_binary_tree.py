__author__ = 'Hk4Fun'
__date__ = '2018/9/29 0:16'

import pytest
from binary_tree import BinaryTree, TreeNode
from exceptions import EmptyError


class TestBinaryTree:
    def test_empty_tree(self):
        tree = BinaryTree()
        assert tree.root is None
        assert tree.is_empty() is True
        assert tree.size == 0
        assert tree.levels == 0
        assert tree.__repr__() == "BinaryTree(serialize='')"
        assert tree.serialize() == ''
        assert tree.level_order() == []
        assert tree.pre_order() == []
        assert tree.in_order() == []
        assert tree.post_order() == []
        assert tree == BinaryTree()

    def test_tree_case1(self):
        node1 = TreeNode(1)
        tree1 = BinaryTree(node1)
        assert tree1.root is node1
        assert tree1.is_empty() is False
        assert tree1.size == 1
        assert tree1.levels == 1
        assert tree1.serialize() == '1'
        assert tree1.level_order() == [[1]]
        assert tree1.pre_order() == [1]
        assert tree1.in_order() == [1]
        assert tree1.post_order() == [1]
        tree2 = BinaryTree(serialize=tree1.serialize())
        assert tree2.root.val is 1
        assert tree1.is_empty() is False
        assert tree1.size == 1
        assert tree1.levels == 1
        assert tree1.serialize() == '1'
        assert tree1.level_order() == [[1]]
        assert tree1.pre_order() == [1]
        assert tree1.in_order() == [1]
        assert tree1.post_order() == [1]
        assert tree1 == tree2

    def test_tree_case2(self):
        #     1
        #   2
        # 3
        node3 = TreeNode(3)
        node2 = TreeNode(2, left=node3)
        node1 = TreeNode(1, left=node2)
        tree1 = BinaryTree(node1)
        assert tree1.root is node1
        assert tree1.is_empty() is False
        assert tree1.size == 3
        assert tree1.levels == 3
        assert tree1.serialize() == '1,2,#,3,#,#,#'
        assert tree1.level_order() == [[1], [2], [3]]
        assert tree1.pre_order() == [1, 2, 3]
        assert tree1.in_order() == [3, 2, 1]
        assert tree1.post_order() == [3, 2, 1]
        tree2 = BinaryTree(serialize=tree1.serialize())
        assert tree2.root.val == 1
        assert tree2.is_empty() is False
        assert tree2.size == 3
        assert tree2.levels == 3
        assert tree2.serialize() == '1,2,#,3,#,#,#'
        assert tree2.level_order() == [[1], [2], [3]]
        assert tree2.pre_order() == [1, 2, 3]
        assert tree2.in_order() == [3, 2, 1]
        assert tree2.post_order() == [3, 2, 1]
        assert tree1 == tree2

    def test_tree_case3(self):
        # 1
        #   2
        #     3
        node3 = TreeNode(3)
        node2 = TreeNode(2, right=node3)
        node1 = TreeNode(1, right=node2)
        tree1 = BinaryTree(node1)
        assert tree1.root is node1
        assert tree1.is_empty() is False
        assert tree1.size == 3
        assert tree1.levels == 3
        assert tree1.serialize() == '1,#,2,#,#,#,3'
        assert tree1.level_order() == [[1], [2], [3]]
        assert tree1.pre_order() == [1, 2, 3]
        assert tree1.in_order() == [1, 2, 3]
        assert tree1.post_order() == [3, 2, 1]
        tree2 = BinaryTree(serialize=tree1.serialize())
        assert tree2.root.val == 1
        assert tree2.is_empty() is False
        assert tree2.size == 3
        assert tree2.levels == 3
        assert tree2.serialize() == '1,#,2,#,#,#,3'
        assert tree2.level_order() == [[1], [2], [3]]
        assert tree2.pre_order() == [1, 2, 3]
        assert tree2.in_order() == [1, 2, 3]
        assert tree2.post_order() == [3, 2, 1]
        assert tree1 == tree2

    def test_tree_case4(self):
        #      1
        #   2     3
        # 4         5
        node4 = TreeNode(4)
        node2 = TreeNode(2, left=node4)
        node5 = TreeNode(5)
        node3 = TreeNode(3, right=node5)
        node1 = TreeNode(1, node2, node3)
        tree1 = BinaryTree(node1)
        assert tree1.root is node1
        assert tree1.is_empty() is False
        assert tree1.size == 5
        assert tree1.levels == 3
        assert tree1.serialize() == '1,2,3,4,#,#,5'
        assert tree1.level_order() == [[1], [2, 3], [4, 5]]
        assert tree1.pre_order() == [1, 2, 4, 3, 5]
        assert tree1.in_order() == [4, 2, 1, 3, 5]
        assert tree1.post_order() == [4, 2, 5, 3, 1]
        tree2 = BinaryTree(serialize=tree1.serialize())
        assert tree2.root.val == 1
        assert tree2.is_empty() is False
        assert tree2.size == 5
        assert tree2.levels == 3
        assert tree2.serialize() == '1,2,3,4,#,#,5'
        assert tree2.level_order() == [[1], [2, 3], [4, 5]]
        assert tree2.pre_order() == [1, 2, 4, 3, 5]
        assert tree2.in_order() == [4, 2, 1, 3, 5]
        assert tree2.post_order() == [4, 2, 5, 3, 1]
        assert tree1 == tree2

    def test_tree_case5(self):
        #          1
        #      2       3
        #   4             5
        #     6         7
        node6 = TreeNode(6)
        node4 = TreeNode(4, right=node6)
        node7 = TreeNode(7)
        node5 = TreeNode(5, left=node7)
        node2 = TreeNode(2, left=node4)
        node3 = TreeNode(3, right=node5)
        node1 = TreeNode(1, node2, node3)
        tree1 = BinaryTree(node1)
        assert tree1.root is node1
        assert tree1.is_empty() is False
        assert tree1.size == 7
        assert tree1.levels == 4
        assert tree1.serialize() == '1,2,3,4,#,#,5,#,6,#,#,#,#,7,#'
        assert tree1.level_order() == [[1], [2, 3], [4, 5], [6, 7]]
        assert tree1.pre_order() == [1, 2, 4, 6, 3, 5, 7]
        assert tree1.in_order() == [4, 6, 2, 1, 3, 7, 5]
        assert tree1.post_order() == [6, 4, 2, 7, 5, 3, 1]
        tree2 = BinaryTree(serialize=tree1.serialize())
        assert tree2.root.val is 1
        assert tree2.is_empty() is False
        assert tree2.size == 7
        assert tree2.levels == 4
        assert tree2.serialize() == '1,2,3,4,#,#,5,#,6,#,#,#,#,7,#'
        assert tree2.level_order() == [[1], [2, 3], [4, 5], [6, 7]]
        assert tree2.pre_order() == [1, 2, 4, 6, 3, 5, 7]
        assert tree2.in_order() == [4, 6, 2, 1, 3, 7, 5]
        assert tree2.post_order() == [6, 4, 2, 7, 5, 3, 1]
        assert tree1 == tree2

    def test_is_bst(self):
        tree = BinaryTree()
        assert tree.is_bst() is True

        tree = BinaryTree(serialize='1')
        assert tree.is_bst() is True

        tree = BinaryTree(serialize='1,2,3,4,#,#,5,#,6,#,#,#,#,7,#')
        assert tree.is_bst() is False

        tree = BinaryTree(serialize='2,1,3')
        assert tree.is_bst() is True

        tree = BinaryTree(serialize='10,1,20,#,5,15,#')
        assert tree.is_bst() is True

    def test_is_full(self):
        tree = BinaryTree()
        assert tree.is_full() is True

        tree = BinaryTree(serialize='1')
        assert tree.is_full() is True

        tree = BinaryTree(serialize='2,1,3')
        assert tree.is_full() is True

        tree = BinaryTree(serialize='10,1,20,#,5,15,#')
        assert tree.is_full() is False

        tree = BinaryTree(serialize='1,2,3,4,5,6,7')
        assert tree.is_full() is True

        tree = BinaryTree(serialize='1,#,3,4,#,6,7')
        assert tree.is_full() is False

    def test_is_complete(self):
        tree = BinaryTree()
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='1')
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='1,#,2')
        assert tree.is_complete() is False

        tree = BinaryTree(serialize='1,2,#')
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='2,1,3')
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='1,2,3,4,#,#,5')
        assert tree.is_complete() is False

        tree = BinaryTree(serialize='1,2,3,4,5,#,#')
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='1,2,3,4,5,6,#')
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='1,2,3,4,#,#,#')
        assert tree.is_complete() is True

        tree = BinaryTree(serialize='1,2,3,4,#,5,#')
        assert tree.is_complete() is False

        tree = BinaryTree(serialize='1,#,2,#,#,3,4')
        assert tree.is_complete() is False

    def test_leaf_count(self):
        tree = BinaryTree()
        assert tree.leaf_nums == 0

        tree = BinaryTree(serialize='1')
        assert tree.leaf_nums == 1

        tree = BinaryTree(serialize='1,2,#')
        assert tree.leaf_nums == 1

        tree = BinaryTree(serialize='1,2,3')
        assert tree.leaf_nums == 2

        tree = BinaryTree(serialize='1,2,3,4,#,#,#')
        assert tree.leaf_nums == 2

        tree = BinaryTree(serialize='1,2,3,#,4,#,#')
        assert tree.leaf_nums == 2

        tree = BinaryTree(serialize='1,2,3,#,#,4,#')
        assert tree.leaf_nums == 2

        tree = BinaryTree(serialize='1,2,3,#,#,#,4')
        assert tree.leaf_nums == 2

        tree = BinaryTree(serialize='1,2,3,4,#,#,5')
        assert tree.leaf_nums == 2

        tree = BinaryTree(serialize='1,2,3,4,5,6,7')
        assert tree.leaf_nums == 4

        tree = BinaryTree(serialize='1,2,3,4,5,6,#')
        assert tree.leaf_nums == 3

    def test_is_balanced(self):
        tree = BinaryTree()
        assert tree.is_balanced() is True

        tree = BinaryTree(serialize='1')
        assert tree.is_balanced() is True

        tree = BinaryTree(serialize='1,2,#')
        assert tree.is_balanced() is True

        tree = BinaryTree(serialize='1,2,#,3,#,#,#')
        assert tree.is_balanced() is False

        tree = BinaryTree(serialize='1,2,#,3,#,#,#')
        assert tree.is_balanced() is False

        tree = BinaryTree(serialize='1,2,3,4,#,#,5')
        assert tree.is_balanced() is True

        tree = BinaryTree(serialize='1,2,3,#,#,#,5')
        assert tree.is_balanced() is True

    def test_max_distance(self):
        tree = BinaryTree()
        with pytest.raises(EmptyError):
            tree.max_distance()

        tree = BinaryTree(serialize='1')
        assert tree.max_distance() == 0

        tree = BinaryTree(serialize='1,2,#')
        assert tree.max_distance() == 1

        tree = BinaryTree(serialize='1,#,2')
        assert tree.max_distance() == 1

        tree = BinaryTree(serialize='1,2,#,3,#,#,#')
        assert tree.max_distance() == 2

        tree = BinaryTree(serialize='1,#,2,#,#,#,3')
        assert tree.max_distance() == 2

        tree = BinaryTree(serialize='1,2,3,4,#,#,5')
        assert tree.max_distance() == 4

        tree = BinaryTree(serialize='1,2,3,4,#,#,5')
        assert tree.max_distance() == 4

        tree = BinaryTree(serialize='1,2,3,4,#,#,#')
        assert tree.max_distance() == 3
