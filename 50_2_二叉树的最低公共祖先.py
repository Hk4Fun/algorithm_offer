__author__ = 'Hk4Fun'
__date__ = '2018/2/19 18:44'

'''题目描述：
找出二叉树中两个结点的最低公共祖先（没有指向父节点的指针）
'''
'''主要思路：
如果有指向父节点的指针那么从这两个结点开始到根节点分别形成两个链表，
问题就相当于求两个链表的第一个公共结点了，即转化为37题
但如果不存在，就只能自上而下。由上面的分析我们发现此题和37题是很相似的，
于是我们借鉴37题的思路2完成：前序遍历记录根节点到两个结点的路径到两个数组中（成倒‘Y’字型）
然后从头遍历两个数组，最后一个公共结点就是两个结点的最低公共祖先
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findParent(self, root, pNode1, pNode2):
        def find_path(path, root, pNode):  # 前序遍历记录根节点到其他结点的路径
            path.append(root)
            if root == pNode:
                return True
            found = False
            if root.left:
                found = find_path(path, root.left, pNode)
            if not found and root.right:
                found = find_path(path, root.right, pNode)
            if not found:
                path.pop()
            return found

        if not root or not pNode1 or not pNode2:
            return
        path1 = []
        find_path(path1, root, pNode1)
        path2 = []
        find_path(path2, root, pNode2)
        last = None
        while path1 and path2:
            if path1[0] == path2[0]:
                last = path1[0]
            path1.pop(0)
            path2.pop(0)
        return last


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


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
