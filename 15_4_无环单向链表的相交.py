__author__ = 'Hk4Fun'
__date__ = '2018/1/7 19:02'

'''题目描述：
判断两个无环链表listA和listB是否相交，如果相交，返回相交的节点在listB中的索引（从0开始），否则返回False
'''
'''主要思路：
可以让其中一个链表（不妨设是listA）的尾节点连接到其头部，这样在listB中就一定会出现一个环，
这样就将问题分别转化成了15_1和15_2（交点即为环的入口点）
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ListIntersect(self, headA, headB):
        if not headA or not headB:
            return
        nodeA = headA
        while nodeA.next:  # 找到listA的尾结点
            nodeA = nodeA.next
        nodeA.next = headA  # 连接listA的尾节点连接到其头部

        fast = slow = headB  # 再在listB中判断是否有环
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

        index = 0  # 开始寻找入口点
        pHead = headB
        pMeet = fast
        while pHead != pMeet:
            pHead = pHead.next
            pMeet = pMeet.next
            index += 1
        return index

# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, headA, headB, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()

    try:
        start = timeit.default_timer()
        result = test.ListIntersect(headA, headB)
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


headA = ListNode(1)
headA.next = ListNode(2)            # listA: 1 -> 2 -> None
headB = ListNode(1)                 # listB: 1 -> None
Test('Test1', headA, headB, False)  # 不相交

headA = ListNode(1)
headA.next = ListNode(2)           # listA: 1 \
headB = ListNode(1)                #           2 -> None
headB.next = headA.next            # listB: 1 /
Test('Test2', headA, headB, 1)  # 相交

headA = ListNode(1)
headA.next = ListNode(2)           # listA: 1 ->2 -> None
headB = ListNode(1)                #        |
headB.next = headA                 # listB: 1
Test('Test3', headA, headB, 1)  # 相交


headA = ListNode(1)                # listA: 1 -> None
headB = ListNode(1)                #        |
headB.next = headA                 # listB: 1
Test('Test4', headA, headB, 1)  # 相交

Test('Test5', [], [], None)  # 空链表


print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
