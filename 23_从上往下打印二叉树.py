__author__ = 'Hk4Fun'
__date__ = '2018/2/1 1:16'

'''题目描述：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
'''主要思路：
相当于宽度优先搜索（BFS），用队列来实现：
每次从头部取出一个结点时，如果该结点有子结点，
就把该结点的子结点从左到右依次放入队列末尾，
重复前面的步骤，直到队列为空
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []

        result = []
        queue = [root]
        while len(queue):
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def ConnectTreeNodes(rootNode, leftNode, rightNode):
    rootNode.left = leftNode
    rootNode.right = rightNode


def Test(testName, root, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.PrintFromTopToBottom(root)
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


#       10
#    /      \
#   6        14
#  /\        /\
# 4  8     12  16
treeNode10 = TreeNode(10)
treeNode6 = TreeNode(6)
treeNode14 = TreeNode(14)
treeNode4 = TreeNode(4)
treeNode8 = TreeNode(8)
treeNode12 = TreeNode(12)
treeNode16 = TreeNode(16)
ConnectTreeNodes(treeNode10, treeNode6, treeNode14)
ConnectTreeNodes(treeNode6, treeNode4, treeNode8)
ConnectTreeNodes(treeNode14, treeNode12, treeNode16)
Test("Test1", treeNode10, [10, 6, 14, 4, 8, 12, 16])

#         5
#        /
#       4
#      /
#     3
treeNode5 = TreeNode(5)
treeNode4 = TreeNode(4)
treeNode3 = TreeNode(3)
ConnectTreeNodes(treeNode5, treeNode4, None)
ConnectTreeNodes(treeNode4, treeNode3, None)
Test("Test2", treeNode5, [5, 4, 3])

# 1
#  \
#   2
#    \
#     3
treeNode1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)
ConnectTreeNodes(treeNode1, None, treeNode2)
ConnectTreeNodes(treeNode2, None, treeNode3)
Test("Test3", treeNode1, [1, 2, 3])

# 树中只有1个结点
treeNode1 = TreeNode(1)
Test("Test4", treeNode1, [1])

# 树中没有结点
Test("Test5", None, [])


print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
