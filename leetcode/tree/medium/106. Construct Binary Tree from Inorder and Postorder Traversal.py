__author__ = 'Hk4Fun'
__date__ = '2018/4/27 19:47'
'''题目描述：
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
'''主要思路：
时间O（n），空间O（n）
思路1：target_offer/6_2_重建二叉树（中序后序）.py
思路2：用一个stop变量控制中序遍历序列的返回，不过这次两个序列都不用先逆序了
      且先连接右子树再连接左子树，因为后序序列从后往前遍历
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """

    def buildTree1(self, inorder, postorder):
        def build(l1, r1, l2, r2):
            if l1 > r1 or l2 > r2: return
            node = TreeNode(postorder[r1])
            index = inorder.index(postorder[r1])
            node.left = build(l1, l1 + index - l2 - 1, l2, index - 1)
            node.right = build(l1 + index - l2, r1 - 1, index + 1, r2)
            return node

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)

    def buildTree2(self, inorder, postorder):
        def build(stop=None):
            if postorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val) # 先连接右子树
                inorder.pop()
                root.left = build(stop) # 再连接左子树
                return root

        # 两个序列都不用先逆序
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
