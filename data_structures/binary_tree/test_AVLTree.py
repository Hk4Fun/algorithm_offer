__author__ = 'Hk4Fun'
__date__ = '2018/10/5 17:46'

import random
import pytest
from AVLTree import AVLTree
from exceptions import InitError


class TestAVLTree:
    def test_init_error(self):
        with pytest.raises(InitError) as e:
            AVLTree(serialize='1,2,3')
        assert str(e.value) == "must start with a bst"
        with pytest.raises(InitError) as e:
            AVLTree(serialize='2,1,#,-1,#,#,#')
        assert str(e.value) == "must start with a AVLTree"

    def test_LL_add(self):
        tree = AVLTree()
        assert tree.is_balanced() is True
        tree.add_values([5, 4, 3])
        assert tree.serialize() == '4,3,5'
        assert tree.is_balanced() is True

    def test_RR_add(self):
        tree = AVLTree()
        tree.add_values([5, 6, 7])
        assert tree.serialize() == '6,5,7'
        assert tree.is_balanced() is True

    def test_LR_add(self):
        tree = AVLTree()
        tree.add_values([5, 3, 4])
        assert tree.serialize() == '4,3,5'
        assert tree.is_balanced() is True

    def test_RL_add(self):
        tree = AVLTree()
        tree.add_values([5, 7, 6])
        assert tree.serialize() == '6,5,7'
        assert tree.is_balanced() is True

    def test_LL_remove(self):
        tree = AVLTree()
        tree.add_values([5, 4, 3, 2])
        tree.remove(5)
        assert tree.serialize() == '3,2,4'
        assert tree.is_balanced() is True

    def test_RR_remove(self):
        tree = AVLTree()
        tree.add_values([5, 6, 7, 8])
        tree.remove(5)
        assert tree.serialize() == '7,6,8'
        assert tree.is_balanced() is True

    def test_LR_remove(self):
        tree = AVLTree()
        tree.add_values([5, 3, 6, 4])
        tree.remove(6)
        assert tree.serialize() == '4,3,5'
        assert tree.is_balanced() is True

    def test_RL_remove(self):
        tree = AVLTree()
        tree.add_values([5, 4, 7, 6])
        tree.remove(4)
        assert tree.serialize() == '6,5,7'
        assert tree.is_balanced() is True

    def test_remove(self):
        tree = AVLTree()
        tree.add_values([5, 3, 8, 6, 7, 9])
        tree.remove(5)
        assert tree.serialize() == '7,6,8,3,#,#,9'
        assert tree.is_balanced() is True

    def test_random_add_remove(self):
        TEST_NUM = 10000
        RANDOM_RANGE = 1000
        nums = {random.randint(0, RANDOM_RANGE) for _ in range(TEST_NUM)}
        nums_copy = nums.copy()

        tree = AVLTree()
        for i in range(len(nums)):
            tree.add(nums.pop())
            assert tree.is_balanced()
        for i in range(len(nums)):
            tree.remove(nums_copy.pop())
            assert tree.is_balanced()
