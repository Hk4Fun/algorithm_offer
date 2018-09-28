__author__ = 'Hk4Fun'
__date__ = '2018/3/14 21:18'


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    '''
    前序、中序、后序的递归实现已经模版化了，三个位置分别对应
    进入左孩子前、从左孩子回来并准备进入右孩子、从右孩子回来，
    即三种状态：访问了0个孩子、访问了1个孩子（左孩子）、访问了3个孩子（左右孩子）
    所以实际上递归时每个结点被访问了三次
    '''

    def traverse_recursion(self, root):
        def pre_order(root):
            if not root:
                return
            res.append(root.val)  # 前序visit
            pre_order(root.left)
            # res.append(root.val) # 中序visit
            pre_order(root.right)
            # res.append(root.val) # 后序visit

        if not root:
            return
        res = []
        pre_order(root)
        return res

    '''
    至于层序遍历一般只用非递归，队列实现
    '''
    # def seq_order_iteration(self, root):
    #     res, level = [], [root]
    #     while level:
    #         next_level = []
    #         res.append([])
    #         for cur in level:
    #             res[-1].append(cur.val)
    #             if cur.left:
    #                 next_level.append(cur.left)
    #             if cur.right:
    #                 next_level.append(cur.right)
    #         level = next_level
    #     return res

    '''
    前序遍历的非递归需要自己维护一个栈来模拟系统栈：
    1、将根结点入栈；
    2、从栈顶弹出一个结点并访问之；
    3、把该结点的右孩子入栈（如果有的话）；
    4、把该结点的左孩子入栈（如果有的话），然后转入步骤2。
    注意先入右孩子再入左孩子，这样访问时才能先访问左孩子再访问右孩子
    '''

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

    '''
    中序遍历的非递归也是自己维护一个栈来模拟系统栈：
    1、cur指向根结点；
    2、cur一路往左遍历左孩子，依次入栈，一直来到最左结点停止；
    3、从栈顶弹出一个结点并访问之；
    4、cur来到弹出结点的右结点，转入步骤2。
    '''
    # def in_order_iteration(self, root):
    #     if not root:
    #         return
    #     stack, res = [], []
    #     cur = root
    #     while stack or cur:
    #         while cur:  # cur一路往左遍历左孩子，依次入栈，一直来到最左结点停止
    #             stack.append(cur)
    #             cur = cur.left
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         cur = cur.right
    #     return res

    '''
    到这里，会觉得前序和中序的非递归在代码上没有像递归那样统一且模版化，
    但实际上仔细观察中序的非递归会发现在cur一路往左遍历左孩子时是入栈操作，
    是第一次来到每个结点的时机，完全可以在入栈前访问该结点，这样就可以实现前序，
    所以前序中序的代码可以统一模版化
    '''

    def pre_in_order_iteration1(self, root):
        if not root:
            return
        stack, res = [], []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)  # 前序visit，入栈前访问
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # res.append(cur.val) # 中序visit，出栈后访问
            cur = cur.right
        return res

    '''
    上面代码中入栈时是前序遍历的时机，而出栈时是中序遍历的时机，每个结点都经历一次入栈和出栈，
    所以每个结点实际上被访问了2次。其实入栈和出栈是对称操作，那么在代码的实现上也可以是‘对称’的:
    如果当前结点不为空，那么就进栈并来到左结点，否则出栈并来到右结点
    进栈前是前序遍历的访问时机，出栈后是中序遍历的访问时机
    '''

    def pre_in_order_iteration2(self, root):
        if not root:
            return
        stack, res = [], []
        cur = root
        while stack or cur: # 注意这里的循环条件
            if cur:
                res.append(cur.val)  # 前序visit，入栈前访问
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                # res.append(cur.val) # 中序visit，出栈后访问
                cur = cur.right
        return res

    '''
    后序遍历的非递归有两种思路：
    思路1：两个栈实现。
    借助前序遍历的非递归实现，在访问根结点时不要直接访问，应等左右结点访问了才轮到它，
    所以应把它压入另外一个栈（第二个栈），然后把的左右结点分别压入第一个栈；
    而在压入第一个栈时先压左结点再压右结点，这样在它们被当作根结点时就会被弹出并压入第二个栈，
    于是右结点在下左结点在上，最后依次弹出第二个栈的结点访问之顺序就是（左结点，右结点，根结点）
    1、将根结点压入stack1；
    2、弹出stack1的栈顶结点，并把该结点压入stack2；
    3、将当前结点的左孩子和右孩子先后分别压入stack1，转入步骤2；
    4、当所有元素都压入stack2后，依次弹出stack2的栈顶结点并访问之。
    '''
    # def post_order_iteration1(self, root):
    #     if not root:
    #         return
    #     stack1, stack2, res = [root], [], []
    #     while stack1:
    #         cur = stack1.pop()
    #         stack2.append(cur)  # cur不直接访问而是先压入另一个栈
    #         if cur.left:
    #             stack1.append(cur.left)
    #         if cur.right:
    #             stack1.append(cur.right)
    #     while stack2:
    #         res.append(stack2.pop().val)
    #     return res

    '''
    思路2：一个栈实现。
    要保证根结点在左孩子和右孩子访问之后才能访问，因此对于任一栈顶结点cur，
    如果cur不存在左孩子和右孩子，则可以弹出直接访问之；
    或者cur存在左孩子或者右孩子，但是其左孩子和右孩子都已被访问过了，则同样可以直接访问该结点。
    若非上述两种情况，则将cur的右孩子和左孩子依次入栈，
    这样就保证了每次取栈顶元素的时候，左孩子在右孩子前面被访问，
    且左孩子和右孩子都在根结点前面被访问。
    现在的问题是如何知道根结点的左孩子和右孩子是否都被访问过？
    可以设置一个pre来记录上次访问过的结点，如果某个结点被访问了就把pre指向它，
    这样来到其根结点时看一下pre是否指向根结点的左孩子或右孩子，
    就知道根结点的左孩子和右孩子是否都已被访问过了。
    这里有个细节：pre只是记录最后一个访问的结点，根结点怎么就能判断其左右孩子是否都被访问了？
    注意出栈的顺序，第一次访问根结点时pre是不可能指向根结点的左右孩子的，因为左右孩子根本还没入栈。
    而如果是第二次访问该结点，则pre一定会指向根结点的孩子，因为左右孩子在根结点前面出栈被访问了。
    '''
    # def post_order_iteration2(self, root):
    #     if not root:
    #         return
    #     stack, res = [root], []
    #     pre = None
    #     while stack:
    #         cur = stack[-1]  # 注意这里不要直接弹出
    #         if (not cur.left and not cur.right) or (pre and (pre == cur.left or pre == cur.right)):
    #             # 如果当前结点没有孩子结点或者孩子节点都已被访问过了
    #             res.append(cur.val)
    #             stack.pop()
    #             pre = cur
    #         data_structures:  # 否则说明该结点有左孩子或右孩子且都没被访问过，直接入栈
    #             if cur.right:
    #                 stack.append(cur.right)
    #             if cur.left:
    #                 stack.append(cur.left)
    #     return res

    '''
    到这里，既然前序中序的非递归已经统一模板了，那么后序是否也可以统一进前面的pre_in_order_iteration1
    或pre_in_order_iteration2呢？不行。因为栈只有两种操作，入栈时用来前序，出栈时用来中序，
    没有其他操作所对应的时机安排给后序了。上面两个思路要么用两个栈，要么用一个栈加一个标记pre。
    所以有必要重新安排一下入栈出栈时机了。既然每个结点只有两次被访问，那么就让结点像递归那样有三次被访问，
    这样就多出一个时机安排给后序了。
    1、进栈为前序时机，给结点打上标记0，表示当前还没有访问任何孩子，是第一次来，然后cur移到左孩子；
    2、第二次来到时不出栈，为中序时机，给结点打上标记1，表示已经访问过一个结点，是第二次来，然后cur移到右孩子；
    3、这样在第三次来到这个结点时查看标记是否为1就知道是否第三次来到该结点，为后序时机，然后出栈，cur指向None。
    '''

    def traverse_iteration1(self, root):
        if not root:
            return
        stack, res = [], []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)  # 前序visit，入栈前访问
                stack.append([cur, 0])
                cur = cur.left
            else:
                cur = stack[-1][0]  # 注意这里不出栈
                if stack[-1][1] == 0:  # 为0说明是第二次来
                    # res.append(cur.val)  # 中序visit，不出栈直接访问
                    stack[-1][1] = 1  # 表示第二次来
                    cur = cur.right
                else:  # 为1说明是第三次来
                    # res.append(cur.val)  # 后序visit，出栈时访问
                    stack.pop()
                    cur = None  # 注意这里cur指向空
        return res

    '''
    上面的模板虽然统一了三种遍历的非递归，但是层层嵌套，逻辑复杂，不好理解。
    且还给每个结点打上标签，实际上和用两个栈的空间是差不多的。那有没有像递归那样简洁的模板呢？
    利用有重合元素的局部有序一定能导致整体有序这个思想就能简化该模板：https://www.jianshu.com/p/49c8cfd07410
    这里的局部有序对于前序来讲是（根，左，右），中序是（左，根，右），后序是（左，右，根），于是入栈顺序就是
    前序（右，左，根），中序（右，根，左），后序（根，右，左）
    将栈顶元素取出，然后以此元素为根结点的局部有序入栈，但若此前已通过该结点将其局部入栈，则直接出栈输出即可。
    '''

    def traverse_iteration2(self, root):
        if not root:
            return
        stack, res = [(root, False)], []
        while stack:
            cur, visited = stack.pop()
            if not cur:
                continue
            if visited:
                res.append(cur.val)
            else:
                # stack.append((cur, True))  # 后序
                stack.append((cur.right, False))
                # stack.append((cur, True))  # 中序
                stack.append((cur.left, False))
                stack.append((cur, True))  # 前序
        return res

    '''
    在模板1中可以看到二叉树的遍历无非就是在三种状态之间转换，
    而对应的序列无非就是来到这三种状态时进行输出，所以可以自动机的思维来分析：
    https://www.jianshu.com/p/8359c1369066
    '''

    def traverse_iteration3(self, root):
        NONE = 0  # 尚未处理左右孩子
        LEFT_DONE = 1  # 处理完左孩子
        LEFT_RIGHT_DONE = 2  # 左右孩子都已经处理完
        when = NONE  # 前序
        # when = LEFT_DONE # 中序
        # when = LEFT_RIGHT_DONE # 后序
        if not root:
            return
        stack, res = [[root, NONE]], []
        while stack:
            cur, state = stack[-1]
            if state == when:  # 在对应时机输出
                res.append(cur.val)
            if state == NONE:  # NONE --> LEFT_DONE
                stack[-1][1] = LEFT_DONE
                if cur.left:
                    stack.append([cur.left, NONE])
            elif state == LEFT_DONE:  # LEFT_DONE --> LEFT_RIGHT_DONE
                stack[-1][1] = LEFT_RIGHT_DONE
                if cur.right:
                    stack.append([cur.right, NONE])
            elif state == LEFT_RIGHT_DONE:  # LEFT_RIGHT_DONE --> 出栈
                stack.pop()
        return res

    '''
    无论递归还是非递归，其空间复杂度都为O(n)，只不过前序、中序和后序的递归用的是系统栈，而剩下的
    非递归是自己维护栈或者队列。那有没有一种二叉树遍历算法的空间复杂度为O(1)呢？Morris遍历！
    Morris遍历算法最神奇的地方就在于只需要常数的空间即可在O(n)时间内完成二叉树的遍历。
    O(1)空间进行遍历的困难之处在于遍历子结点的时候如何重新返回其父节点。
    因此在Morris遍历算法中，通过修改叶子结点的左右空指针来指向其后继结点来实现。
    其思路来源于线索二叉树的遍历，只不过线索二叉树在遍历前需要将整棵二叉树线索化，且修改了空指针。
    而Morris遍历算法取其精华去其糟粕，一边线索化一边遍历，且只线索化后继指针，
    同时将使用过的线索化指针改回空指针，从而使整棵二叉树在遍历完成后还原。
    Morris遍历算法：
    1、当cur来到一个结点P的时候看它有没有左子树，没有的话无论前序中序都输出该结点，cur向右子树移动；
    2、有的话就找到左子树的最右结点，
       如果这个最右结点的右指针为空，说明cur是第一次来到P，则让该右指针指向P，然后cur向左子树移动；
    3、如果这个最右结点已经指向P，说明cur是第二次来到P，则让该右结点指向None还原，然后cur向右子树移动。
    在该算法的步骤2中让最右结点指向P，其实就是在线索化右空指针，
    这样每个叶结点都会有一个后继指针让它们直接右移回溯。
    Morris遍历算法中每个结点都会被遍历两次，第一次是前序输出的时机，第二次是中序输出的时机，
    至于后序遍历，由于没有第三次经过，所以需要使用其他手段实现：
    注意到当遍历到某个结点第二次时，该结点的左子树一定是遍历完的，所以我们只需逆向输出左子树右边界即可，
    而逆向输出右边界实际上就是反转链表，可以反转后输出再反转还原。
    '''

    def morris(self, root):
        def reverse(start):
            pre = None
            cur = start
            while cur:
                cur.right, cur, pre = pre, cur.right, cur
                # next = cur.right
                # cur.right = pre
                # pre = cur
                # cur = next
            return pre

        def print_reverse(start):
            tail = reverse(start)
            cur = tail
            while cur:
                res.append(cur.val)
                cur = cur.right
            reverse(tail)  # 记得反转回来

        if not root:
            return
        cur = root
        res = []
        while cur:
            if not cur.left:
                res.append(cur.val)  # 无论前序中序都输出该结点，后序不能直接输出，因为右结点可能还没遍历到
                cur = cur.right  # 向右子树遍历
            else:
                last_right = cur.left
                while last_right.right and last_right.right != cur:  # 找到左子树的最右子结点
                    last_right = last_right.right
                if not last_right.right:  # 最右结点的右指针为空，第一次来到结点
                    res.append(cur.val)  # 前序visit
                    last_right.right = cur  # 线索化右空指针，指向后继
                    cur = cur.left  # 向左子树遍历
                else:  # 否则是第二次来到结点
                    # res.append(cur.val)  # 中序visit
                    last_right.right = None  # 还原为空指针
                    # print_reverse(cur.left)  # 后序visit, 反转输出左子树右边界
                    cur = cur.right  # 向右子树遍历
        # print_reverse(root) # 后序visit, 最后记得输出整棵树的右边界
        return res

    '''
    morris遍历实际上是时间换空间的策略，因为寻找左子树最右结点所耗时间在最坏情况下不是常数项，
    且后序遍历还要多次反转链表，相当耗时。且类推可知morris遍历应该有一个统一的模板，这个还需想想       
    '''


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
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
        testArgs.append([node8, [8, 6, 5, 7, 10, 9, 11]])  # 前序
        # testArgs.append([node8, [5, 6, 7, 8, 9, 10, 11]])  # 中序
        # testArgs.append([node8, [5, 7, 6, 9, 11, 10, 8]])  # 后序
        # testArgs.append([node8, [8, 6, 10, 5, 7, 9, 11]])  # 层序

        #      2
        #    3   4
        #   5     6
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        ConnectTreeNodes(node2, node3, node4)
        ConnectTreeNodes(node3, node5, None)
        ConnectTreeNodes(node4, None, node6)
        testArgs.append([node2, [2, 3, 5, 4, 6]])  # 前序
        # testArgs.append([node2, [5, 3, 2, 4, 6]])  # 中序
        # testArgs.append([node2, [5, 3, 6, 4, 2]])  # 后序
        # testArgs.append([node2, [2, 3, 4, 5, 6]])  # 层序

        # 单个结点
        testArgs.append([TreeNode(1), [1]])

        # 空树
        testArgs.append([None, None])

        # 随机生成二叉树进行测试

        def correct(root):
            def pre_order(root):
                if not root:
                    return
                res.append(root.val)  # 前序visit
                pre_order(root.left)
                # res.append(root.val) # 中序visit
                pre_order(root.right)
                # res.append(root.val) # 后序visit

            if not root:
                return
            res = []
            pre_order(root)
            return res

        import random
        tree_num = 50  # 二叉树棵数
        node_num = 1000  # 结点数

        for tree in range(tree_num):
            root = TreeNode(-1)
            nodeList = [root]
            randomList = [(root, 'l'), (root, 'r')]
            for i in range(random.randint(0, node_num)):
                newNode = TreeNode(i)
                nodeList.append(newNode)
                connect = random.choice(randomList)
                if connect[1] == 'l':
                    connect[0].left = newNode
                else:
                    connect[0].right = newNode
                newNode.parent = connect[0]
                randomList.remove(connect)
                randomList.append((newNode, 'l'))
                randomList.append((newNode, 'r'))
            testArgs.append([root, correct(root)])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
