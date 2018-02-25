__author__ = 'Hk4Fun'
__date__ = '2018/2/25 20:03'

'''题目描述：
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''
'''主要思路：
序列化可以采用多种遍历方式，本来可以仿照第6题序列化成前序+中序或后序+中序，
但这要求结点值不能重复，所以不能使用双遍历的方式。采用单遍历就允许结点值重复，
可是单次遍历是无法确定一个二叉树的，所以可以在遍历到None时也加入遍历序列中。
这里的序列化字符串用‘#’表示None，且采用层次遍历。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 先序列化再反序列化，最终返回反序列化后的树的根结点
    def Serialize(self, root):
        def serialize(root):
            if not root:
                return '#'
            serializeStr = ''
            queue = [root]
            while queue:
                cur = queue.pop(0)
                if cur:
                    serializeStr += str(cur.val) + ','
                else:
                    serializeStr += '#,'  # 遇到None使用#替代
                    continue
                if cur.left:
                    queue.append(cur.left)
                else:
                    queue.append(None)
                if cur.right:
                    queue.append(cur.right)
                else:
                    queue.append(None)
            return serializeStr[:-1]

        def deserialize(s):
            s = s.split(',')
            if s[0] == '#':
                return
            TreeRoot = TreeNode(int(s[0]))
            queue = [TreeRoot]
            for i in range(1, len(s), 2):  # s的长度一定为奇数
                SubTreeRoot = queue.pop(0)
                if s[i] != '#':  # 连接左孩子
                    left = TreeNode(int(s[i]))
                    queue.append(left)
                    SubTreeRoot.left = left
                if s[i + 1] != '#':  # 连接右孩子
                    right = TreeNode(int(s[i + 1]))
                    queue.append(right)
                    SubTreeRoot.right = right
            return TreeRoot

        serializeStr = serialize(root)
        return deserialize(serializeStr)


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

        #    5
        #     5
        #      5
        #     5
        #    5
        #   5 5
        #  5   5
        node1 = TreeNode(5)
        node2 = TreeNode(5)
        node3 = TreeNode(5)
        node4 = TreeNode(5)
        node5 = TreeNode(5)
        node61 = TreeNode(5)
        node62 = TreeNode(5)
        node71 = TreeNode(5)
        node72 = TreeNode(5)
        ConnectTreeNodes(node1, None, node2)
        ConnectTreeNodes(node2, None, node3)
        ConnectTreeNodes(node3, node4, None)
        ConnectTreeNodes(node4, node5, None)
        ConnectTreeNodes(node5, node61, node62)
        ConnectTreeNodes(node61, node71, None)
        ConnectTreeNodes(node62, None, node72)
        testArgs.append([node1, [[5], [5], [5], [5], [5], [5, 5], [5, 5]]])

        testArgs.append([TreeNode(1), [[1]]])
        testArgs.append([None, []])

        return testArgs

    def convert(self, result, *func_arg):
        if result and result == func_arg[0]:  # 防止直接返回原树根结点
            return
        # 用层次遍历检测返回的新树
        pRoot = result
        if not pRoot:
            return []
        result = []
        queue = [pRoot]
        while queue:
            result.append([])
            for i in range(len(queue)):
                cur = queue.pop(0)
                result[-1].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
