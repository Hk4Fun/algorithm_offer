__author__ = 'Hk4Fun'
__date__ = '2018/4/15 22:48'
'''题目描述：
Given a linked list, swap every two adjacent nodes and return its head.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:
Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

'''
'''主要思路：
时间O（n），空间O（1）
这里要求不能交换结点的值，而是要修改结点的连接。但实际上oj检测值并没有检测结点指针。。。
所以可以投机取巧，但这里不这么做
两种实现方式：递归or迭代
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

    def swapPairs_recursive(self, head):
        if not head or not head.next: return head
        p = head.next
        head.next = self.swapPairs_recursive(head.next.next)
        p.next = head
        return p

    def swapPairs_iterative(self, head):
        dummy = cur = ListNode(-1)  # cur指向要交换的两个结点的前一个结点
        dummy.next = head
        while cur.next and cur.next.next:
            p1, p2 = cur.next, cur.next.next
            cur.next, p1.next, p2.next = p2, p2.next, p1
            cur = cur.next.next
        return dummy.next


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
    solution = Solution()
    MyTest(solution=solution).start_test()
