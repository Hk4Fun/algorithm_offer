__author__ = 'Hk4Fun'
__date__ = '2018/1/1 18:58'

'''题目描述：
输入一个链表，从尾到头打印链表每个节点的值（不能改变原链表结构）
'''
'''主要思路：
思路1：使用栈，从头到尾扫描，按顺序放入栈中，最后一个个弹出即从尾到头
思路2：使用递归，每访问一个结点，先递归输出后面的结点，再输出自身
'''


class listNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列
    def ListReverse1(self, listNode):
        l = []  # 用列表模拟栈
        while listNode:
            l.insert(0, listNode.val)
            listNode = listNode.next
        return l

    def ListReverse2(self, listNode):
        def recursive(listNode):
            if listNode:
                recursive(listNode.next)
                l.append(listNode.val)

        l = []
        recursive(listNode)
        return l


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def linkNodes(values):
            head = listNode(None)
            lastNode = head
            for val in values:
                newNode = listNode(val)
                lastNode.next = newNode
                lastNode = newNode
            return head.next

        testArgs = []
        testArgs.append([linkNodes([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1]])  # 1->2->3->4->5
        testArgs.append([linkNodes([1]), [1]])  # 只有一个结点的链表: 1
        testArgs.append([[], []])  # 空链表

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
