__author__ = 'Hk4Fun'
__date__ = '2018/4/21 22:10'
'''题目描述：
Given a binary search tree (BST) with duplicates, 
find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? 
(Assume that the implicit stack space incurred due to recursion does not count).
'''
'''主要思路：
思路1（时间O（n），空间O（n））
哈希表存储，前序遍历，没有充分利用BST的特点，打乱了顺序，所以只能用哈希表，但对任意树可行
思路2（时间O（n），空间O（1））
中序遍历，相当于在有序数组中找出重复次数最多的数。
遍历两遍数组，第一遍统计出最大重复数max_freq，第二遍找出重复次数为max_freq的数
'''
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def findMode1(self, root):
        def dfs(root):
            if not root: return
            self.cache[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        if not root: return []
        self.cache = defaultdict(int)
        dfs(root)
        max_freq = max(self.cache.values())
        return [i for i, v in self.cache.items() if v == max_freq]

    def findMode2(self, root):
        def in_order(root):
            if not root: return
            in_order(root.left)
            handleValue(root.val)
            in_order(root.right)

        def handleValue(val):
            if self.cur != val:
                self.cur = val
                self.curCount = 0
            self.curCount += 1
            if self.curCount > self.maxCount:
                self.maxCount = self.curCount
            elif self.curCount == self.maxCount:
                self.modes.append(val)

        self.cur = None
        self.curCount = self.maxCount = 0
        self.modes = []
        in_order(root)
        self.curCount = 0
        self.modes = []
        in_order(root)
        return self.modes


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
