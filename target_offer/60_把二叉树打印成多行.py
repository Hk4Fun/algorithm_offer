__author__ = 'Hk4Fun'
__date__ = '2018/2/23 22:19'

'''题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
'''主要思路：
思路1： 层次遍历，队列实现
思路2： 因为前序，中序和后序遍历都是先左后右，所以和层次遍历是类似的，
        我们只需在递归时多传递一个当前结点所在层次的变量即可实现，这里采用前序遍历
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表
    def levelOrder1(self, pRoot):
        if not pRoot:
            return []
        result = []
        queue = [pRoot]
        while queue:
            result.append([])  # 用来保存当前层次结点的值
            # len(queue)保证了每次只会遍历当前层次的结点，
            # 后加入的结点（即下一层结点）下一循环才会被遍历
            for _ in range(len(queue)):
                cur = queue.pop(0)
                result[-1].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result

    def levelOrder2(self, pRoot):
        def preOrder(root, depth):
            if not root:
                return
            if depth > len(result):  # 大于当前层次，说明来到新的层次
                result.append([])  # 添加新的层次
            result[depth - 1].append(root.val)  # 找到该结点所在层次的列表并添加值
            preOrder(root.left, depth + 1)
            preOrder(root.right, depth + 1)

        if not pRoot:
            return []
        result = []
        preOrder(pRoot, 1)
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
        testArgs.append([node8, [[8], [6, 10], [5, 7, 9, 11]]])

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
        testArgs.append([node5, [[5], [4], [3], [2]]])

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
        testArgs.append([node5, [[5], [4], [3], [2]]])

        #  100
        #  /
        # 50
        #   \
        #   150
        node100 = TreeNode(100)
        node50 = TreeNode(50)
        node150 = TreeNode(150)
        ConnectTreeNodes(node100, node50, None)
        ConnectTreeNodes(node50, None, node150)
        testArgs.append([node100, [[100], [50], [150]]])

        testArgs.append([TreeNode(1), [[1]]])
        testArgs.append([None, []])
        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
