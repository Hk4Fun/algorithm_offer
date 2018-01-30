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
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    # 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    # 如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if not pRoot2:  # 来到B的叶结点，递归遍历结束，结构一致
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def ConnectTreeNodes(rootNode, leftNode, rightNode):
    rootNode.left = leftNode
    rootNode.right = rightNode


def Test(testName, treeNodeA, treeNodeB, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.HasSubtree(treeNodeA, treeNodeB)
        end = timeit.default_timer()

    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


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

Test('Test1', treeNodeA1, treeNodeB1, True)

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

Test('Test2', treeNodeA1, treeNodeB1, False)

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
Test('Test3', treeNodeA1, treeNodeB1, True)

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
Test('Test4', treeNodeA1, treeNodeB1, False)

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
Test('Test5', treeNodeA1, treeNodeB1, True)

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
Test('Test6', treeNodeA1, treeNodeB1, False)

# 树A为空树
treeNodeB1 = TreeNode(8)
treeNodeB2 = TreeNode(9)
treeNodeB3 = TreeNode(3)
treeNodeB4 = TreeNode(2)
ConnectTreeNodes(treeNodeB1, None, treeNodeB2)
ConnectTreeNodes(treeNodeB2, treeNodeB3, treeNodeB4)
Test('Test7', None, treeNodeB1, False)

# 树B为空树
treeNodeA1 = TreeNode(8)
treeNodeA2 = TreeNode(9)
treeNodeA3 = TreeNode(3)
treeNodeA4 = TreeNode(2)
ConnectTreeNodes(treeNodeA1, None, treeNodeA2)
ConnectTreeNodes(treeNodeA2, treeNodeA3, treeNodeA4)
Test('Test8', treeNodeA1, None, False)

# 树A和树B都为空
Test('Test8', None, None, False)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
