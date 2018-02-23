__author__ = 'Hk4Fun'
__date__ = '2018/2/23 17:09'

'''题目描述：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''主要思路：
思路1：该结点若有右子树就找到右子树的最左结点；
       没有右子树则向上找到第一个当前结点是其父结点左孩子的结点的父结点；
       退到了根节点仍没找到则返回None
思路2：既然是中序遍历，那就先中序遍历整棵树，把结点都存放在数组里，
       然后在数组里找到所给结点的下一个结点，当然如果所给结点在最后则返回None
       (题目没给根结点，所以需要先找到根结点才能开始中序遍历，
       而根结点可以根据父指针一直向上找到)
       该算法不是最优，但思路简单
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def GetNext1(self, pNode):
        if not pNode:
            return
        if pNode.right:  # 若有右子树就找到右子树的最左结点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.parent:  # 没有右子树则向上找到第一个当前结点是其父结点左孩子的结点的父结点
            if pNode.parent.left == pNode:
                return pNode.parent
            pNode = pNode.parent
        # 退到了根节点仍没找到则返回None

    def GetNext2(self, pNode):
        def midTraversal(root, treeNodes):
            if not root: return
            midTraversal(root.left, treeNodes)
            treeNodes.append(root)
            midTraversal(root.right, treeNodes)

        if not pNode:
            return
        cur = pNode
        while cur.parent:  # 先找到根结点
            cur = cur.parent
        treeNodes = []
        midTraversal(cur, treeNodes)
        index = treeNodes.index(pNode)
        return treeNodes[index + 1] if index != len(treeNodes) - 1 else None


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def ConnectTreeNodes(parent, left, right):
            if parent:
                parent.left = left
                parent.right = right
                if left:
                    left.parent = parent
                if right:
                    right.parent = parent

        testArgs = []

        #      8
        #  6      10
        # 5 7    9  11
        node8 = TreeNode(8)
        node6 = TreeNode(6)
        node10 = TreeNode(10)
        node5 = TreeNode(5)
        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node11 = TreeNode(11)
        ConnectTreeNodes(node8, node6, node10)
        ConnectTreeNodes(node6, node5, node7)
        ConnectTreeNodes(node10, node9, node11)
        testArgs.append([node8, node9])
        testArgs.append([node6, node7])
        testArgs.append([node10, node11])
        testArgs.append([node5, node6])
        testArgs.append([node7, node8])
        testArgs.append([node9, node10])
        testArgs.append([node11, None])

        #       5
        #     4
        #   3
        # 2
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        ConnectTreeNodes(node5, node4, None)
        ConnectTreeNodes(node4, node3, None)
        ConnectTreeNodes(node3, node2, None)
        testArgs.append([node5, None])
        testArgs.append([node4, node5])
        testArgs.append([node3, node4])
        testArgs.append([node2, node3])

        # 2
        #  3
        #   4
        #    5
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        ConnectTreeNodes(node2, None, node3)
        ConnectTreeNodes(node3, None, node4)
        ConnectTreeNodes(node4, None, node5)
        testArgs.append([node5, None])
        testArgs.append([node4, node5])
        testArgs.append([node3, node4])
        testArgs.append([node2, node3])

        # 单个结点
        testArgs.append([TreeNode(1), None])

        # 空树
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
