__author__ = 'Hk4Fun'
__date__ = '2018/2/23 18:48'

'''题目描述：
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
'''主要思路：
思路1：前序、中序、后序、层次遍历都行，这里采用前序
       先前序遍历(MLR)再对称前序遍历(MRL)，遍历到None也要放进数组中
       （针对所有结点数值都相等的二叉树），如果两个序列一致则为对称
思路2：递归实现，把当前结点的左右子树看成俩棵树，只有当左树的左子树和右树的右子树相同
       并且左树的右子树和右树的左子树相同才对称
思路3：非递归实现，但思路不变，一个先左后右一个先右后左，使用层次遍历

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical1(self, pRoot):
        def preOrder(root):
            if not root:
                preList.append(None)
                return
            preList.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        def mirrorPreOrder(root):
            if not root:
                mirrorList.append(None)
                return
            mirrorList.append(root.val)
            mirrorPreOrder(root.right)
            mirrorPreOrder(root.left)

        preList = []
        preOrder(pRoot)
        mirrorList = []
        mirrorPreOrder(pRoot)
        return preList == mirrorList

    def isSymmetrical2(self, pRoot):
        def isSymmetrical(root1, root2):
            if root1 and root2 and root1.val == root2.val:
                return isSymmetrical(root1.left, root2.right) and isSymmetrical(root1.right, root2.left)
            return not root1 and not root2  # 两个都为None时返回True，一个为None另一个非None时返回False

        return isSymmetrical(pRoot, pRoot)  # 把一棵树当成两棵树来遍历，一个MLR一个MRL

    def isSymmetrical3(self, pRoot):
        if not pRoot:
            return True
        leftQueue, rightQueue = [pRoot.left], [pRoot.right]
        while leftQueue and rightQueue:
            left, right = leftQueue.pop(0), rightQueue.pop(0)
            if left and right:
                if left.val != right.val:
                    return False
                leftQueue.append(left.left)
                rightQueue.append(right.right)
            elif not left and not right:  # 两边都为None
                continue
            else:  # 只有一边为None
                return False
        return True


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

        #       8
        #   6      6
        #  5 7    7 5
        node8 = TreeNode(8)
        node61 = TreeNode(6)
        node62 = TreeNode(6)
        node51 = TreeNode(5)
        node71 = TreeNode(7)
        node72 = TreeNode(7)
        node52 = TreeNode(5)
        ConnectTreeNodes(node8, node61, node62)
        ConnectTreeNodes(node61, node51, node71)
        ConnectTreeNodes(node62, node72, node52)
        testArgs.append([node8, True])

        #       8
        #   6      9
        #  5 7    7 5
        node8 = TreeNode(8)
        node61 = TreeNode(6)
        node9 = TreeNode(9)
        node51 = TreeNode(5)
        node71 = TreeNode(7)
        node72 = TreeNode(7)
        node52 = TreeNode(5)
        ConnectTreeNodes(node8, node61, node9)
        ConnectTreeNodes(node61, node51, node71)
        ConnectTreeNodes(node9, node72, node52)
        testArgs.append([node8, False])

        #       8
        #   6      6
        #  5 7    7
        node8 = TreeNode(8)
        node61 = TreeNode(6)
        node62 = TreeNode(6)
        node51 = TreeNode(5)
        node71 = TreeNode(7)
        node72 = TreeNode(7)
        ConnectTreeNodes(node8, node61, node62)
        ConnectTreeNodes(node61, node51, node71)
        ConnectTreeNodes(node62, node72, None)
        testArgs.append([node8, False])

        #     5
        #    / \
        #   3   3
        #  /     \
        # 4       4
        node5 = TreeNode(5)
        node31 = TreeNode(3)
        node32 = TreeNode(3)
        node41 = TreeNode(4)
        node42 = TreeNode(4)
        ConnectTreeNodes(node5, node31, node32)
        ConnectTreeNodes(node31, node41, None)
        ConnectTreeNodes(node32, None, node42)
        testArgs.append([node5, True])

        #     5
        #    / \
        #   3   2
        #  /     \
        # 4       4
        node5 = TreeNode(5)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node41 = TreeNode(4)
        node42 = TreeNode(4)
        ConnectTreeNodes(node5, node3, node2)
        ConnectTreeNodes(node3, node41, None)
        ConnectTreeNodes(node2, None, node42)
        testArgs.append([node5, False])

        #     5
        #    / \
        #   3   2
        #  /
        # 4
        node5 = TreeNode(5)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node4 = TreeNode(4)
        ConnectTreeNodes(node5, node3, node2)
        ConnectTreeNodes(node3, node4, None)
        testArgs.append([node5, False])

        #     1
        #    / \
        #   1   1
        #  /     \
        # 1       1
        node11 = TreeNode(1)
        node12 = TreeNode(1)
        node13 = TreeNode(1)
        node14 = TreeNode(1)
        node15 = TreeNode(1)
        ConnectTreeNodes(node11, node12, node13)
        ConnectTreeNodes(node12, node14, None)
        ConnectTreeNodes(node13, None, node15)
        testArgs.append([node11, True])

        #     1
        #    / \
        #   1   1
        #  /
        # 1
        node11 = TreeNode(1)
        node12 = TreeNode(1)
        node13 = TreeNode(1)
        node14 = TreeNode(1)
        ConnectTreeNodes(node11, node12, node13)
        ConnectTreeNodes(node12, node14, None)
        testArgs.append([node11, False])

        # 单结点和空树都是对称的
        testArgs.append([TreeNode(1), True])
        testArgs.append([None, True])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
