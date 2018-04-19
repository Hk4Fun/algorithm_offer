__author__ = 'Hk4Fun'
__date__ = '2018/4/19 14:53'
'''题目描述：
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
'''主要思路：
类似于leetcode/tree/easy/104. Maximum Depth of Binary Tree.py
但要注意当左子树或右子树为空时，此时最小深度为不为空的那棵子树的深度+1而不是直接0+1
时间O（n），空间O（n）
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + min(l, r) if (l and r) else (l + r + 1)

    def minDepth_pythonic(self, root):
        if not root: return 0
        d = map(self.minDepth_pythonic, (root.left, root.right))
        return 1 + (min(d) or max(d))


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