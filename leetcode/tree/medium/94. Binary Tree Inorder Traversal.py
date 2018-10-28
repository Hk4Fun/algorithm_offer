__author__ = 'Hk4Fun'
__date__ = '2018/4/25 12:06'
'''题目描述：
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
'''主要思路：
时间O（n），空间O（n）
详见else/traverse_concise.py
这里采用其中的pre_in_order_iteration2和morris
'''


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
    def inorderTraversal(self, root):
        res, stack = [], []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res

    def inorderTraversal_morris(self, root):
        res, cur = [], root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                last_right = cur.left
                while last_right.right and last_right.right is not cur:
                    last_right = last_right.right
                if last_right.right:
                    res.append(cur.val)
                    last_right.right = None
                    cur = cur.right
                else:
                    last_right.right = cur
                    cur = cur.left
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