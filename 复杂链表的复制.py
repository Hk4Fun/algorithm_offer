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
                pCloned.random = dict[pNode.random] # dict[S]=S'
            pNode = pNode.next
            pCloned = pCloned.next
        return pCloneHead

    def Clone3(self, pHead):
        if not pHead:
            return
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next

    # 将复制链表中结点的random指针链接到被复制结点random指针的后一个结点
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedNode.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead

