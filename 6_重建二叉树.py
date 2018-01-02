__author__ = 'Hk4Fun'
__date__ = '2018/1/1 22:45'

'''题目描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回其根节点。
'''
'''主要思路：
前序的第一个元素是根结点的值，在中序中找到该值，
中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre_order, in_order):
        if not pre_order and not in_order:
            return None
        if set(pre_order) != set(in_order):  # 鲁棒性，错误序列
            return None
        index = in_order.index(pre_order[0])  # 先序第一个为根节点
        root = TreeNode(pre_order[0])  # 在中序中找到根节点位置
        root.left = self.reConstructBinaryTree(pre_order[1:index + 1], in_order[:index])  # 构建左子树
        root.right = self.reConstructBinaryTree(pre_order[index + 1:], in_order[index + 1:])  # 构建右子树
        return root


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


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


def Test(testName, pre_order, in_order, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.reConstructBinaryTree(pre_order, in_order)
        end = timeit.default_timer()
        result = BFS(result)
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


# 普通二叉树
#              1
#           /     \
#          2       3
#         /       / \
#        4       5   6
#         \         /
#          7       8
Test('Test1', [1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6], [1, 2, 3, 4, 5, 6, 7, 8])

# 所有结点都没有右子结点
#            1
#           /
#          2
#         /
#        3
#       /
#      4
#     /
#    5
Test('Test2', [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5])

# 所有结点都没有左子结点
#            1
#             \
#              2
#               \
#                3
#                 \
#                  4
#                   \
#                    5
Test('Test3', [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

# 完全二叉树
#              1
#           /     \
#          2       3
#         / \     / \
#        4   5   6   7
Test('Test4', [1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7])

Test('Test5', [1], [1], [1])  # 树中只有一个结点
Test('Test6', [], [], None)  # 传入空树
Test('Test7', [1, 2, 4, 5, 3, 6, 7], [4, 2, 8, 1, 6, 3, 7], None)  # 传入的两个序列不匹配

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
