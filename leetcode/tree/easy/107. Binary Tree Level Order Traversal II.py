__author__ = 'Hk4Fun'
__date__ = '2018/4/17 23:33'
'''题目描述：
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
'''主要思路：
target_offer/60_把二叉树打印成多行.py, 只不过最后要逆序输出
时间O（n），空间O（n）
recursively(dfs) and iteratively(bfs)
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    def levelOrderBottom_bfs(self, root):
        # 不用insert(0, list), 该操作为O(n)
        if not root: return []
        res = [[root.val]]
        cur_level = [root]
        while cur_level:  # 这里用cur_level和next_level而不用一个queue是为了避免使用pop(0)，该操作为O(n)
            next_level = []
            res.append([])
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                    res[-1].append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    res[-1].append(node.right.val)
            cur_level = next_level
        return res[-2::-1]  # 最后一个为[]，应去掉

    def levelOrderBottom_bfs_pythonic(self, root):  # 上一思路的简化版，相当精妙，来自lee215
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return res[-2::-1]

    def levelOrderBottom_dfs(self, root):
        def dfs(root, level):
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)

        res = []
        dfs(root, 0)
        return res[::-1]


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
