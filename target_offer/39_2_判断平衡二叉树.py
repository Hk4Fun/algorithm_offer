__author__ = 'Hk4Fun'
__date__ = '2018/2/14 0:22'

'''题目描述：
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
注：平衡二叉树任意结点的左右子树深度相差不超过1，空树算平衡二叉树
'''
'''主要思路：
每个结点都要看自己是否平衡，这需要知道左右子树的深度，
平衡的话再看左右子树是否平衡。或者先检查左右子树再检查自己。
思路1：根据平衡二叉树的定义，只需遍历每个结点，看它的左右子树深度相差是否不超过1，
       然后再判断它的左右子树是否也都为平衡二叉树。这种算法需要重复遍历结点多次，
       虽然简单但时间效率不高
思路2：根据后序遍历的特点，当遍历到某一结点时该结点的左右子树已经遍历结束。
       因此在遍历每个结点的时候记录以它为根节点的树的深度，这样在遍历到某个结点时
       既知道了左右子树的深度，也知道左右子树是否为平衡二叉树(递归)，即一边计算深度一边判断是否平衡。
       书上用变量left和right来单独表示左右子树的深度，函数返回的是true或者false，
       其实不用这两个变量，我们直接把树的深度返回即可，这样根节点可直接拿到左右子树的深度，
       因为我们注意到深度总是大于等于0的，所以我们只需定义当子树不平衡时返回-1即可，
       这样根节点也就可以通过左右子树返回的深度是否大于等于0来间接判断左右子树是否平衡
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced1(self, pRoot):
        def TreeDepth(pRoot):
            if not pRoot: return 0
            return max(TreeDepth(pRoot.left), TreeDepth(pRoot.right)) + 1

        if not pRoot:  # 空树算平衡二叉树
            return True
        if abs(TreeDepth(pRoot.left) - TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced1(pRoot.left) and self.IsBalanced1(pRoot.right)

    def IsBalanced2(self, pRoot):
        def balanceHeight(root):
            if not root:
                return 0
            left = balanceHeight(root.left)
            right = balanceHeight(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return balanceHeight(pRoot) >= 0


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

        self.debug = True
        testArgs = []

        # 完全二叉树
        #        1
        #    /      \
        #   2        3
        #  /\       / \
        # 4  5     6   7
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
        testArgs.append([treeNode1, True])

        # 不是完全二叉树，但是平衡二叉树
        #        1
        #    /      \
        #   2        3
        #  /\         \
        # 4  5         6
        #   /
        #  7
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        treeNode6 = TreeNode(6)
        treeNode7 = TreeNode(7)
        ConnectTreeNodes(treeNode1, treeNode2, treeNode3)
        ConnectTreeNodes(treeNode2, treeNode4, treeNode5)
        ConnectTreeNodes(treeNode3, None, treeNode6)
        ConnectTreeNodes(treeNode5, treeNode7, None)
        testArgs.append([treeNode1, True])

        # 不是平衡二叉树
        #         1
        #     /      \
        #    2        3
        #   /\
        #  4  5
        #    /
        #   6
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        treeNode6 = TreeNode(6)
        ConnectTreeNodes(treeNode1, treeNode2, treeNode3)
        ConnectTreeNodes(treeNode2, treeNode4, treeNode5)
        ConnectTreeNodes(treeNode5, treeNode6, None)
        testArgs.append([treeNode1, False])

        #         1
        #        /
        #       2
        #      /
        #     3
        #    /
        #   4
        #  /
        # 5
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        ConnectTreeNodes(treeNode1, treeNode2, None)
        ConnectTreeNodes(treeNode2, treeNode3, None)
        ConnectTreeNodes(treeNode3, treeNode4, None)
        ConnectTreeNodes(treeNode4, treeNode5, None)
        testArgs.append([treeNode1, False])

        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        #        \
        #         5
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        ConnectTreeNodes(treeNode1, None, treeNode2)
        ConnectTreeNodes(treeNode2, None, treeNode3)
        ConnectTreeNodes(treeNode3, None, treeNode4)
        ConnectTreeNodes(treeNode4, None, treeNode5)
        testArgs.append([treeNode1, False])

        # 树中只有1个结点
        treeNode1 = TreeNode(1)
        testArgs.append([treeNode1, True])

        # 树中没有结点
        testArgs.append([None, True])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
