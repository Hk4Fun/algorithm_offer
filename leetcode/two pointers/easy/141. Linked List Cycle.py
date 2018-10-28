__author__ = 'Hk4Fun'
__date__ = '2018/4/9 13:28'
'''题目描述：
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
'''
'''主要思路：
target_offer 15_3_判断链表是否含环
双指针，一快一慢
时间O（n），空间O（1），n为结点个数
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    :type head: ListNode
    :rtype: bool
    """

    def hasCycle1(self, head):
        if head is None: return False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow: return True
        return False

    def hasCycle2(self, head):  # 使用异常捕捉，不用抠边界情况
        try:
            slow, fast = head, head.next
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []

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
        testArgs.append([linkNodes([], False, 0), False])  # 空链表

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
