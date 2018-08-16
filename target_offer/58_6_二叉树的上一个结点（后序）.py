__author__ = 'Hk4Fun'
__date__ = '2018/2/23 19:12'

'''题目描述：
给定一个二叉树和其中的一个结点，请找出后序遍历顺序的上一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''主要思路：
思路1：若该结点有右孩子则下一个结点为该右孩子；
       否则若该结点有左孩子则下一个结点为该左孩子；
       既没有左孩子也没有右孩子，则下一个结点为第一个左兄弟（左堂兄弟）。
       如何找到第一个左兄弟（左堂兄弟）：
       向上迭代找到第一个其父亲的左孩子存在且不是自己的那个结点
       退到了根节点仍没找到则返回None
思路2：既然是后序遍历，那就先后序遍历整棵树，把结点都存放在数组里，
       然后在数组里找到所给结点的上一个结点，当然如果所给结点在最前则返回None
       (题目没给根结点，所以需要先找到根结点才能开始后序遍历，
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
        if pNode.right:
            return pNode.right
        if pNode.left:
            return pNode.left
        while pNode.parent:
            if pNode.parent.left and pNode.parent.left is not pNode:
                return pNode.parent.left
            pNode = pNode.parent

    # def GetNext2(self, pNode):
    #     def postTraversal(root, treeNodes):
    #         if not root: return
    #         postTraversal(root.left, treeNodes)
    #         postTraversal(root.right, treeNodes)
    #         treeNodes.append(root)
    #
    #     if not pNode:
    #         return
    #     cur = pNode
    #     while cur.parent:
    #         cur = cur.parent
    #     treeNodes = []
    #     postTraversal(cur, treeNodes)
    #     index = treeNodes.index(pNode)
    #     return treeNodes[index - 1] if index != 0 data_structures None


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

        self.debug = True
        testArgs = []

        #       8
        #   6      10
        # 5   7   9
        #    4     11
        node8 = TreeNode(8)
        node6 = TreeNode(6)
        node10 = TreeNode(10)
        node5 = TreeNode(5)
        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node11 = TreeNode(11)
        node4 = TreeNode(4)
        ConnectTreeNodes(node8, node6, node10)
        ConnectTreeNodes(node6, node5, node7)
        ConnectTreeNodes(node10, node9, None)
        ConnectTreeNodes(node9, None, node11)
        ConnectTreeNodes(node7, node4, None)
        testArgs.append([node8, node10])
        testArgs.append([node6, node7])
        testArgs.append([node10, node9])
        testArgs.append([node5, None])
        testArgs.append([node7, node4])
        testArgs.append([node9, node11])
        testArgs.append([node11, node6])
        testArgs.append([node4, node5])

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
        testArgs.append([node5, node4])
        testArgs.append([node4, node3])
        testArgs.append([node3, node2])
        testArgs.append([node2, None])

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

        #      2
        #    3   4
        #   5     6
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        ConnectTreeNodes(node2, node3, node4)
        ConnectTreeNodes(node3, node5, None)
        ConnectTreeNodes(node4, None, node6)
        testArgs.append([node2, node4])
        testArgs.append([node3, node5])
        testArgs.append([node5, None])
        testArgs.append([node4, node6])
        testArgs.append([node6, node3])

        # 单个结点
        testArgs.append([TreeNode(1), None])

        # 空树
        testArgs.append([None, None])

        # 随机生成二叉树进行测试

        def correct(pNode):
            def postTraversal(root, treeNodes):
                if not root: return
                postTraversal(root.left, treeNodes)
                postTraversal(root.right, treeNodes)
                treeNodes.append(root)

            if not pNode:
                return
            cur = pNode
            while cur.parent:
                cur = cur.parent
            treeNodes = []
            postTraversal(cur, treeNodes)
            index = treeNodes.index(pNode)
            return treeNodes[index - 1] if index != 0 else None

        import random
        tree_num = 1000  # 二叉树棵数
        node_num = 100  # 结点数

        for tree in range(tree_num):
            root = TreeNode(-1)
            nodeList = [root]
            randomList = [(root, 'l'), (root, 'r')]
            for i in range(random.randint(0, node_num)):
                newNode = TreeNode(i)
                nodeList.append(newNode)
                connect = random.choice(randomList)
                if connect[1] == 'l':
                    connect[0].left = newNode
                else:
                    connect[0].right = newNode
                newNode.parent = connect[0]
                randomList.remove(connect)
                randomList.append((newNode, 'l'))
                randomList.append((newNode, 'r'))
            for node in nodeList:
                testArgs.append([node, correct(node)])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
