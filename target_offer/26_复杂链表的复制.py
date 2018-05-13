__author__ = 'Hk4Fun'
__date__ = '2018/2/3 22:30'

'''题目描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，
next指向下一个节点，random指向任意一个节点），
返回结果为复制后复杂链表的head。
'''
'''主要思路：
关键在于如何快速找到random结点在复制链表中的位置
思路1（时间复杂度O(n^2)，空间复杂度O(1)）：
       第一步，复制原链表上的每一个节点，并用next连接起来；
       第二步，在原链表和复制链表设置两个指针同时从头遍历，
       当在原链表中找到每个结点的random结点时停下，此时
       复制链表的指针也正好指向每个复制结点的random结点
思路2（时间复杂度O(n)，空间复杂度O(n)）：
       第一步，复制原始链表上的每一个节点N为N'，并用next连接起来，
       同时建立字典（哈希表）dict[N]=N';
       第二步，如果在原链表中结点N的random指向结点S，那么在复制链表中，
       对应的N'应该指向S'。利用前面建立的字典，则dict[S]=S',可以快速找到random结点
思路3（时间复杂度O(n)，空间复杂度O(1)）：
       第一步，复制原链表的结点N并创建新结点N'，再把N'链接到N的后面；
       第二步，设置每个N'的random。如果原链表上的结点N的random指向S，
       则它对应的复制结点N'的random指向S的下一个结点S'
       第三步，把这个长链表拆分成两个链表，奇数位置上的结点组成原链表，
       偶数位置上的结点组成复制链表
'''


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone1(self, pHead):
        if not pHead:
            return
        # 第一步，复制原链表上的每一个节点，并用next连接起来
        pCloneHead = RandomListNode(pHead.label)
        pClonePre = pCloneHead
        pNode = pHead.next
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pClonePre.next = pCloned
            pNode = pNode.next
            pClonePre = pCloned
        # 第二步，链接复制链表每个结点的random结点
        pNode = pHead
        pCloned = pCloneHead
        while pNode:
            pRandom = pNode.random
            if pRandom:
                pOld = pHead  # 从原链表头结点开始遍历
                pCloneRandom = pCloneHead  # 复制链表也同时从头遍历
                while pOld != pRandom:  # 直到来到原链表的random结点
                    pOld = pOld.next
                    pCloneRandom = pCloneRandom.next
                pCloned.random = pCloneRandom  # 此时的pCloneRandom正好也指向自己的random结点
            pNode = pNode.next
            pCloned = pCloned.next
        return pCloneHead

    def Clone2(self, pHead):
        if not pHead:
            return
        # 第一步，复制原链表上的每一个节点，并用next连接起来
        pCloneHead = RandomListNode(pHead.label)
        pClonePre = pCloneHead
        pNode = pHead.next
        dict = {pHead: pCloneHead}  # 同时建立字典dict[N]=N';
        while pNode:
            pCloned = RandomListNode(pNode.label)
            dict[pNode] = pCloned
            pClonePre.next = pCloned
            pNode = pNode.next
            pClonePre = pCloned
        # 第二步，链接复制链表每个结点的random结点
        pNode = pHead
        pCloned = pCloneHead
        while pNode:
            if pNode.random:
                pCloned.random = dict[pNode.random]  # dict[S]=S'
            pNode = pNode.next
            pCloned = pCloned.next
        return pCloneHead

    def Clone3(self, pHead):
        # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
        def CloneNodes(pHead):
            pNode = pHead
            while pNode:
                pCloned = RandomListNode(pNode.label)
                pCloned.next = pNode.next
                pNode.next = pCloned
                pNode = pCloned.next

        # 将复制链表中结点的random指针链接到被复制结点random指针的后一个结点
        def ConnectRandomNodes(pHead):
            pNode = pHead
            while pNode:
                pCloned = pNode.next
                if pNode.random:
                    pCloned.random = pNode.random.next
                pNode = pCloned.next

        # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
        def ReconnectNodes(pHead):
            pNode = pHead
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next  # 到这里pClonedNode在前，pNode在后，

            while pNode:
                pClonedNode.next = pNode.next  # pNode的下一个与pClonedNode链接
                pClonedNode = pClonedNode.next  # pClonedNode顺着链接后移一格
                pNode.next = pClonedNode.next  # pClonedNode把下一个与pNode链接
                pNode = pNode.next  # pNode顺着链接后移一格，保证pClonedNode在前，pNode在后

            return pClonedHead

        if not pHead:
            return
        CloneNodes(pHead)
        ConnectRandomNodes(pHead)
        return ReconnectNodes(pHead)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def ConnectNode(node, next, random):
            node.next = next
            node.random = random

        testArgs = []

        #         -----------------
        #        \|/              |
        # 1-------2-------3-------4-------5
        # |       |      /|\             /|\
        # --------+--------               |
        #         -------------------------
        pNode1 = RandomListNode(1)
        pNode2 = RandomListNode(2)
        pNode3 = RandomListNode(3)
        pNode4 = RandomListNode(4)
        pNode5 = RandomListNode(5)
        ConnectNode(pNode1, pNode2, pNode3)
        ConnectNode(pNode2, pNode3, pNode5)
        ConnectNode(pNode3, pNode4, None)
        ConnectNode(pNode4, pNode5, pNode2)
        testArgs.append([pNode1, [[1, 2, 3], [2, 3, 5], [3, 4, None], [4, 5, 2], [5, None, None]]])

        # random指向结点自身
        #          -----------------
        #         \|/              |
        #  1-------2-------3-------4-------5
        #         |       | /|\           /|\
        #         |       | --             |
        #         |------------------------|
        pNode1 = RandomListNode(1)
        pNode2 = RandomListNode(2)
        pNode3 = RandomListNode(3)
        pNode4 = RandomListNode(4)
        pNode5 = RandomListNode(5)
        ConnectNode(pNode1, pNode2, None)
        ConnectNode(pNode2, pNode3, pNode5)
        ConnectNode(pNode3, pNode4, pNode3)
        ConnectNode(pNode4, pNode5, pNode2)
        testArgs.append([pNode1, [[1, 2, None], [2, 3, 5], [3, 4, 3], [4, 5, 2], [5, None, None]]])

        # random形成环
        #          -----------------
        #         \|/              |
        #  1-------2-------3-------4-------5
        #          |              /|\
        #          |               |
        #          |---------------|
        pNode1 = RandomListNode(1)
        pNode2 = RandomListNode(2)
        pNode3 = RandomListNode(3)
        pNode4 = RandomListNode(4)
        pNode5 = RandomListNode(5)
        ConnectNode(pNode1, pNode2, None)
        ConnectNode(pNode2, pNode3, pNode4)
        ConnectNode(pNode3, pNode4, None)
        ConnectNode(pNode4, pNode5, pNode2)
        testArgs.append([pNode1, [[1, 2, None], [2, 3, 4], [3, 4, None], [4, 5, 2], [5, None, None]]])

        # 只有一个结点，且其random指向自己
        pNode1 = RandomListNode(1)
        ConnectNode(pNode1, None, pNode1)
        testArgs.append([pNode1, [[1, None, 1]]])

        # 鲁棒性测试
        pNode1 = RandomListNode(1)
        ConnectNode(pNode1, None, pNode1)
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        def Convert(pClonedHead, pHead):
            # 将复杂链表转换成三元组，例如Test1的复杂链表转换后为：
            # [[1,2,3],[2,3,5],[3,4,None],[4,5,2],[5,None,None]]
            if pHead == pClonedHead:  # 防止答题者直接返回pHead
                return
            result = []
            pClonedNode = pClonedHead
            while pClonedNode:
                l = [pClonedNode.label]
                if pClonedNode.next:
                    l.append(pClonedNode.next.label)
                else:
                    l.append(None)
                if pClonedNode.random:
                    l.append(pClonedNode.random.label)
                else:
                    l.append(None)
                result.append(l)
                pClonedNode = pClonedNode.next
            return result

        return Convert(result, *func_arg)


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
