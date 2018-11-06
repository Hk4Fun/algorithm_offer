__author__ = 'Hk4Fun'
__date__ = '2018/8/20 18:49'
'''题目描述：
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
'''主要思路：
merge sort

思路1（时间O（nlogn），空间O（n））：
自顶向下，先利用快慢指针找到链表中间结点然后分割开，
不断下去来到底部只有一个结点直接返回
然后使用dummy结点往上merge
由于使用了递归，所以空间O（n）

思路2（时间O（nlogn），空间O（1））：
自底向上，消除递归

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    :type head: ListNode
    :rtype: ListNode
    """

    def sortList1(self, head):
        def split(head):
            pre, slow, fast = None, head, head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            return head, slow

        def merge(h1, h2):
            dummy = tail = ListNode(0)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next = h1
                    h1 = h1.next
                else:
                    tail.next = h2
                    h2 = h2.next
                tail = tail.next
            tail.next = h1 or h2
            return dummy.next

        if head is None or head.next is None: return head
        return merge(*map(self.sortList, split(head)))

    def sortList2(self, head):
        def length(head):
            """获取链表长度"""
            count = 0
            while head:
                head = head.next
                count += 1
            return count

        def split(head, size):
            """从head开始往后切下size大小的链表，并返回分割后的下一段的头结点"""
            i = 1
            while i < size and head:
                head = head.next
                i += 1
            if head is None: return
            next = head.next
            head.next = None
            return next

        def merge(h1, h2, tail):
            """把h1和h2合并到tail后面并返回合并后的尾结点"""
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next = h1
                    h1 = h1.next
                else:
                    tail.next = h2
                    h2 = h2.next
                tail = tail.next
            tail.next = h1 or h2
            while tail.next:
                tail = tail.next
            return tail

        if head is None: return
        size = length(head)
        sz = 1  # 合并块的大小
        dummy = ListNode(0)
        dummy.next = head
        while sz < size:
            tail, cur = dummy, dummy.next  # cur表示当前正在分割的头结点，tail表示已经合并的尾结点
            # 注意每一轮cur的初始化必须是dummy.next而不是head
            # 因为每一轮merge过后head可能不再是头结点，但dummy一直不变，所以dummy.next永远指向头结点
            while cur:
                l = cur  # 左链表头结点
                r = split(l, sz)  # 以sz大小分割出左链表并拿到右链表的头结点
                cur = split(r, sz)  # 再以sz为大小分割出右链表并拿到下次开始分割的头结点
                tail = merge(l, r, tail)  # 合并左链表和右链表到已经合并好的链表的尾结点，并拿到合并后的尾结点给下次合并使用
            sz *= 2  # 合并块的大小扩大2倍
        return dummy.next


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
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
    MyTest(Solution()).start_test()
