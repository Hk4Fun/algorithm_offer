__author__ = 'Hk4Fun'
__date__ = '2018/4/12 16:04'
'''题目描述：
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
'''主要思路：
时间O（n），空间O（1）
思路1：类似于leetcode/linked list/easy/83. Remove Duplicates from Sorted List.py
        需要借助一个虚拟头结点
思路2：不用借助虚拟头结点，用pre
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """

    def removeElements1(self, head, val):
        cur = dummy = ListNode(0)
        dummy.next = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

    def removeElements2(self, head, val):
        pre = cur = head
        while cur:
            if head.val == val:
                head = head.next
            elif cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


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
