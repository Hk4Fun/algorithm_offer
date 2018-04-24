__author__ = 'Hk4Fun'
__date__ = '2018/4/25 0:26'
'''题目描述：
Given a non-empty binary tree, 
return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  
on level 1 is 14.5, and on level 2 is 11. 
Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
'''主要思路：
时间O（n），空间O（m）
n--树的结点个数，m--树的宽度
bfs
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res, queue = [], deque([root])
        while queue:
            length = len(queue)
            res.append(0)
            for _ in range(length):
                cur = queue.popleft()
                res[-1] += cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res[-1] /= length
        return res


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