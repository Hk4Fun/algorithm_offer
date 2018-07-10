__author__ = 'Hk4Fun'
__date__ = '2018/1/7 19:02'

'''题目描述：
判断两个无环链表listA和listB是否相交，如果相交，返回相交的节点在listB中的索引（从0开始），否则返回False
'''
'''主要思路：
可以让其中一个链表（不妨设是listA）的尾节点连接到其头部，这样在listB中就一定会出现一个环，
这样就将问题分别转化成了15_3和15_4（交点即为环的入口点）
（参考题37，给出其他算法思路，不要被前面几道题的思路给局限了）
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ListIntersect(self, headA, headB):
        if not headA or not headB: return
        nodeA = headA
        while nodeA.next:  # 找到listA的尾结点
            nodeA = nodeA.next
        nodeA.next = headA  # 连接listA的尾节点连接到其头部
        fast = slow = headB  # 再在listB中判断是否有环
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast: break
        else:  # 正常退出循环说明不含环
            return False
        # 开始寻找入口点
        index = 0
        pHead = headB
        pMeet = fast
        while pHead != pMeet:
            pHead = pHead.next
            pMeet = pMeet.next
            index += 1
        return index


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        headA = ListNode(1)
        headA.next = ListNode(2)  # listA: 1 -> 2 -> None
        headB = ListNode(1)  # listB: 1 -> None
        testArgs.append([headA, headB, False])  # 不相交

        headA = ListNode(1)
        headA.next = ListNode(2)  # listA: 1 \
        headB = ListNode(1)  # 2 -> None
        headB.next = headA.next  # listB: 1 /
        testArgs.append([headA, headB, 1])  # 相交

        headA = ListNode(1)
        headA.next = ListNode(2)  # listA: 1 ->2 -> None
        headB = ListNode(1)  # |
        headB.next = headA  # listB: 1
        testArgs.append([headA, headB, 1])  # 相交

        headA = ListNode(1)  # listA: 1 -> None
        headB = ListNode(1)  # |
        headB.next = headA  # listB: 1
        testArgs.append([headA, headB, 1])  # 相交

        testArgs.append([[], [], None])  # 空链表

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
