__author__ = 'Hk4Fun'
__date__ = '2018/2/19 18:43'

'''题目描述：
找出二叉搜索树中两个结点的最低公共祖先
'''
'''主要思路：
二分法：从根节点开始，如果当前结点的值比两个结点都大，那么最低公共祖先在当前结点的左子树中；
如果当前结点的值比两个结点都小，那么最低公共祖先在当前结点的右子树中；
这样从上到下找到的第一个在两个输入结点的值之间的结点就是最低公共祖先
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findParent(self, root, pNode1, pNode2):
        if not root or not pNode1 or not pNode2:
            return
        val1, val2 = pNode1.val, pNode2.val
        while root:
            if (val1 - root.val) * (val2 - root.val) <= 0:
                return root
            elif val1 > root.val and val2 > root.val:
                root = root.right
            else:
                root = root.left


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def ConnectTreeNodes(rootNode, leftNode, rightNode):
            rootNode.left = leftNode
            rootNode.right = rightNode

        testArgs = []

        #        4
        #    /      \
        #   2        6
        #  /\       / \
        # 1  3     5   7
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        treeNode6 = TreeNode(6)
        treeNode7 = TreeNode(7)
        ConnectTreeNodes(treeNode4, treeNode2, treeNode6)
        ConnectTreeNodes(treeNode2, treeNode1, treeNode3)
        ConnectTreeNodes(treeNode6, treeNode5, treeNode7)

        testArgs.append([treeNode4, treeNode1, treeNode3, treeNode2])
        testArgs.append([treeNode4, treeNode1, treeNode7, treeNode4])
        testArgs.append([treeNode4, treeNode1, treeNode6, treeNode4])
        testArgs.append([treeNode4, treeNode1, treeNode2, treeNode2])
        testArgs.append([treeNode4, treeNode1, treeNode4, treeNode4])
        testArgs.append([treeNode4, treeNode1, treeNode1, treeNode1])
        testArgs.append([treeNode1, treeNode1, treeNode1, treeNode1])
        testArgs.append([treeNode4, treeNode4, treeNode4, treeNode4])
        testArgs.append([None, None, None, None])



        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
