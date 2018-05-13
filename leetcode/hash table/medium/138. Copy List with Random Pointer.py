__author__ = 'Hk4Fun'
__date__ = '2018/5/13 23:47'
'''题目描述：
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.
Return a deep copy of the list.
'''
'''主要思路：
时间O(n)，空间O(n)
target_offer/26_复杂链表的复制.py 思路2
时间O(n)，空间O(1)
target_offer/26_复杂链表的复制.py 思路3
'''


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList1(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = copy = RandomListNode(0)
        node = head
        table = {}
        while node:
            copy.next = RandomListNode(node.label)
            table[node] = copy.next
            copy = copy.next
            node = node.next
        node, copy = head, dummy.next
        while node:
            if node.random:
                copy.random = table[node.random]
            copy = copy.next
            node = node.next
        return dummy.next

    def copyRandomList2(self, head):
        if not head: return
        node = head
        while node:
            copy = RandomListNode(node.label)
            copy.next = node.next
            node.next = copy
            node = copy.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        node, copy_head = head, head.next
        while node:
            copy = node.next
            node.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            node = node.next
        return copy_head


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
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
