__author__ = 'Hk4Fun'
__date__ = '2018/1/7 1:28'

'''题目描述：
输入一个单向链表，输出该链表的中间结点。
如果结点总数为奇数，返回中间结点；如果为偶数则返回中间两个结点的任意一个。
'''
'''主要思路：
定义两个指针，同时从头结点出发，一个指针一次走一步，另一个一次走两步。
当走得快的指针走到链表末尾时，走得慢的指针正好在链表的在中间。
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
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def linkNodes(values):
    head = ListNode(None)
    lastNode = head
    for val in values:
        newNode = ListNode(val)
        lastNode.next = newNode
        lastNode = newNode
    return head.next


def Test(testName, head, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()

    try:
        start = timeit.default_timer()
        result = test.FindMiddleNode(head)
        end = timeit.default_timer()
        if result:
            result = result.val
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


Test('Test1', linkNodes([1, 2, 3, 4, 5, 6, 7, 8]), 5)  # 链表个数为偶数
Test('Test2', linkNodes([1, 2, 3, 4, 5]), 3)  # 链表个数为奇数
Test('Test3', linkNodes([]), None)  # 空链表

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
