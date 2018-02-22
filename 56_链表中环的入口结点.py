__author__ = 'Hk4Fun'
__date__ = '2018/2/22 18:04'

'''题目描述：
一个链表中包含环，请找出该链表的环的入口结点。
'''
'''主要思路：
此题和15_4是一样的，这里提供另一个思路：
先获取环的长度n，然后在头部设两个指针p1，p2，让p1先走n步，然后两个指针以相同速度向前移动，
当二者首次相遇时，相遇点即为环的入口点。那么如何获取环的长度？这在15_5中也有相应的思路：
在头部设两个指针，快指针fast每次走2步，慢指针slow每次走1步，则两者一定在环中相遇。相遇后fast
不动，让slow接着走，一边走一边计步数，则当它再次来到相遇点（fast的位置）时，所走过的步数即为
环的长度。记得在获取环的长度之前先判断是否含环：slow和fast能相遇说明含环
另一个思路是采用断链法：
两个指针，一个在前面before，另一个紧邻着这个指针，在后面after。
两个指针同时向前移动，每移动一次，前面的指针before的next指向None。
也就是说：访问过的结点都断开，那么当before来到环的入口点并将其next指向None后，环被打开，
入口点成为了尾结点，则最后after为None的时候，before第二次来到尾结点，此时返回before即可
由于该算法会破坏原链的结构，所以并不推荐
还有一种思路：
遍历链表，用一个数组存放遍历过的结点指针，则遍历遇见的第一个重复的指针即为入口结点
该思路多使用了O(n)的空间，但代码简洁许多，实际上由于少去函数调用和指针复杂操作反而更快
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 没有入口点就返回None，有就返回指向该入口结点的指针
    def EntryNodeOfLoop1(self, pHead):
        def isLoop(pHead):
            # 判断是否含环，不含环返回False，含环则返回相遇点
            fast = slow = pHead
            while fast.next:
                fast = fast.next
                if fast.next:  # 确定fast是否能再走一步
                    fast = fast.next
                else:  # None说明来到尾部，即不含环
                    return False
                slow = slow.next
                if fast == slow:
                    return slow
            if not fast.next:
                return False

        def loopLen(meetNode):
            # 返回环的长度
            cirLen = 1
            tmp = meetNode
            while tmp.next != meetNode:
                tmp = tmp.next
                cirLen += 1
            return cirLen

        if not pHead:
            return
        meetNode = isLoop(pHead)
        if not meetNode:
            return
        p1 = p2 = pHead
        for i in range(loopLen(meetNode)):
            p1 = p1.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    # def EntryNodeOfLoop2(self, pHead):
    # # 该算法会破坏原链的结构，所以只能测试1次，再次测试会无法通过
    #     def isLoop(pHead):
    #         # 判断是否含环，不含环返回False，含环则返回相遇点
    #         fast = slow = pHead
    #         while fast.next:
    #             fast = fast.next
    #             if fast.next:  # 确定fast是否能再走一步
    #                 fast = fast.next
    #             else:  # None说明来到尾部，即不含环
    #                 return False
    #             slow = slow.next
    #             if fast == slow:
    #                 return slow
    #         if not fast.next:
    #             return False
    #
    #     if not pHead:
    #         return
    #     meetNode = isLoop(pHead)
    #     if not meetNode:
    #         return
    #     before = pHead
    #     after = pHead.next
    #     while after:
    #         before.next = None
    #         before = after
    #         after = after.next
    #     return before

    def EntryNodeOfLoop3(self, pHead):
        tmp = []
        p = pHead
        while p:
            if p in tmp:
                return p
            tmp.append(p)
            p = p.next


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 单向链表，多个结点
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        testArgs.append([node1, None])

        # 单向链表，单个结点
        node1 = ListNode(1)
        testArgs.append([node1, None])

        # 循环链表，单个结点
        node1 = ListNode(1)
        node1.next = node1
        testArgs.append([node1, node1])

        # 循环链表，多个结点， 尾结点与头结点连接
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node1
        testArgs.append([node1, node1])

        # 循环链表，多个结点， 尾结点与中间某个结点连接
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        testArgs.append([node1, node2])

        # 循环链表，多个结点， 尾结点与尾结点连接
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node4
        testArgs.append([node1, node4])

        # 空链表
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
