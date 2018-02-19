__author__ = 'Hk4Fun'
__date__ = '2018/2/13 22:20'

'''题目描述：
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
'''主要思路：
思路1：递归实现，树的深度=max(左子树深度，右子树深度)+1
思路2：循环实现，按层遍历，用一个队列来放每一层的结点，每遍历完一层深度+1
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth1(self, pRoot):
        if not pRoot: return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

    def TreeDepth2(self, pRoot):
        if not pRoot: return 0
        depth = 0
        queue = [pRoot] # 先放第一层
        while queue:
            tmp = []  # 暂时缓存下一层的结点
            for node in queue: # 遍历每一层的结点，将它们的子节点放进下一层
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue=tmp[:] # 更新当前层为下一层，准备遍历下一层
            depth += 1 # 每遍历完一层深度+1
        return depth


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

        #        1
        #     /      \
        #    2        3
        #   /\         \
        #  4  5         6
        #    /
        #   7
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        treeNode6 = TreeNode(6)
        treeNode7 = TreeNode(7)
        ConnectTreeNodes(treeNode1, treeNode2, treeNode3)
        ConnectTreeNodes(treeNode2, treeNode4, treeNode5)
        ConnectTreeNodes(treeNode3, None, treeNode6)
        ConnectTreeNodes(treeNode5, treeNode7, None)
        testArgs.append([treeNode1, 4])

        #         1
        #        /
        #       2
        #      /
        #     3
        #    /
        #   4
        #  /
        # 5
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        ConnectTreeNodes(treeNode1, treeNode2, None)
        ConnectTreeNodes(treeNode2, treeNode3, None)
        ConnectTreeNodes(treeNode3, treeNode4, None)
        ConnectTreeNodes(treeNode4, treeNode5, None)
        testArgs.append([treeNode1, 5])

        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        #        \
        #         5
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        ConnectTreeNodes(treeNode1, None, treeNode2)
        ConnectTreeNodes(treeNode2, None, treeNode3)
        ConnectTreeNodes(treeNode3, None, treeNode4)
        ConnectTreeNodes(treeNode4, None, treeNode5)
        testArgs.append([treeNode1, 5])

        # 树中只有1个结点
        treeNode1 = TreeNode(1)
        testArgs.append([treeNode1, 1])

        # 树中没有结点
        testArgs.append([None, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
