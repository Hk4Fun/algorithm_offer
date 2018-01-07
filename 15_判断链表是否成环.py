__author__ = 'Hk4Fun'
__date__ = '2018/1/7 1:49'

'''题目描述：
给一个链表，判断该链表是否成环
'''
'''主要思路：
定义两个指针，同时从链表的头结点出发，一个指针一次走一步，另一个一次走两步。
如果走得快的指针追上了走得慢的指针说明链表成环；
如果快指针来到了链表末尾都没有追上第一个指针，那么链表不成环
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isCircle(self, head):
        if not head:
            return
        pNode1 = pNode2 = head  # 两个指针同时从头结点出发
        while pNode1.next:  # 走得快的指针走到链表末尾时结束遍历
            pNode1 = pNode1.next
            if pNode1 == pNode2:  # 第一个指针每走一步都要判断一下是否走到了第二个指针的位置
                return True
            if pNode1.next:  # 第一个指针一次走两步，但如果来到倒数第二个结点时就只能走一步了
                pNode1 = pNode1.next
            else:  # 说明来到了倒数第一个结点，可以判断是单向链表了，直接返回
                return False
            pNode2 = pNode2.next  # 第二个指针一次只走一步
        return False


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


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


def Test(testName, head, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()

    try:
        start = timeit.default_timer()
        result = test.isCircle(head)
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


Test('Test1', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], False, 0), False)  # 单向链表，多个结点
Test('Test2', linkNodes([1], False, 0), False)  # 单向链表，单个结点
Test('Test3', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 0), True)  # 循环链表，多个结点， 尾结点与头结点连接
Test('Test4', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 3), True)  # 循环链表，多个结点， 尾结点与中间某个结点连接
Test('Test5', linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 7), True)  # 循环链表，多个结点， 尾结点与尾结点连接
Test('Test6', linkNodes([1], True, 0), True)  # 循环链表，单个结点
Test('Test7', linkNodes([], False, 0), None)  # 空链表

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
