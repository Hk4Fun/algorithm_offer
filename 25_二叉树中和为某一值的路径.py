__author__ = 'Hk4Fun'
__date__ = '2018/2/2 17:07'

'''题目描述：
输入一颗二叉树和一个整数，输出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''
'''主要思路：
深度遍历DFS，具体见代码和注释
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectedSum):
        total_path = []
        path = []
        currentSum = 0
        if root:
            self.find(root, expectedSum, path, total_path, currentSum)
        return total_path

    def find(self, root, expectedSum, path, total_path, currentSum):
        # 每遍历一个结点就把该结点加入路径中，更新currentSum
        currentSum += root.val
        path.append(root.val)

        # 如果是叶结点，并且路径上结点的和等于输入的值，则找到新的路径
        isLeaf = not (root.left or root.right)
        if currentSum == expectedSum and isLeaf:
            total_path.append(path[:])  # 注意这里应该是path的拷贝，否则后面path改变，这里也会一起改变

        # 不是叶结点的话就遍历它的左右子结点
        if root.left:
            self.find(root.left, expectedSum, path, total_path, currentSum)

        if root.right:
            self.find(root.right, expectedSum, path, total_path, currentSum)

        # 在返回父节点之前，在路径上删除当前结点，并在currentSum中减去当前结点的值
        # 最终遍历整棵树，找到所有路径
        currentSum -= root.val
        path.pop(-1)

        # 注意：其实当currentSum > expectedSum 时就没有必要往下遍历了，可以直接回溯
        # 即可以适当剪枝，提高遍历速度，但此题并没有说明全部结点值都大于0，
        # 说明后面可能有负数使得currentSum会减回来等于expectedSum，所以这里没有剪枝而是到叶结点才返回


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def ConnectTreeNodes(rootNode, leftNode, rightNode):
    rootNode.left = leftNode
    rootNode.right = rightNode


def Test(testName, root, expectedSum, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.FindPath(root, expectedSum)
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


# 有两条路径上的结点和为22
#     10
#    /  \
#   5   12
#  /\
# 4  7
treeNode10 = TreeNode(10)
treeNode5 = TreeNode(5)
treeNode12 = TreeNode(12)
treeNode4 = TreeNode(4)
treeNode7 = TreeNode(7)

ConnectTreeNodes(treeNode10, treeNode5, treeNode12)
ConnectTreeNodes(treeNode5, treeNode4, treeNode7)
Test('Test1', treeNode10, 22, [[10, 5, 7], [10, 12]])

# 没有路径上的结点和为15
Test('Test2', treeNode10, 15, [])

# 有一条路径上面的结点和为15
#         5
#        /
#       4
#      /
#     3
#    /
#   2
#  /
# 1
treeNode5 = TreeNode(5)
treeNode4 = TreeNode(4)
treeNode3 = TreeNode(3)
treeNode2 = TreeNode(2)
treeNode1 = TreeNode(1)
ConnectTreeNodes(treeNode5, treeNode4, None)
ConnectTreeNodes(treeNode4, treeNode3, None)
ConnectTreeNodes(treeNode3, treeNode2, None)
ConnectTreeNodes(treeNode2, treeNode1, None)
Test('Test3', treeNode5, 15, [[5, 4, 3, 2, 1]])

# 没有路径上面的结点和为16
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#          5
treeNode5 = TreeNode(5)
treeNode4 = TreeNode(4)
treeNode3 = TreeNode(3)
treeNode2 = TreeNode(2)
treeNode1 = TreeNode(1)
ConnectTreeNodes(treeNode1, None, treeNode2)
ConnectTreeNodes(treeNode2, None, treeNode3)
ConnectTreeNodes(treeNode3, None, treeNode4)
ConnectTreeNodes(treeNode4, None, treeNode5)
Test('Test4', treeNode5, 16, [])

# 结点值出现负数，检测剪枝
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         -3
treeNode_3 = TreeNode(-3)
treeNode4 = TreeNode(4)
treeNode3 = TreeNode(3)
treeNode2 = TreeNode(2)
treeNode1 = TreeNode(1)
ConnectTreeNodes(treeNode1, None, treeNode2)
ConnectTreeNodes(treeNode2, None, treeNode3)
ConnectTreeNodes(treeNode3, None, treeNode4)
ConnectTreeNodes(treeNode4, None, treeNode_3)
Test('Test5', treeNode1, 7, [[1, 2, 3, 4, -3]])

# 树中只有1个结点且存在路径
Test('Test6', TreeNode(1), 1, [[1]])

# 树中只有1个结点但不存在路径
Test('Test7', TreeNode(1), 2, [])

# 树中没有结点
Test('Test8', None, 0, [])

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
