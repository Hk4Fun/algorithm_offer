__author__ = 'Hk4Fun'
__date__ = '2018/2/25 0:33'

'''题目描述：
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
'''主要思路：
思路1：两个栈实现。奇数层打印时先保存左孩子再保存右孩子到另一个栈里，
       这样在打印偶数层时就会先打印右孩子再打印左孩子
       同理，偶数层在打印时反过来先右后左保存子结点。为什么必须两个栈？
       因为在弹栈的同时要压子结点入栈，所以必须要用另一个栈来保存，
       否则顺序错乱。
思路2：一个队列实现。类似60题，用一个队列来保存即可，只不过在打印时奇数层
       append(cur.val)而偶数层insert(0, cur.val)。为什么可以只用一个队列来完成？
       因为队列取数和存数在两头，而栈都在同一头，所以队列可以保证存数时不影响取数。
       每次在取出本层结点时固定本层的结点数即可，不会越界取出下一层的结点，
       使得下一层的结点能在下一个循环取出。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def ZigZagOrder1(self, pRoot):
        if not pRoot:
            return []
        current = 0  # 0表示当前正在打印奇数层， 1表示当前正在打印偶数层
        next = 1  # 1表示保存在偶数层，0表示保存在奇数层
        stack = [[], []]  # 奇偶栈
        result = [[]]
        stack[current].append(pRoot)
        while stack[0] or stack[1]:
            node = stack[current].pop()
            result[-1].append(node.val)
            if current == 0:  # 如果当前正在打印奇数层
                if node.left:
                    stack[next].append(node.left)  # 保存子结点于偶数层
                if node.right:
                    stack[next].append(node.right)
            else:  # 如果当前正在打印偶数层
                if node.right:
                    stack[next].append(node.right)  # 保存子结点于奇数层
                if node.left:
                    stack[next].append(node.left)
            if not stack[current]: # 当前层次中所有结点遍历完
                result.append([])
                current = 1 - current # 进入下一层
                next = 1 - next
        return result[:-1]

    def ZigZagOrder2(self, pRoot):
        if not pRoot:
            return []
        next = 0 # 0 表示奇数层，1表示偶数层
        result = []
        queue = [pRoot]
        while queue:
            result.append([])
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if next == 0: # 奇数层把出队的结点放到列表后面
                    result[-1].append(cur.val)
                else:# 偶数层把出队的结点插到列表前面
                    result[-1].insert(0, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            next = 1 - next
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

        #              8
        #      4              12
        #   2     6       10      14
        # 1  3  5  7     9 11   13  15
        node8 = TreeNode(8)
        node4 = TreeNode(4)
        node12 = TreeNode(12)
        node2 = TreeNode(2)
        node6 = TreeNode(6)
        node10 = TreeNode(10)
        node14 = TreeNode(14)
        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node11 = TreeNode(11)
        node13 = TreeNode(13)
        node15 = TreeNode(15)
        ConnectTreeNodes(node8, node4, node12)
        ConnectTreeNodes(node4, node2, node6)
        ConnectTreeNodes(node12, node10, node14)
        ConnectTreeNodes(node2, node1, node3)
        ConnectTreeNodes(node6, node5, node7)
        ConnectTreeNodes(node10, node9, node11)
        ConnectTreeNodes(node14, node13, node15)
        testArgs.append([node8, [[8], [12, 4], [2, 6, 10, 14], [15, 13, 11, 9, 7, 5, 3, 1]]])

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
        testArgs.append([node8, [[8], [10, 6], [5, 7, 9, 11]]])

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
