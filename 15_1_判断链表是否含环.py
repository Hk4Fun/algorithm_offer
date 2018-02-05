__author__ = 'Hk4Fun'
__date__ = '2018/1/7 1:49'

'''题目描述：
给一个链表，判断该链表是否含环
'''
'''主要思路：
定义两个指针，同时从链表的头结点出发，一个指针一次走一步，另一个一次走两步。
如果走得快的指针追上了走得慢的指针说明链表含环；
如果快指针来到了链表末尾都没有追上第一个指针，那么链表不含环
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isCircle(self, head):
        if not head:
            return
        fast = slow = head  # 两个指针同时从头结点出发
        while fast.next:  # fast走到链表末尾时结束遍历
            fast = fast.next
            if fast.next:  # fast一次走两步，但如果来到倒数第二个结点时就只能走一步了
                fast = fast.next
            else:  # 说明fast来到了倒数第一个结点，可以判断是单向链表了，直接返回
                return False
            slow = slow.next  # slow一次只走一步
            if fast == slow:  # fast判断一下是否走到了slow的位置
                return True
        return False


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
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

        testArgs = []

        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], False, 0), False])  # 单向链表，多个结点
        testArgs.append([linkNodes([1], False, 0), False])  # 单向链表，单个结点
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 0), True])  # 循环链表，多个结点， 尾结点与头结点连接
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 3), True])  # 循环链表，多个结点， 尾结点与中间某个结点连接
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 7), True])  # 循环链表，多个结点， 尾结点与尾结点连接
        testArgs.append([linkNodes([1], True, 0), True])  # 循环链表，单个结点
        testArgs.append([linkNodes([], False, 0), None])  # 空链表

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
