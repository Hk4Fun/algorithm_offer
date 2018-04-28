__author__ = 'Hk4Fun'
__date__ = '2018/4/28 22:14'
'''题目描述：
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
'''
'''主要思路：
注意这里不再是完全二叉树了，而是一棵普通的二叉树

思路1：时间O（n），空间O（n）
leetcode/tree/medium/116. Populating Next Right Pointers in Each Node.py 的思路1
代码完全不变

思路2：时间O（n），空间O（1）
leetcode/tree/medium/116. Populating Next Right Pointers in Each Node.py 的思路3
把提前返回去掉即可
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect1(self, root):
        if not root: return
        level = [root]
        while level:
            next_level = []
            pre = level[0]
            for cur in level:
                if cur is not level[0]:
                    pre.next = cur
                    pre = cur
                if cur.left: next_level.append(cur.left)
                if cur.right: next_level.append(cur.right)
            level = next_level

    def connect2(self, root):
        while root:
            cur = dummy = TreeLinkNode(0)  # 下一层的虚拟头结点
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = dummy.next


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        node1 = TreeLinkNode(1)
        node2 = TreeLinkNode(2)
        node3 = TreeLinkNode(3)
        node4 = TreeLinkNode(4)
        node5 = TreeLinkNode(5)
        node7 = TreeLinkNode(7)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.right = node7
        testArgs.append([node1, None])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
