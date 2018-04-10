__author__ = 'Hk4Fun'
__date__ = '2018/4/10 15:43'
'''题目描述：
Given a singly linked list, determine if it is a palindrome.
'''
'''主要思路：
时间O（n），空间O（1）

思路1：比较链表的前一半和后一半关于中点是否对称，来到中点前反转链表的前一半，
这样就可以同时从中点出发向两端比较

思路2：思路1改变了链表前半部分的结构，所以在从中间向左边比较时，边比较边反转链表，
这样比较结束时前半部分可以恢复原来的结构
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    :type head: ListNode
    :rtype: bool
    """

    def isPalindrome_change(self, head):
        pre = None
        slow = fast = head
        while fast and fast.next:  # # 边找中点边反转链表
            fast = fast.next.next
            slow.next, slow, pre = pre, slow.next, slow  # 一句话反转链表
        if fast:  # 奇数情况下slow往后移一格（偶数情况下正好）
            slow = slow.next
        while pre and pre.val == slow.val:  # 从中间出发向两边比较
            pre, slow = pre.next, slow.next
        return not pre

    def isPalindrome_no_change(self, head):
        pre = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, pre = pre, slow.next, slow
        right_half = slow.next if fast else slow
        isPali = True
        while pre:
            isPali = isPali and pre.val == right_half.val
            pre.next, pre, slow = slow, pre.next, pre  # 此时，slow和pre的角色调换了（对比之前反转的代码）
            right_half = right_half.next
        return isPali


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
