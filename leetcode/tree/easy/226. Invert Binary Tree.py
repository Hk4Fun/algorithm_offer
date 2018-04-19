__author__ = 'Hk4Fun'
__date__ = '2018/4/19 19:48'
'''题目描述：
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
'''主要思路：
target_offer/19_二叉树的镜像.py
时间O（n），空间O（n）
dfs or bfs
'''

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    def invertTree_dfs1(self, root):  # 自上而下
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree_dfs1(root.left)
        self.invertTree_dfs1(root.right)
        return root

    def invertTree_dfs2(self, root):  # 自下而上
        if root:
            root.left, root.right = self.invertTree_dfs2(root.right), self.invertTree_dfs2(root.left)
            return root

    def invertTree_dfs3(self, root):  # 迭代
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root

    def invertTree_bfs(self, root):
        queue = deque([root]) # 双端队列模拟队列，queue.popleft()比queue.pop(0)快
        while queue:
            cur = queue.popleft()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                queue.append(cur.left)
                queue.append(cur.right)
        return root


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
