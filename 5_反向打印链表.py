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
    def ListReverse_Stack(self, listNode):
        l = []  # 用列表模拟栈
        while listNode:
            l.insert(0, listNode.val)
            listNode = listNode.next
        return l

    def ListReverse_Recursive(self, listNode):
        l = []

        def recursive(listNode):
            if listNode:
                recursive(listNode.next)
                l.append(listNode.val)

        recursive(listNode)
        return l


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def linkNodes(values):
    head = listNode(None)
    lastNode = head
    for val in values:
        newNode = listNode(val)
        lastNode.next = newNode
        lastNode = newNode
    return head.next


def Test(testName, methodType, listNode, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0
    try:
        if methodType == 1 or methodType == '1':
            start = timeit.default_timer()
            result = test.ListReverse_Stack(listNode)
            end = timeit.default_timer()
        elif methodType == 2 or methodType == '2':
            start = timeit.default_timer()
            result = test.ListReverse_Recursive(listNode)
            end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


# Test('Test1_1', 1, linkNodes([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])  # 1->2->3->4->5
# Test('Test1_2', 1, linkNodes([1]), [1])  # 只有一个结点的链表: 1
# Test('Test1_3', 1, [], [])  # 空链表

Test('Test2_1', 2, linkNodes([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])  # 1->2->3->4->5
Test('Test2_2', 2, linkNodes([1]), [1])  # 只有一个结点的链表: 1
Test('Test2_3', 2, [], [])  # 空链表

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
