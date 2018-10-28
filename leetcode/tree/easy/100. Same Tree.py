__author__ = 'Hk4Fun'
__date__ = '2018/4/17 22:26'
'''题目描述：
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''
'''主要思路：
思路1（时间O（n），空间O（n））:
序列化（层序遍历），相当于迭代
思路2（时间O（n），空间O（n））：
递归
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    def isSameTree1(self, p, q):
        def serialize(root):
            res, level = [], [root]
            while level:
                next_level = []
                for cur in level:
                    res.append(cur.val if cur else None)
                    if cur: next_level += cur.left, cur.right
                level = next_level
            return res

        return serialize(p) == serialize(q)

    def isSameTree2(self, p, q):
        if p and q and p.val == q.val:
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)
        return p is q  # 当且仅当 p == q == None，相当于 return not p and not q


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
