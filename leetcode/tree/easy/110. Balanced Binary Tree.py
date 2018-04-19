__author__ = 'Hk4Fun'
__date__ = '2018/4/19 14:44'
'''题目描述：
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''
'''主要思路：
target_offer/39_2_判断平衡二叉树.py 思路2
时间O（n），空间O（n）
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: bool
    """

    def isBalanced1(self, root):
        def is_bst(root):
            if not root:
                return 0
            l, r = is_bst(root.left), is_bst(root.right)
            if l < 0 or r < 0 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return is_bst(root) >= 0

    def isBalanced2(self, root):  # 更快点？
        def is_bst(root):
            if not root:
                return 0
            l = is_bst(root.left)
            if l == -1: return -1
            r = is_bst(root.right)
            if r == -1: return -1
            if abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return is_bst(root) != -1


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
