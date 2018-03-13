__author__ = 'Hk4Fun'
__date__ = '2018/1/30 18:14'

'''题目描述：
输入两棵二叉树A，B，判断B是不是A的子结构（空树不是任意一个树的子结构）
'''
'''主要思路：
先递归遍历（先序遍历）树A，找到相同的根结点子树，
再用递归分别判断该子树的左右子树是否与B一样，递归结束的条件是来到B的叶结点
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        def DoesTree1haveTree2(pRoot1, pRoot2):
            # 用于递归判断树的每个节点是否相同
            # 需要注意的地方是: 前两个if语句不可以颠倒顺序
            # 如果颠倒顺序, 会先判断pRoot1是否为None,
            # 其实这个时候pRoot2的结点已经遍历完成确定相等了,
            # 但是返回了False, 判断错误
            if not pRoot2:  # 来到B的叶结点，递归遍历结束，结构一致
                return True
            if not pRoot1:
                return False
            if pRoot1.val != pRoot2.val:
                return False
            return DoesTree1haveTree2(pRoot1.left, pRoot2.left) \
                   and DoesTree1haveTree2(pRoot1.right, pRoot2.right)

        if pRoot1 and pRoot2:
            return True if DoesTree1haveTree2(pRoot1, pRoot2) \
                else (self.HasSubtree(pRoot1.left, pRoot2)
                      or self.HasSubtree(pRoot1.right, pRoot2))
        return False


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

        # 树中结点含有分叉，树B是树A的子结构
        #                8              8
        #              /   \           / \
        #             8     7         9   2
        #           /   \                  \
        #          9     2                  7
        #               / \
        #              4   7
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(8)
        treeNodeA3 = TreeNode(7)
        treeNodeA4 = TreeNode(9)
        treeNodeA5 = TreeNode(2)
        treeNodeA6 = TreeNode(4)
        treeNodeA7 = TreeNode(7)
        ConnectTreeNodes(treeNodeA1, treeNodeA2, treeNodeA3)
        ConnectTreeNodes(treeNodeA2, treeNodeA4, treeNodeA5)
        ConnectTreeNodes(treeNodeA5, treeNodeA6, treeNodeA7)

        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(2)
        treeNodeB4 = TreeNode(7)
        ConnectTreeNodes(treeNodeB1, treeNodeB2, treeNodeB3)
        ConnectTreeNodes(treeNodeB3, None, treeNodeB4)
        testArgs.append([treeNodeA1, treeNodeB1, True])

        # 树中结点含有分叉，树B不是树A的子结构
        #                  8                8
        #              /       \           / \
        #             8         7         9   2
        #           /   \                    /
        #          9     2                  7
        #               / \
        #              4   7
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(8)
        treeNodeA3 = TreeNode(7)
        treeNodeA4 = TreeNode(9)
        treeNodeA5 = TreeNode(2)
        treeNodeA6 = TreeNode(4)
        treeNodeA7 = TreeNode(7)
        ConnectTreeNodes(treeNodeA1, treeNodeA2, treeNodeA3)
        ConnectTreeNodes(treeNodeA2, treeNodeA4, treeNodeA5)
        ConnectTreeNodes(treeNodeA5, treeNodeA6, treeNodeA7)

        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(2)
        treeNodeB4 = TreeNode(7)
        ConnectTreeNodes(treeNodeB1, treeNodeB2, treeNodeB3)
        ConnectTreeNodes(treeNodeB3, treeNodeB4, None)
        testArgs.append([treeNodeA1, treeNodeB1, False])

        # 树中结点只有左子结点，树B是树A的子结构
        #                8                  8
        #              /                   /
        #             8                   9
        #           /                    /
        #          9                    2
        #         /
        #        2
        #       /
        #      5
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(8)
        treeNodeA3 = TreeNode(9)
        treeNodeA4 = TreeNode(2)
        treeNodeA5 = TreeNode(5)
        ConnectTreeNodes(treeNodeA1, treeNodeA2, None)
        ConnectTreeNodes(treeNodeA2, treeNodeA3, None)
        ConnectTreeNodes(treeNodeA3, treeNodeA4, None)
        ConnectTreeNodes(treeNodeA4, treeNodeA5, None)

        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(2)
        ConnectTreeNodes(treeNodeB1, treeNodeB2, None)
        ConnectTreeNodes(treeNodeB2, treeNodeB3, None)
        testArgs.append([treeNodeA1, treeNodeB1, True])

        # 树中结点只有左子结点，树B不是树A的子结构
        #                8                  8
        #              /                   /
        #             8                   9
        #           /                    /
        #          9                    3
        #         /
        #        2
        #       /
        #      5
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(8)
        treeNodeA3 = TreeNode(9)
        treeNodeA4 = TreeNode(2)
        treeNodeA5 = TreeNode(5)
        ConnectTreeNodes(treeNodeA1, treeNodeA2, None)
        ConnectTreeNodes(treeNodeA2, treeNodeA3, None)
        ConnectTreeNodes(treeNodeA3, treeNodeA4, None)
        ConnectTreeNodes(treeNodeA4, treeNodeA5, None)

        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(3)
        ConnectTreeNodes(treeNodeB1, treeNodeB2, None)
        ConnectTreeNodes(treeNodeB2, treeNodeB3, None)
        testArgs.append([treeNodeA1, treeNodeB1, False])

        # 树中结点只有右子结点，树B是树A的子结构
        #       8                   8
        #        \                   \
        #         8                   9
        #          \                   \
        #           9                   2
        #            \
        #             2
        #              \
        #               5
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(8)
        treeNodeA3 = TreeNode(9)
        treeNodeA4 = TreeNode(2)
        treeNodeA5 = TreeNode(5)
        ConnectTreeNodes(treeNodeA1, None, treeNodeA2)
        ConnectTreeNodes(treeNodeA2, None, treeNodeA3)
        ConnectTreeNodes(treeNodeA3, None, treeNodeA4)
        ConnectTreeNodes(treeNodeA4, None, treeNodeA5)

        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(2)
        ConnectTreeNodes(treeNodeB1, None, treeNodeB2)
        ConnectTreeNodes(treeNodeB2, None, treeNodeB3)
        testArgs.append([treeNodeA1, treeNodeB1, True])

        # 树A中结点只有右子结点，树B不是树A的子结构
        #       8                   8
        #        \                   \
        #         8                   9
        #          \                 / \
        #           9               3   2
        #            \
        #             2
        #              \
        #               5
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(8)
        treeNodeA3 = TreeNode(9)
        treeNodeA4 = TreeNode(2)
        treeNodeA5 = TreeNode(5)
        ConnectTreeNodes(treeNodeA1, None, treeNodeA2)
        ConnectTreeNodes(treeNodeA2, None, treeNodeA3)
        ConnectTreeNodes(treeNodeA3, None, treeNodeA4)
        ConnectTreeNodes(treeNodeA4, None, treeNodeA5)

        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(3)
        treeNodeB4 = TreeNode(2)
        ConnectTreeNodes(treeNodeB1, None, treeNodeB2)
        ConnectTreeNodes(treeNodeB2, treeNodeB3, treeNodeB4)
        testArgs.append([treeNodeA1, treeNodeB1, False])

        # 树A为空树
        treeNodeB1 = TreeNode(8)
        treeNodeB2 = TreeNode(9)
        treeNodeB3 = TreeNode(3)
        treeNodeB4 = TreeNode(2)
        ConnectTreeNodes(treeNodeB1, None, treeNodeB2)
        ConnectTreeNodes(treeNodeB2, treeNodeB3, treeNodeB4)
        testArgs.append([None, treeNodeB1, False])

        # 树B为空树
        treeNodeA1 = TreeNode(8)
        treeNodeA2 = TreeNode(9)
        treeNodeA3 = TreeNode(3)
        treeNodeA4 = TreeNode(2)
        ConnectTreeNodes(treeNodeA1, None, treeNodeA2)
        ConnectTreeNodes(treeNodeA2, treeNodeA3, treeNodeA4)
        testArgs.append([treeNodeA1, None, False])

        # 树A和树B都为空
        testArgs.append([None, None, False])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
