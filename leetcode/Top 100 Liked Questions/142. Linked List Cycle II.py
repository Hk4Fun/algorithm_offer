__author__ = 'Hk4Fun'
__date__ = '2018/8/21 18:52'
'''题目描述：
Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space?
'''
'''主要思路：
时间O（n），空间O（1）
target_offer/15_4_含环链表的入口点.py
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if slow is fast:
                while slow is not head:
                    slow, head = slow.next, head.next
                return slow
        return None  # 退出循环说明遇到了None，说明链表不含环


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
