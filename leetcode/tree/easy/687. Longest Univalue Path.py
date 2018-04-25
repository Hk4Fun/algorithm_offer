__author__ = 'Hk4Fun'
__date__ = '2018/4/25 1:24'
'''题目描述：
Given a binary tree, find the length of the longest path 
where each node in the path has the same value. 
This path may or may not pass through the root.
Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. 
The height of the tree is not more than 1000.
'''
'''主要思路：
时间O（n），空间O（h）
n---树的结点个数，h--树的高度
思路与leetcode/tree/easy/543. Diameter of Binary Tree.py类似
树形dp，后序遍历
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    :type root: TreeNode
    :rtype: int
    """
    def longestUnivaluePath(self, root):
        def dfs(root):
            if not root: return 0
            l_longest, r_longest = dfs(root.left), dfs(root.right)
            l_len = l_longest + 1 if root.left and root.left.val == root.val else 0
            r_len = r_longest + 1 if root.right and root.right.val == root.val else 0
            self.longest = max(self.longest, l_len + r_len)
            return max(l_len, r_len) # 只返回一边最大值

        self.longest = 0
        dfs(root)
        return self.longest

    def longestUnivaluePath_simple(self, root): # 上一思路的简化版
        def dfs(root, parent_val):
            if not root: return 0
            l_longest, r_longest = dfs(root.left, root.val), dfs(root.right, root.val)
            self.longest = max(self.longest, l_longest + r_longest)
            return 1 + max(l_longest, r_longest) if root.val == parent_val else 0 # 只返回一边最大值

        self.longest = 0
        dfs(root, None)
        return self.longest


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