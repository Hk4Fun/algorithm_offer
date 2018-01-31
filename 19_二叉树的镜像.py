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
            return
        root.left, root.right = root.right, root.left
        self.Mirror1(root.left)
        self.Mirror1(root.right)
    def Mirror2(self, root):
        if not root:
            return
        nodeQue = [root]
        while len(nodeQue):
            pRoot = nodeQue.pop(0)
            pRoot.left, pRoot.right = pRoot.right, pRoot.left
            if pRoot.left:
                nodeQue.append(pRoot.left)
            if pRoot.right:
                nodeQue.append(pRoot.right)

# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def ConnectTreeNodes(rootNode, leftNode, rightNode):
    rootNode.left = leftNode
    rootNode.right = rightNode


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


def Test(testName, methodType, root, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0
    try:
        if methodType == 1 or methodType == '1':
            start = timeit.default_timer()
            test.Mirror1(root)
            result = BFS(root)
            end = timeit.default_timer()
        elif methodType == 2 or methodType == '2':
            start = timeit.default_timer()
            test.Mirror2(root)
            result = BFS(root)
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


# # 测试完全二叉树：除了叶子节点，其他节点都有两个子节点
# #            1
# #        2      3
# #       4 5    6  7
# treeNode1 = TreeNode(1)
# treeNode2 = TreeNode(2)
# treeNode3 = TreeNode(3)
# treeNode4 = TreeNode(4)
# treeNode5 = TreeNode(5)
# treeNode6 = TreeNode(6)
# treeNode7 = TreeNode(7)
# ConnectTreeNodes(treeNode1, treeNode2, treeNode3)
# ConnectTreeNodes(treeNode2, treeNode4, treeNode5)
# ConnectTreeNodes(treeNode3, treeNode6, treeNode7)
# Test('Test1_1', 1, treeNode1, [1, 3, 2, 7, 6, 5, 4])
#
# # 测试二叉树：出叶子结点之外，左右的结点都有且只有一个左子结点
# #            1
# #          2
#
# #        3
# treeNode1 = TreeNode(1)
# treeNode2 = TreeNode(2)
# treeNode3 = TreeNode(3)
# ConnectTreeNodes(treeNode1, treeNode2, None)
# ConnectTreeNodes(treeNode2, treeNode3, None)
# Test('Test1_2', 1, treeNode1, [1, 2, 3])
#
# # 测试二叉树：出叶子结点之外，左右的结点都有且只有一个右子结点
# #            1
# #             2
# #              3
# treeNode1 = TreeNode(1)
# treeNode2 = TreeNode(2)
# treeNode3 = TreeNode(3)
# ConnectTreeNodes(treeNode1, None, treeNode2)
# ConnectTreeNodes(treeNode2, None, treeNode3)
# Test('Test1_3', 1, treeNode1, [1, 2, 3])
#
# # 测试空二叉树：根结点为空指针
# Test('Test1_4', 1, None, None)
#
# # 测试只有一个结点的二叉树
# treeNode1 = TreeNode(1)
# Test('Test1_5', 1, treeNode1, [1])


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
Test('Test2_1', 2, treeNode1, [1, 3, 2, 7, 6, 5, 4])

# 测试二叉树：出叶子结点之外，左右的结点都有且只有一个左子结点
#            1
#          2

#        3
treeNode1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)
ConnectTreeNodes(treeNode1, treeNode2, None)
ConnectTreeNodes(treeNode2, treeNode3, None)
Test('Test2_2', 2, treeNode1, [1, 2, 3])

# 测试二叉树：出叶子结点之外，左右的结点都有且只有一个右子结点
#            1
#             2
#              3
treeNode1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)
ConnectTreeNodes(treeNode1, None, treeNode2)
ConnectTreeNodes(treeNode2, None, treeNode3)
Test('Test2_3', 2, treeNode1, [1, 2, 3])

# 测试空二叉树：根结点为空指针
Test('Test2_4', 2, None, None)

# 测试只有一个结点的二叉树
treeNode1 = TreeNode(1)
Test('Test2_5', 2, treeNode1, [1])


print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
