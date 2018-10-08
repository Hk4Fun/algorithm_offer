__author__ = 'Hk4Fun'
__date__ = '2018/2/1 18:19'

'''题目描述：
输入某二叉树的中序遍历和后序遍历的结果，请重建出该二叉树并返回其根节点。
假设输入的中序遍历和后序遍历的结果中都不含重复的数字。
'''
'''主要思路：
后序的最后一个元素是根结点的值，在中序中找到该值，
中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree1(self, post_order, in_order):
        if not post_order and not in_order: return None
        index = in_order.index(post_order[-1])  # 后序的最后一个根节点，在中序中找到该根节点的位置，
        root = TreeNode(post_order[-1])  # 创建根节点
        root.left = self.reConstructBinaryTree1(post_order[:index], in_order[:index])  # 构建左子树
        root.right = self.reConstructBinaryTree1(post_order[index:-1], in_order[index + 1:])  # 构建右子树
        return root

    def reConstructBinaryTree2(self, post_order, in_order):
        def build(postLeft, postRight, inLeft, inRight):
            if postLeft > postRight or inLeft > inRight: return None
            idx = inLeft
            while idx <= inRight:
                if in_order[idx] == post_order[postRight]: break
                idx += 1
            root = TreeNode(post_order[postRight])
            root.left = build(postLeft, postLeft + idx - inLeft - 1, inLeft, idx - 1)
            root.right = build(postLeft + idx - inLeft, postRight - 1, idx + 1, inRight)
            return root

        return build(0, len(post_order) - 1, 0, len(in_order) - 1)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []
        # 普通二叉树
        #              1
        #           /     \
        #          2       3
        #         /       / \
        #        4       5   6
        #         \         /
        #          7       8
        testArgs.append([[7, 4, 2, 5, 8, 6, 3, 1], [4, 7, 2, 1, 5, 3, 8, 6], [1, 2, 3, 4, 5, 6, 7, 8]])

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
        testArgs.append([[5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]])

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
        testArgs.append([[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

        # 完全二叉树
        #              1
        #           /     \
        #          2       3
        #         / \     / \
        #        4   5   6   7
        testArgs.append([[4, 5, 2, 6, 7, 3, 1], [4, 2, 5, 1, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7]])

        testArgs.append([[1], [1], [1]])  # 树中只有一个结点
        testArgs.append([[], [], None])  # 传入空树

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
