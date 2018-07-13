__author__ = 'Hk4Fun'
__date__ = '2018/2/5 15:03'

'''题目描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
'''主要思路：
二叉搜索树与双向链表的每个结点均含有两个指针，数据结构类似，可以实现相互转换
转换过程中，原先指向左子结点的指针调整为链表中指向前一结点的指针，
原先指向右子结点的指针调整为链表中指向后一结点的指针：
      10
    /    \
   6     14        =====>     None<-4<->6<->8<->10<->12<->14<->16->None
  /\     /\
 4  8  12  16
思路1：中序遍历，同时设置一个指针指向当前双向链表的最后一个结点，
       每个被遍历到的结点都与当前双向链表的最后一个结点互相连接，
       同时更新该指针为当前被遍历到的结点
思路2：处理左子树，连接根与左子树最大结点（左子树最右边结点），
       处理右子树，连接根与右子树最小结点（右子树最左边结点）
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert1(self, pRootOfTree):
        def ConvertNode(pNode):
            nonlocal pLastNodeInList  # 指向当前双向链表的最后一个结点
            if not pNode: return
            pCurrent = pNode
            # 转换左子树
            ConvertNode(pCurrent.left)
            # 与当前双向链表的最后一个结点互相连接
            pCurrent.left = pLastNodeInList
            pLastNodeInList.right = pCurrent
            pLastNodeInList = pCurrent  # 更新当前双向链表的最后一个结点
            # 转换右子树
            ConvertNode(pCurrent.right)

        if not pRootOfTree: return
        dummy = pLastNodeInList = TreeNode(0)
        ConvertNode(pRootOfTree)
        head = dummy.right # 伪结点的右边是真正的头结点
        head.left = None # 去掉伪结点
        return head

    def Convert2(self, pRootOfTree):
        def ConvertNode(pRootOfTree):
            if not pRootOfTree:
                return

            # 处理左子树
            left = ConvertNode(pRootOfTree.left)
            # 连接根与左子树最大结点（左子树最右边结点）
            if left:
                while left.right:  # 移到左子树最右边结点
                    left = left.right
                pRootOfTree.left, left.right = left, pRootOfTree

            # 处理右子树
            right = ConvertNode(pRootOfTree.right)
            # 连接根与右子树最小结点（右子树最左边结点）
            if right:
                while right.left:  # 移到右子树最左边结点
                    right = right.left
                pRootOfTree.right, right.left = right, pRootOfTree
            return pRootOfTree

        if not pRootOfTree:
            return
        ConvertNode(pRootOfTree)
        while pRootOfTree.left:  # 移到头结点返回
            pRootOfTree = pRootOfTree.left
        return pRootOfTree


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
        testArgs.append([treeNode10, [[4, 6, 8, 10, 12, 14, 16], [16, 14, 12, 10, 8, 6, 4]]])

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
        testArgs.append([treeNode5, [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]])

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
        testArgs.append([treeNode1, [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]])

        # 树中只有1个结点
        treeNode1 = TreeNode(1)
        testArgs.append([treeNode1, [[1], [1]]])

        # 树中没有结点
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        def Convert(pHead):  # 从左和从右打印双向链表的结点值
            if not pHead:
                return
            result = []
            pNode = pHead
            left = [pHead.val]
            while pNode.right:
                pNode = pNode.right
                left.append(pNode.val)
            result.append(left)
            right = [pNode.val]
            while pNode.left:
                pNode = pNode.left
                right.append(pNode.val)
            result.append(right)
            return result

        return Convert(result)


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
