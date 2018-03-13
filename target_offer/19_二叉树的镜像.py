__author__ = 'Hk4Fun'
__date__ = '2018/1/30 22:40'

'''题目描述：
将给定的二叉树变换为原二叉树的镜像。
'''
'''主要思路：
思路1：递归实现，前序遍历二叉树的每个结点，如果遍历到的结点有子结点，就交换它的两个子结点，
       当交换完所有的非叶子结点的左右子结点之后，就得到了树的镜像
思路2：非递归实现，宽度优先遍历
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror1(self, root):
        if not root or (not root.left and not root.right):
            return root
        root.left, root.right = root.right, root.left
        self.Mirror1(root.left)
        self.Mirror1(root.right)
        return root

    def Mirror2(self, root):
        if not root:
            return
        nodeQue = [root]
        while nodeQue:
            pRoot = nodeQue.pop(0)
            pRoot.left, pRoot.right = pRoot.right, pRoot.left
            if pRoot.left:
                nodeQue.append(pRoot.left)
            if pRoot.right:
                nodeQue.append(pRoot.right)
        return root


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

        # 测试完全二叉树：除了叶子节点，其他节点都有两个子节点
        #            1
        #        2      3
        #       4 5    6  7
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        treeNode6 = TreeNode(6)
        treeNode7 = TreeNode(7)
        ConnectTreeNodes(treeNode1, treeNode2, treeNode3)
        ConnectTreeNodes(treeNode2, treeNode4, treeNode5)
        ConnectTreeNodes(treeNode3, treeNode6, treeNode7)
        testArgs.append([treeNode1, [1, 3, 2, 7, 6, 5, 4]])

        # 测试二叉树：出叶子结点之外，左右的结点都有且只有一个左子结点
        #            1
        #          2

        #        3
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        ConnectTreeNodes(treeNode1, treeNode2, None)
        ConnectTreeNodes(treeNode2, treeNode3, None)
        testArgs.append([treeNode1, [1, 2, 3]])

        # 测试二叉树：出叶子结点之外，左右的结点都有且只有一个右子结点
        #            1
        #             2
        #              3
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        ConnectTreeNodes(treeNode1, None, treeNode2)
        ConnectTreeNodes(treeNode2, None, treeNode3)
        testArgs.append([treeNode1, [1, 2, 3]])

        # 测试空二叉树：根结点为空指针
        testArgs.append([None, None])

        # 测试只有一个结点的二叉树
        treeNode1 = TreeNode(1)
        testArgs.append([treeNode1, [1]])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        def BFS(rootNode):  # 宽度优先搜索遍历二叉树，用来测试结果
            if not rootNode:
                return None
            l = []
            queue = [rootNode]  # 用列表模仿队列，左出右进
            while queue:
                node = queue.pop(0)
                if node:  # 每拿出一个结点就把其左右结点放入队列
                    l.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            return l

        return BFS(result)


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
