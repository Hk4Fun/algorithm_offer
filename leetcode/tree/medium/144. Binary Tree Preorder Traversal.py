__author__ = 'Hk4Fun'
__date__ = '2018/4/28 23:19'
'''题目描述：

'''
'''主要思路：
思路1：时间O（n），空间O（n）
else/1_二叉树的遍历.py pre_in_order_iteration2

思路2：时间O（n），空间O（1）
else/1_二叉树的遍历.py morris
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

    def preorderTraversal(self, root):
        if not root: return []
        stack, res = [], []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop().right
        return res

    def morris(self, root):
        if not root: return []
        res, cur = [], root
        while cur:
            if cur.left:
                last_right = cur.left
                while last_right.right and last_right.right is not cur:
                    last_right = last_right.right
                if last_right.right is cur:
                    last_right.right = None
                    cur = cur.right
                else:
                    res.append(cur.val)
                    last_right.right = cur
                    cur = cur.left
            else:
                res.append(cur.val)
                cur = cur.right
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
