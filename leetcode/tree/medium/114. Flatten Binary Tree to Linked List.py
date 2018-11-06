__author__ = 'Hk4Fun'
__date__ = '2018/4/27 21:44'
'''题目描述：
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
'''主要思路：
时间O（n），空间O（n）
思路1：前序遍历，设置一个pre保存前一个结点，
      由于进入左子树会改变当前结点右孩子的连接，
      所以在进入左子树前记得先保存当前结点的右孩子
      
思路2：思路1之所以要先保存当前结点的右孩子是因为前序遍历的特点，cur->left->right
      那么可以反过来，用一种类似后序遍历的遍历方式：right->left->cur
      这样就可以不用先保存当前结点的右孩子了
      这是一个自底向上的构建过程
      
思路3：仿照morris遍历的思路
      
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    def flatten1(self, root):
        def build(root):
            if not root: return
            self.pre.left, self.pre.right = None, root
            self.pre = root
            right = root.right  # 进入左子树前先保存右孩子
            build(root.left)
            build(right)

        self.pre = TreeNode(0) # 注意这里的pre不能为None，因为这里自顶向下构建
        build(root)

    def flatten2(self, root):
        def build(root):
            if not root: return
            build(root.right)
            build(root.left)
            root.right, root.left = self.prev, None
            self.prev = root

        self.prev = None  # 注意这里的pre必须为None，因为这里自底向上构建
        build(root)

    def flatten3(self, root):
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right: pre = pre.right # 来到左子树的最右结点
                pre.right = cur.right # 把当前结点的右子树连接到最右结点的右指针
                cur.left, cur.right = None, cur.left # 把当前结点的左子树连接到右指针
            cur = cur.right # 继续访问右子树


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

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

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
