__author__ = 'Hk4Fun'
__date__ = '2018/4/16 21:38'
'''题目描述：
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
'''主要思路：
时间O（n），空间O（1）
头插法
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            pre = pre.next
        start, then = pre.next, pre.next.next

        # 1 - 2 - 3 - 4 - 5; m = 2; n = 4 - --> pre = 1, start = 2, then = 3
        # dummy-> 1 -> 2 -> 3 -> 4 -> 5
        for _ in range(n - m):
            # pre.next, start.next, then.next, = then, then.next, pre.next
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        # first reversing: dummy->1 - 3 - 2 - 4 - 5; pre = 1, start = 2, then = 4
        # second reversing: dummy->1 - 4 - 3 - 2 - 5; pre = 1, start = 2, then = 5(finish)
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
