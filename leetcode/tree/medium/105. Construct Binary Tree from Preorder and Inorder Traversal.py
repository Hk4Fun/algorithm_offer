__author__ = 'Hk4Fun'
__date__ = '2018/4/26 11:57'
'''题目描述：
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
'''主要思路：
时间O（n），空间O（n）
思路1：target_offer/6_1_重建二叉树（前序中序）.py
思路2：用一个stop变量控制中序遍历序列的返回
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    def buildTree1(self, preorder, inorder):
        def build(l1, r1, l2, r2):
            if l1 > r1 or l2 > r2: return
            node = TreeNode(preorder[l1])
            index = inorder.index(preorder[l1])
            node.left = build(l1 + 1, l1 + index - l2, l2, index - 1)
            node.right = build(l1 + index - l2 + 1, r1, index + 1, r2)
            return node

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTree2(self, preorder, inorder):

        def build(stop=None):
            if preorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build()


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

        testArgs.append([[1, 2, 3], [2, 3, 1], []])

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
