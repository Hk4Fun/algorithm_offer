__author__ = 'Hk4Fun'
__date__ = '2018/2/19 18:44'

'''题目描述：
找出二叉树中两个结点的最低公共祖先（没有指向父节点的指针）
'''
'''主要思路：
思路1：
如果有指向父节点的指针那么从这两个结点开始到根节点分别形成两个链表，
问题就相当于求两个链表的第一个公共结点了，即转化为37题
但如果不存在，就只能自上而下。由上面的分析我们发现此题和37题是很相似的，
于是我们借鉴37题的思路2完成：前序遍历记录根节点到两个结点的路径到两个数组中（成倒‘Y’字型）
然后从头遍历两个数组，最后一个公共结点就是两个结点的最低公共祖先

思路2：
结束递归：
如果遇到了目标节点就返回那个目标节点，表示找到了该结点；
如果是None就返回None，表示没有找到。
继续递归：
既不是None也不是目标节点，说明要接着递归往下左右子树遍历，
收集下面传上来的有关子树中出现目标节点的信息
处理递归返回的信息：
如果左子树、右子树都有找到，说明自己就是最小公共祖先了，返回本身；
只有一边找到，则说明自己不是最小公共祖先，而是在最小公共祖先的上面，
且间接说明这个传上来的结点就是最小公共祖先，把这个传上来的结点继续往上传；
两边都没有找到则直接返回None，表示没有找到。

50_1~3小结:
前两题都是根据二叉树本身的性质（搜索二叉树的有序性以及满二叉树的编号规律）进行寻找，
而这一题的解法是通用的，且这里的思路2的递归框架更是具有通用性，
它在39_2的思路2中其实已经体现出来了：后序遍历树，使树自下而上传递信息，
根据这些信息构造相同结构的新的信息往上传，类似与承上启下，这里是承下启上
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findParent1(self, root, pNode1, pNode2):
        def find_path(path, root, pNode):  # 前序遍历记录根节点到其他结点的路径
            path.append(root)  # 先把当前结点加入路径
            if root == pNode:  # 来到该结点，说明找到课路径
                return True
            if root.left and find_path(path, root.left, pNode):  # 从左边开始找
                return True
            if root.right and find_path(path, root.right, pNode):  # 左边找不到就从右边找
                return True
            path.pop()  # 左右都没找到就把该结点从当前路径中删了，返回False
            return False

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

    def findParent2(self, root, pNode1, pNode2):
        if not root or root == pNode1 or root == pNode2: return root
        left = self.findParent2(root.left, pNode1, pNode2)
        right = self.findParent2(root.right, pNode1, pNode2)
        return root if left and right else left or right


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

        self.debug = False
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
