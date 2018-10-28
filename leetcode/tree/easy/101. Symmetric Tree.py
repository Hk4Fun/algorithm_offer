__author__ = 'Hk4Fun'
__date__ = '2018/4/17 22:52'
'''题目描述：
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
'''主要思路：
类似于leetcode/tree/easy/100. Same Tree.py，只不过反过来比较
时间O（n），空间O（n）
recursively and iteratively(bfs,serialize)
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

    def isSymmetric_serialize(self, root):
        def serialize(root, flag):
            res, level = [], [root]
            while level:
                next_level = []
                for cur in level:
                    res.append(cur.val if cur else None)
                    if cur:
                        if flag == 'l':
                            next_level += cur.left, cur.right
                        elif flag == 'r':
                            next_level += cur.right, cur.left
                level = next_level
            return res

        if not root: return True
        return serialize(root.left, 'l') == serialize(root.right, 'r')

    def isSymmetric_recursive(self, root):
        def sym(left, right):
            if left and right and left.val == right.val:
                return sym(left.left, right.right) and sym(left.right, right.left)
            return left is right

        if not root: return True
        return sym(root.left, root.right)


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
