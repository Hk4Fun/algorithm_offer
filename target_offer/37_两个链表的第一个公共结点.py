__author__ = 'Hk4Fun'
__date__ = '2018/2/11 21:53'

'''题目描述：
输入两个单向无环链表，找出它们的第一个公共结点。
'''
'''主要思路：
题目其实与15_6相同，只是在这里找不到就返回None，这里给出其他算法思路：
思路1：暴力枚举。在第一个链表上顺序遍历每个结点，每遍历到一个节点就在第二个链表上遍历每一个节点
       如果在第二个链表上有一个节点和第一个链表上的结点一样，说明两个链表在这个结点上重合，于是
       就找到了它们的第一个公共节点。时间复杂度O(mn)，空间复杂度O(1)。
思路2：栈实现。注意这是两个单向链表，所以第一个公共结点之后是重合的，整体呈'Y'字型，而不可能是'X'
       于是可以从后往前遍历，找到最后一个相同的结点就是第一个相同的公共结点，但单向链表没有向前的指针
       所以采用栈的数据结构实现：分别把两个链表从头到尾的结点依次放入两个辅助栈里，这样两个链表的尾结点
       就位于两个栈顶，接下来比较两个栈顶的结点是否相同。如果相同，则把栈顶弹出接着比较下一个栈顶，
       直到找到最后一个相同的结点。时间复杂度=空间复杂度=O(m+n)
思路3：先走若干步。首先遍历两个链表得到它们的长度，就能知道哪个链表比较长，以及长的链表比短的链表多几个结点，设为x。
       在第二次遍历的时候，在较长链表上先走x步，接着再同时在两个链表上遍历，找到的第一个相同的结点
       就是它们的第一个公共结点。时间复杂度O(m+n)，不需要辅助空间了，空间复杂度O(1)
思路4：同时从头开始遍历，遇到None就返回头结点从新开始遍历，直到二者相同(注意：都为None也属于相同情况)。
       长度相同：
       有公共结点，则第一次遍历时在第一个公共结点就相遇；无公共结点，则走到None看作相遇，返回None
       长度不同：
       有公共结点，设长度分别为m和n，且头部到公共结点长度分别为m'和n'，假设二者第一次在第一个公共结点相遇，
       则有不定方程：m'+i(m+1)=n'+j(n+1)，易知该不定方程的解为i=[lcd(m+1,n+1)/(m+1)]-1,j=[lcd(m+1,n+1)/(n+1)]-1
       存在解，所以一定会在第一个公共结点相遇；
       无公共结点，则把None看作公共结点，所以也一定会相遇，返回None
       设公共长度为x，则由i、j可以推出时间复杂度=O[lcm(m+1,n+1)-(n+1)+n']
                                              =O[lcm(m+1,n+1)-(m+1)+m']
                                              =O[lcm(m+1,n+1)-(x+1)]
                                              =O[lcm(m,n)]，空间复杂度O(1)
思路5：结合思路3和思路4。
       不用计算两个链表的长度差，根据思路4，两个链表指针（p1,p2）都从头开始一起遍历，
       但是p1来到末尾时指向另一个链表的头结点（不是指向原链表的头结点），p2也一样。
       这样第一次遍历时，短的链表指针（假如为p1）来到长链表（假如为l2）的头结点，
       此时p2还在l2上，且p2距离末尾（l2-l1）。p2来到l1头结点时，p1在l2上距离末尾（l2-(l2-l1)）
       此时p1的位置正好就是思路3中长指针先出发来到二者长度差的位置，下面一起遍历一定能够相遇，
       即使没有公共结点，也会在None处一起返回（相当于相遇），相当于转化成思路3   
       整个过程最坏情况下p1、p2各遍历两个链表一次，所以时间复杂度O(m+n)，空间复杂度O(1)。
       注意这个思路和思路4只是在指针来到末尾时指回哪里有区别，其他一致，但复杂度降低了                                   
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 暴力枚举，时间复杂度 = O(mn)，空间复杂度 = O(1)
    def FindFirstCommonNode1(self, pHead1, pHead2):
        if not pHead1 or not pHead2: return
        pNode1 = pHead1
        while pNode1:
            pNode2 = pHead2
            while pNode2:
                if pNode1 is pNode2: return pNode1  # 注意比较的是结点是否一样，不是结点的值
                pNode2 = pNode2.next
            pNode1 = pNode1.next

    # 栈实现，时间复杂度 = 空间复杂度 = O(m+n)
    def FindFirstCommonNode2(self, pHead1, pHead2):
        def PutInStack(pHead):  # 把链表结点放进辅助栈里
            pNode = pHead
            stack = []
            while pNode:
                stack.append(pNode)
                pNode = pNode.next
            return stack

        if not pHead1 or not pHead2: return
        stack1, stack2 = PutInStack(pHead1), PutInStack(pHead2)
        while stack1 and stack2:
            pNode1, pNode2 = stack1.pop(), stack2.pop()
            if pNode1 is not pNode2: return pNode1.next
        # 链表来到末尾，说明两个链表重合（可能部分重合），则第一个公共结点就是较短链表头结点
        return pHead1 if not stack1 else pHead2

    # 先走若干步，时间复杂度=O(m+n)，空间复杂度=O(1)
    def FindFirstCommonNode3(self, pHead1, pHead2):
        def GetListLength(pHead):
            length = 0
            while pHead:
                pHead = pHead.next
                length += 1
            return length

        length1 = GetListLength(pHead1)
        length2 = GetListLength(pHead2)
        LengthDiff = abs(length1 - length2)

        if length1 > length2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1

        for i in range(LengthDiff):  # 较长的链表先走长度之差的步数
            pListHeadLong = pListHeadLong.next

        while pListHeadLong and pListHeadShort and (pListHeadLong is not pListHeadShort):  # 再同时遍历
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next
        return pListHeadLong  # 包含了无公共结点的情况（即返回None）

    # 同时从头开始遍历，时间复杂度=O[lcm(m,n)]，空间复杂度=O(1)
    def FindFirstCommonNode4(self, pHead1, pHead2):
        pNode1, pNode2 = pHead1, pHead2
        while pNode1 is not pNode2:
            pNode1 = pNode1.next if pNode1 else pHead1
            pNode2 = pNode2.next if pNode2 else pHead2
        return pNode1

    # 注意与上一解法比较
    def FindFirstCommonNode5(self, pHead1, pHead2):
        pNode1, pNode2 = pHead1, pHead2
        while pNode1 is not pNode2:
            pNode1 = pNode1.next if pNode1 else pHead2
            pNode2 = pNode2.next if pNode2 else pHead1
        return pNode1


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []

        # 第一个公共结点在链表中间
        # 1 - 2 - 3 \
        #            6 - 7
        #     4 - 5 /
        pNode1 = ListNode(1)
        pNode2 = ListNode(2)
        pNode3 = ListNode(3)
        pNode4 = ListNode(4)
        pNode5 = ListNode(5)
        pNode6 = ListNode(6)
        pNode7 = ListNode(7)
        pNode1.next = pNode2
        pNode2.next = pNode3
        pNode3.next = pNode6
        pNode6.next = pNode7
        pNode4.next = pNode5
        pNode5.next = pNode6
        testArgs.append([pNode1, pNode4, pNode6])

        # 两个链表的值一样
        # 1 - 2 \
        #         3 - 4
        # 1 - 2 /
        pNode1 = ListNode(1)
        pNode_1 = ListNode(1)
        pNode2 = ListNode(2)
        pNode_2 = ListNode(2)
        pNode3 = ListNode(3)
        pNode4 = ListNode(4)
        pNode1.next = pNode2
        pNode2.next = pNode3
        pNode3.next = pNode4
        pNode_1.next = pNode_2
        pNode_2.next = pNode3
        testArgs.append([pNode1, pNode_1, pNode3])

        # 没有公共结点
        # 1 - 2 - 3 - 4
        #
        # 5 - 6 - 7
        pNode1 = ListNode(1)
        pNode2 = ListNode(2)
        pNode3 = ListNode(3)
        pNode4 = ListNode(4)
        pNode5 = ListNode(5)
        pNode6 = ListNode(6)
        pNode7 = ListNode(7)
        pNode1.next = pNode2
        pNode2.next = pNode3
        pNode3.next = pNode4
        pNode5.next = pNode6
        pNode6.next = pNode7
        testArgs.append([pNode1, pNode5, None])

        # 公共结点是最后一个结点
        # 1 - 2 - 3 - 4 \
        #                7
        #         5 - 6 /
        pNode1 = ListNode(1)
        pNode2 = ListNode(2)
        pNode3 = ListNode(3)
        pNode4 = ListNode(4)
        pNode5 = ListNode(5)
        pNode6 = ListNode(6)
        pNode7 = ListNode(7)
        pNode1.next = pNode2
        pNode2.next = pNode3
        pNode3.next = pNode4
        pNode4.next = pNode7
        pNode5.next = pNode6
        pNode6.next = pNode7
        testArgs.append([pNode1, pNode5, pNode7])

        # 公共结点是第一个结点
        # 1 - 2 - 3 - 4 - 5
        # 两个链表完全重合
        pNode1 = ListNode(1)
        pNode2 = ListNode(2)
        pNode3 = ListNode(3)
        pNode4 = ListNode(4)
        pNode5 = ListNode(5)
        pNode1.next = pNode2
        pNode2.next = pNode3
        pNode3.next = pNode4
        pNode4.next = pNode5
        testArgs.append([pNode1, pNode1, pNode1])

        # 第二个链表是第一个链表的一部分
        # 1 - 2 - 3 \
        #            4 - 5
        # 两个链表完全重合
        pNode1 = ListNode(1)
        pNode2 = ListNode(2)
        pNode3 = ListNode(3)
        pNode4 = ListNode(4)
        pNode5 = ListNode(5)
        pNode1.next = pNode2
        pNode2.next = pNode3
        pNode3.next = pNode4
        pNode4.next = pNode5
        testArgs.append([pNode1, pNode4, pNode4])

        # 只有一个结点
        pNode1 = ListNode(1)
        testArgs.append([pNode1, pNode1, pNode1])

        # 空链表
        pNode1 = ListNode(1)
        testArgs.append([None, pNode1, None])
        testArgs.append([pNode1, None, None])
        testArgs.append([None, None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        if not result and not expected: return True
        return result.val == expected.val


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
