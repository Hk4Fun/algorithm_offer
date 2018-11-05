__author__ = 'Hk4Fun'
__date__ = '2018/4/25 13:50'
'''题目描述：
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''
'''主要思路：
时间O（n），空间O（n）
中序遍历，判断是否为严格递增序列
也可以一边遍历一边判断，这可以只遍历一次，但需要保存前一个数
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

    def isValidBST1(self, root):
        def in_order(root):
            if root is None: return
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)

        res = []
        in_order(root)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

    def isValidBST2(self, root):
        def in_order(root):
            if root is None: return True
            if not in_order(root.left) or self.pre >= root.val: return False
            self.pre = root.val
            return in_order(root.right)

        self.pre = -float('inf')
        return in_order(root)


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
