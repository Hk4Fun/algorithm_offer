__author__ = 'Hk4Fun'
__date__ = '2018/2/23 19:12'

'''题目描述：
给定一个二叉树和其中的一个结点，请找出后序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''主要思路：
思路1：若该结点的父结点无右孩子或其父结点的右孩子就是自己，则后序遍历顺序的下一个结点
       就是其父结点；否则若该结点的父结点有右孩子则后序遍历顺序的下一个结点为
       以其父结点的右孩子为根的子树的最左叶结点。如何找出该最左叶结点？
       类似于寻找最右叶结点，只不过在这里是左孩子优先：从其父结点的右孩子开始向下迭代遍历，
       有左孩子就迭代左孩子，没有就迭代右孩子，即优先迭代左孩子，都没有说明来到了那个最左叶结点
思路2：既然是后序遍历，那就先后序遍历整棵树，把结点都存放在数组里，
       然后在数组里找到所给结点的下一个结点，当然如果所给结点在最后则返回None
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
        if not pNode or not pNode.parent:
            return
        if not pNode.parent.right or pNode.parent.right == pNode:
            return pNode.parent
        if pNode.parent.right:
            pNode = pNode.parent.right
            while True:
                if pNode.left:
                    pNode = pNode.left
                elif pNode.right:
                    pNode = pNode.right
                else:
                    break
            return pNode

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
    #     return treeNodes[index + 1] if index != len(treeNodes) - 1 else None


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
        testArgs.append([node8, None])
        testArgs.append([node6, node11])
        testArgs.append([node10, node8])
        testArgs.append([node5, node4])
        testArgs.append([node7, node6])
        testArgs.append([node9, node10])
        testArgs.append([node11, node9])
        testArgs.append([node4, node7])

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
        testArgs.append([node5, node4])
        testArgs.append([node4, node3])
        testArgs.append([node3, node2])
        testArgs.append([node2, None])

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
        testArgs.append([node2, None])
        testArgs.append([node3, node6])
        testArgs.append([node5, node3])
        testArgs.append([node4, node2])
        testArgs.append([node6, node4])

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
            return treeNodes[index + 1] if index != len(treeNodes) - 1 else None

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
