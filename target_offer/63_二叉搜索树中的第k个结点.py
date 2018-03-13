__author__ = 'Hk4Fun'
__date__ = '2018/2/25 22:24'

'''题目描述：
给定一棵二叉搜索树，请找出其中的第k大的结点。例如，
     5
   /   \ 
  3     7
 / \   / \ 
2   4  6  8 中，
按结点数值大小顺序第三个结点的值为4。
'''
'''主要思路：
思路1：二叉搜索树的中序遍历序列是递增排序的，所以中序遍历二叉树，递归实现，找到就返回
思路2：先中序遍历完整棵树到列表中，在从中返回第k个结点。该算法虽然需要遍历完整棵树，但代码简洁
思路3：思路1的非递归实现，也是找到就返回。用栈来实现中序遍历的非递归
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回结点而不是结点的值
    def KthNode1(self, pRoot, k):
        def inOrder(root):
            nonlocal k
            if not root:
                return
            target = inOrder(root.left)
            if target:  # 找到就直接返回
                return target
            # 没找到就继续找中间
            k -= 1
            if k == 0:
                return root  # 找到就直接返回
            return inOrder(root.right)  # 没找到就继续找右边

        if not pRoot or k < 1:
            return
        return inOrder(pRoot)

    def KthNode2(self, pRoot, k):
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            result.append(root)
            inOrder(root.right)

        result = []
        inOrder(pRoot)
        return result[k - 1] if 1 <= k <= len(result) else None

    def KthNode3(self, pRoot, k):
        if not pRoot or k < 1:
            return
        stack = []
        while stack or pRoot:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop()
            k -= 1
            if k == 0:
                return pRoot  # 找到就直接返回
            pRoot = pRoot.right


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
        testArgs.append([node8, 0, None])
        testArgs.append([node8, 1, node5])
        testArgs.append([node8, 2, node6])
        testArgs.append([node8, 3, node7])
        testArgs.append([node8, 4, node8])
        testArgs.append([node8, 5, node9])
        testArgs.append([node8, 6, node10])
        testArgs.append([node8, 7, node11])
        testArgs.append([node8, 8, None])

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
        testArgs.append([node5, 1, node2])
        testArgs.append([node5, 2, node3])
        testArgs.append([node5, 3, node4])
        testArgs.append([node5, 4, node5])

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
        testArgs.append([node5, 1, node5])
        testArgs.append([node5, 2, node4])
        testArgs.append([node5, 3, node3])
        testArgs.append([node5, 4, node2])

        node1 = TreeNode(1)
        testArgs.append([node1, -1, None])
        testArgs.append([node1, 1, node1])
        testArgs.append([node1, 10, None])

        testArgs.append([None, 1, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
