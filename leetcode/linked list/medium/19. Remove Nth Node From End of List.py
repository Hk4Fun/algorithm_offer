__author__ = 'Hk4Fun'
__date__ = '2018/4/14 22:40'
'''题目描述：
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
'''
'''主要思路：
时间O（n），空间O（1）
思路1：
要求遍历一遍链表删除倒数第n个结点，
借助题目target_offer/15_1_链表倒数第k个结点.py思路2
双指针fast先走n步，然后一起走，当fast来到None时，slow刚好来到倒数第n个结点
由于题目说明了n的值合法，所以不用考虑n溢出的情况，
但这里需考虑如果n=1的话，需要知道slow的pre，
于是借助虚拟头结点（哨兵）dummy来避免删除head的情况

思路2：
既然可以获得倒数第n个结点，那干嘛不获取倒数第n+1个结点，这样删除不是更直接？
dummy也可以不用要了，想想什么时候会删掉头结点？不就是n为链表长度的时候吗？
而fast不是提前走了n步吗？所以当fast走n步来到None，说明删除的是头结点，直接返回head.next就行了
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    def removeNthFromEnd(self, head, n):
        slow = fast = head
        pre = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n):  # fast先走n步
            fast = fast.next
        while fast:  # 然后一起走，直到fast为None
            pre, slow, fast = slow, slow.next, fast.next
        pre.next = slow.next
        return dummy.next  # 返回真正的头结点

    def removeNthFromEnd_best(self, head, n):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None: # 删除倒数第n个结点，即删除头结点
            return head.next
        while fast.next:  # 注意这里的循环条件，slow来到倒数第 n+1 个结点
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
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
