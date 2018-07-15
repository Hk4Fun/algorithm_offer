__author__ = 'Hk4Fun'
__date__ = '2018/2/23 19:20'

'''题目描述：
前面几道题的前提是结点有指向父结点的指针，假如没有该指针，如何找到结点的父结点？
实现一个函数返回二叉树中某个结点的父结点（整棵树的根结点的父结点是自己）
'''
'''主要思路：
思路1：层次遍历
思路2：前序遍历（中序后序都行）
思路3：思路2的非递归实现
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def parent1(self, pRoot, node):
        if not pRoot or not node:
            return
        if pRoot is node:
            return pRoot
        queue = [pRoot]
        while queue:
            parent = queue.pop(0)
            if parent.left is node or parent.right is node:
                return parent
            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)

    def parent2(self, pRoot, node):
        def postOrder(root, node):
            if not root:
                return
            if root.left is node or root.right is node:
                return root
            parent = postOrder(root.left, node)
            if parent:  # 找到就一路返回
                return parent
            return postOrder(root.right, node)

        if not pRoot or not node:
            return
        if pRoot is node:
            return pRoot
        return postOrder(pRoot, node)

    def parent3(self, pRoot, node):
        if not pRoot or not node:
            return
        if pRoot is node:
            return pRoot
        stack = []
        while stack or pRoot:
            while pRoot:
                if pRoot.left is node or pRoot.right is node:
                    return pRoot
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop().right


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def ConnectTreeNodes(rootNode, leftNode, rightNode):
            rootNode.left = leftNode
            rootNode.right = rightNode

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
        testArgs.append([node8, node8, node8])
        testArgs.append([node8, node6, node8])
        testArgs.append([node8, node10, node8])
        testArgs.append([node8, node5, node6])
        testArgs.append([node8, node7, node6])
        testArgs.append([node8, node9, node10])
        testArgs.append([node8, node11, node10])
        testArgs.append([node8, None, None])
        testArgs.append([node8, TreeNode(1), None])  # 结点不在二叉树中

        #       5
        #     4
        #   3
        # 2
        node5 = TreeNode(5)
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        ConnectTreeNodes(node5, node4, None)
        ConnectTreeNodes(node4, node3, None)
        ConnectTreeNodes(node3, node2, None)
        testArgs.append([node5, node5, node5])
        testArgs.append([node5, node4, node5])
        testArgs.append([node5, node3, node4])
        testArgs.append([node5, node2, node3])
        testArgs.append([node8, None, None])

        # 5
        #  4
        #   3
        #    2
        node5 = TreeNode(5)
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        ConnectTreeNodes(node5, None, node4)
        ConnectTreeNodes(node4, None, node3)
        ConnectTreeNodes(node3, None, node2)
        testArgs.append([node5, node5, node5])
        testArgs.append([node5, node4, node5])
        testArgs.append([node5, node3, node4])
        testArgs.append([node5, node2, node3])
        testArgs.append([node8, None, None])

        node1 = TreeNode(1)
        testArgs.append([node1, node1, node1])

        testArgs.append([None, None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result

    def checked(self, result, expected, *func_arg):
        return result.val == expected.val if result else result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
