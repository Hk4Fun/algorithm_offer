__author__ = 'Hk4Fun'
__date__ = '2018/3/10 14:31'

'''题目描述：
找出满二叉树中两个结点的最低公共祖先（没有指向父节点的指针）
'''
'''主要思路：
层序遍历满二叉树，给每个结点编号，从1开始。
根据满二叉树的特点，假设子树的结点编号为k，则其左孩子编号为2k，
右孩子编号为2k+1。用二进制表示就是k左移以及k左移+1。
也就是在父结点的二进制表示的后面添1或添0。
所以两个结点的最低公共祖先就是它们编号二进制表示的最长前缀所对应编号的结点
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findParent(self, root, pNode1, pNode2):
        if not root or not pNode1 or not pNode2:
            return
        # 层序遍历给两个结点编号
        queue = [(root, 1)]
        num = 1
        while queue:
            cur = queue.pop(0)
            if cur[0] is pNode1:
                num1 = cur[1]
            if cur[0] is pNode2:  # 考虑到两个结点可能为同一结点，不能用elif
                num2 = cur[1]
            if cur[0].left:
                num += 1
                queue.append((cur[0].left, num))
            if cur[0].right:
                num += 1
                queue.append((cur[0].right, num))
        # 寻找最长前缀，为父节点编号
        while num1 != num2:
            if num1 > num2:
                num1 >>= 1
            else:
                num2 >>= 1
        parentNum = num1
        # 层序遍历，根据编号找到父结点返回
        queue = [root]
        while queue:
            cur = queue.pop(0)
            parentNum -= 1
            if parentNum == 0:
                return cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def ConnectTreeNodes(rootNode, leftNode, rightNode):
            rootNode.left = leftNode
            rootNode.right = rightNode

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

        testArgs.append([treeNode1, treeNode4, treeNode5, treeNode2])
        testArgs.append([treeNode1, treeNode4, treeNode7, treeNode1])
        testArgs.append([treeNode1, treeNode4, treeNode3, treeNode1])
        testArgs.append([treeNode1, treeNode4, treeNode2, treeNode2])
        testArgs.append([treeNode1, treeNode4, treeNode1, treeNode1])
        testArgs.append([treeNode1, treeNode4, treeNode4, treeNode4])
        testArgs.append([treeNode1, treeNode1, treeNode1, treeNode1])
        testArgs.append([treeNode4, treeNode4, treeNode4, treeNode4])
        testArgs.append([None, None, None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result

    def checked(self, result, expected, *func_arg):
        return result.val == expected.val if result else result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
