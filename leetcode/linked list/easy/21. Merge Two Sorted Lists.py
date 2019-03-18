__author__ = 'Hk4Fun'
__date__ = '2018/4/12 14:06'
'''题目描述：
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
'''主要思路：
target_offer/17_合并两个排序的链表.py
时间O（n+m），空间O（1）
迭代or递归，递归不用创建伪头结点
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    def mergeTwoLists1(self, l1, l2):
        dummy = tail = ListNode(0)  # 使用虚拟头结点简化迭代逻辑
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:  # 只要有一个为空
            return l1 or l2  # 就返回不为空的那个（都为空返回None）
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists2(l1, l2.next)
        return l2


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
