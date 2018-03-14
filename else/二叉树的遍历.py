__author__ = 'Hk4Fun'
__date__ = '2018/3/14 21:18'
'''
二叉树的遍历主要有前序、中序、后序和层序遍历，算法上有递归版本和非递归版本（层序一般只用非递归）
但无论递归还是非递归，其空间复杂度都为O（n），只不过前序、中序和后序的递归用的是系统栈，而剩下的
非递归是自己维护一个栈或者队列。

前序、中序、后序的递归实现已经模版化了，三个位置分别对应
进入左孩子前、从左孩子回来并准备进入右孩子、从右孩子回来，
所以实际上递归实现时每个结点被访问了三次；
至于层序遍历一般只用非递归，队列实现。

前序遍历的非递归需要自己维护一个栈来模拟系统栈：
1、将根结点入栈；
2、从栈顶弹出一个结点并访问之；
3、把该结点的右孩子入栈（如果有的话）；
4、把该结点的左孩子入栈（如果有的话），然后转入步骤2。
注意先入右孩子再入左孩子，这样访问时才能先访问左孩子再访问右孩子

中序遍历的非递归也是自己维护一个栈来模拟系统栈：
1、cur指向根结点；
2、cur一路往左遍历左孩子，依次入栈，一直来到最左结点停止；
3、从栈顶弹出一个结点并访问之；
4、cur来到弹出结点的右结点，转入步骤2。

后序遍历的非递归有两种思路：
思路1：两个栈实现。
借助前序遍历的非递归实现，在访问根结点时不要直接访问，应等左右结点访问了才轮到它，
所以应把它压入另外一个栈；而在压入第一个栈时先压左结点再压右结点，
这样在它们被当作根结点时就会被弹出并压入第二个栈，于是右结点在下左结点在上；
最后从依次弹出第二个栈的结点访问之顺序就是（左结点，右结点，根结点）
1、将根结点压入stack1；
2、弹出stack1的栈顶结点，并把该结点压入stack2；
3、将当前结点的左孩子和右孩子先后分别压入stack1，转入步骤2；
4、当所有元素都压入stack2后，依次弹出stack2的栈顶结点并访问之。
思路2：一个栈实现。
要保证根结点在左孩子和右孩子访问之后才能访问，因此对于任一结点P，先将其入栈。
如果P不存在左孩子和右孩子，则可以直接访问它；
或者P存在左孩子或者右孩子，但是其左孩子和右孩子都已被访问过了，则同样可以直接访问该结点。
若非上述两种情况，则将P的右孩子和左孩子依次入栈，
这样就保证了每次取栈顶元素的时候，左孩子在右孩子前面被访问，
且左孩子和右孩子都在根结点前面被访问。
现在的问题是如何知道根结点的左孩子和右孩子是否都被访问过？
可以设置一个pre来记录上次访问过的结点，如果某个结点被访问了就把pre指向它，
这样来到其根结点时看一下pre是否指向根结点的左孩子或右孩子，
就知道根结点的左孩子和右孩子是否都已被访问过了。
这里有个细节：pre只是记录最后一个访问的结点，根结点怎么就能判断其左右孩子是否都被访问了？
注意出栈的顺序，左右孩子一定在根结点前面出栈，当只有左孩子时，pre指向左孩子；
只有右孩子时pre指向右孩子；既有左孩子又有右孩子时pre指向右孩子。
'''


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pre_order_recursion(self, root):
        def pre_order(root):
            if not root:
                return
            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        res = []
        pre_order(root)
        return res

    def pre_order_iteration(self, root):
        if not root:
            return
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def in_order_recursion(self, root):
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)

        res = []
        in_order(root)
        return res

    def in_order_iteration(self, root):
        if not root:
            return
        stack, res = [], []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def post_order_recursion(self, root):
        def post_order(root):
            if not root:
                return
            post_order(root.left)
            post_order(root.right)
            res.append(root.val)

        res = []
        post_order(root)
        return res

    def post_order_iteration1(self, root):
        if not root:
            return
        stack1, stack2, res = [root], [], []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        while stack2:
            res.append(stack2.pop().val)
        return res

    def post_order_iteration2(self, root):
        if not root:
            return
        stack, res = [root], []
        pre = None
        while stack:
            cur = stack[-1] # 注意这里不要直接弹出
            if (not cur.left and not cur.right) or (not pre and (pre == cur.left or pre == cur.right)):
                res.append(cur.val)
                stack.pop()
                pre = cur
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return res


    def seq_order_iteration(self, root):
        queue, res = [root], []
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def ConnectTreeNodes(rootNode, leftNode, rightNode):
            rootNode.left = leftNode
            rootNode.right = rightNode

        #      8
        #  6      10
        # 5 7    9  11
        node8 = TreeNode(8)
        node6 = TreeNode(6)
        node10 = TreeNode(10)
        node5 = TreeNode(5)
        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node11 = TreeNode(11)
        ConnectTreeNodes(node8, node6, node10)
        ConnectTreeNodes(node6, node5, node7)
        ConnectTreeNodes(node10, node9, node11)
        # testArgs.append([node8, [8, 6, 5, 7, 10, 9, 11]])  # 前序
        # testArgs.append([node8, [5, 6, 7, 8, 9, 10, 11]])  # 中序
        # testArgs.append([node8, [5, 7, 6, 9, 11, 10, 8]])  # 后序
        # testArgs.append([node8, [8, 6, 10, 5, 7, 9, 11]])  # 层序

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
