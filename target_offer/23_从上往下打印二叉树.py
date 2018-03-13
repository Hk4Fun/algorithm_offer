__author__ = 'Hk4Fun'
__date__ = '2018/2/1 1:16'

'''题目描述：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
'''主要思路：
相当于宽度优先搜索（BFS），用队列来实现：
每次从头部取出一个结点时，如果该结点有子结点，
就把该结点的子结点从左到右依次放入队列末尾，
重复前面的步骤，直到队列为空
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result


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

        #       10
        #    /      \
        #   6        14
        #  /\        /\
        # 4  8     12  16
        treeNode10 = TreeNode(10)
        treeNode6 = TreeNode(6)
        treeNode14 = TreeNode(14)
        treeNode4 = TreeNode(4)
        treeNode8 = TreeNode(8)
        treeNode12 = TreeNode(12)
        treeNode16 = TreeNode(16)
        ConnectTreeNodes(treeNode10, treeNode6, treeNode14)
        ConnectTreeNodes(treeNode6, treeNode4, treeNode8)
        ConnectTreeNodes(treeNode14, treeNode12, treeNode16)
        testArgs.append([treeNode10, [10, 6, 14, 4, 8, 12, 16]])

        #         5
        #        /
        #       4
        #      /
        #     3
        treeNode5 = TreeNode(5)
        treeNode4 = TreeNode(4)
        treeNode3 = TreeNode(3)
        ConnectTreeNodes(treeNode5, treeNode4, None)
        ConnectTreeNodes(treeNode4, treeNode3, None)
        testArgs.append([treeNode5, [5, 4, 3]])

        # 1
        #  \
        #   2
        #    \
        #     3
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        ConnectTreeNodes(treeNode1, None, treeNode2)
        ConnectTreeNodes(treeNode2, None, treeNode3)
        testArgs.append([treeNode1, [1, 2, 3]])

        # 树中只有1个结点
        treeNode1 = TreeNode(1)
        testArgs.append([treeNode1, [1]])

        # 树中没有结点
        testArgs.append([None, []])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
