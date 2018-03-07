__author__ = 'Hk4Fun'
__date__ = '2018/1/7 1:28'

'''题目描述：
输入一个单向链表，输出该链表的中间结点。
如果结点总数为奇数，返回中间结点；如果为偶数则返回中间两个结点的任意一个。
'''
'''主要思路：
定义两个指针，同时从头结点出发，一个指针一次走一步，另一个一次走两步。
当走得快的指针走到链表末尾时，走得慢的指针正好在链表的中间。
注意：一次走两步的指针不能一下子走完，因为如果来到倒数第二个结点时就只能走一步了
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindMiddleNode(self, head):
        if not head:
            return
        pNode1 = pNode2 = head  # 两个指针同时从头结点出发
        while pNode1.next:  # 走得快的指针走到链表末尾时结束遍历
            pNode1 = pNode1.next  # 第一个指针一次走两步，但如果来到倒数第二个结点时就只能走一步了
            if pNode1.next:
                pNode1 = pNode1.next
            pNode2 = pNode2.next  # 第二个指针一次只走一步
        return pNode2  # 返回走得慢的指针（第二个指针）


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def linkNodes(values):
            head = ListNode(None)
            lastNode = head
            for val in values:
                newNode = ListNode(val)
                lastNode.next = newNode
                lastNode = newNode
            return head.next

        testArgs = []

        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8]), 5])  # 链表个数为偶数
        testArgs.append([linkNodes([1, 2, 3, 4, 5]), 3])  # 链表个数为奇数
        testArgs.append([linkNodes([1]), 1])  # 只有一个结点的链表
        testArgs.append([linkNodes([]), None])  # 空链表

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result.val if result else result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
