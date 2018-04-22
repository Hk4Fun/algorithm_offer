__author__ = 'Hk4Fun'
__date__ = '2018/4/23 0:18'
'''题目描述：
Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
'''主要思路：
target_offer/18_树的子结构.py，但这里要求必须s和t都要到达None才匹配成功

思路1（时间O（m*n），空间O（n），s--n，t--m，n>=m）：
target_offer/18_树的子结构.py，暴力前序遍历
先递归遍历（先序遍历）树A，找到相同的根结点子树，
再用递归分别判断该子树的左右子树是否与B一样，递归结束的条件是来到B的叶结点

思路1（时间O（n），空间O（n），s--n，t--m，n>=m）：
target_offer/62_二叉树的序列化和反序列化.py
序列化该二叉树，然后用in判断（KMP）
'''


class Solution:
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    def isSubtree1(self, s, t):
        def sub(s, t):
            if not s or not t: return s == t
            return s.val == t.val and sub(s.left, t.left) and sub(s.right, t.right)

        return True if (s and (sub(s, t) or self.isSubtree1(s.left, t) or self.isSubtree1(s.right, t))) else False

    def isSubtree2(self, s, t):
        def serialize(root):
            return ',' + str(root.val) + ',' + serialize(root.left) + serialize(root.right) if root else '#'

        return serialize(t) in serialize(s)


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
