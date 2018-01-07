__author__ = 'Hk4Fun'
__date__ = '2018/1/7 18:21'

'''题目描述：
给一个链表，判断该链表是否含环，若含环则返回链表的长度和环的长度，否则返回False
'''
'''主要思路：
环的长度：
思路1：当slow和fast在环内相遇时，开始计步数，则当它们再次相遇时slow的步数就正好是环的长度；
思路2：也可以设一个临时指针pTemp指向相遇点，则slow下次来到pTemp时所走过的步数就是环的长度,
       再仔细一想，完全可以让fast来充当pTemp的角色，即fast不动，slow每次走一步。
链表的长度：
思路1：可在上一题的基础上，找到入口点后让pHead重新从头开始遍历，则第二次到达入口点时走过的步数就是链表的长度；
思路2：既然前面已经求得环的长度了，那么在寻找入口点时让pHead记录到达入口点的步数，加上环的长度，不就是链表的长度了吗？

这里实现环的长度思路1和链表的长度思路2
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ListLenAndCircleLen(self, head):
        if not head:
            return
        fast = slow = head
        # 先判断是否含环
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                break
        if fast.next == None:
            return False

        # 第二次遍历计算环长
        CirLen = 0
        fast = fast.next.next  # 先让fast和slow错开
        slow = slow.next
        CirLen += 1
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            CirLen += 1

        # 寻找入口点
        Head2EntryLen = 0
        pHead = head  # 指向头结点
        pMeet = fast  # 指向相遇点
        while pHead != pMeet:  # 二者还没相遇之前一直走下去
            pHead = pHead.next
            pMeet = pMeet.next
            Head2EntryLen += 1

        return Head2EntryLen + CirLen, CirLen


# ================================测试代码================================

import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def linkNodes(values, isCircle, linkIndex):
    # linkIndex表示环的连接点索引，0表示尾结点与第一个结点链接成环，以此类推
    head = ListNode(None)
    lastNode = head
    nodeList = []
    for val in values:
        newNode = ListNode(val)
        nodeList.append(newNode)
        lastNode.next = newNode
        lastNode = newNode
    if isCircle:
        lastNode.next = nodeList[linkIndex]
    return head.next


def Test(testName, head, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()

    try:
        start = timeit.default_timer()
        result = test.ListLenAndCircleLen(head)
        end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


Test('Test1', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], False, 0), False)  # 单向链表，多个结点
Test('Test2', linkNodes([1], False, 0), False)  # 单向链表，单个结点
Test('Test3', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 0), (8, 8))  # 循环链表，多个结点， 尾结点与头结点连接
Test('Test4', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 3), (8, 5))  # 循环链表，多个结点， 尾结点与中间某个结点连接
Test('Test5', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 7), (8, 1))  # 循环链表，多个结点， 尾结点与尾结点连接
Test('Test6', linkNodes([1], True, 0), (1, 1))  # 循环链表，单个结点
Test('Test7', linkNodes([], False, 0), None)  # 空链表

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
