__author__ = 'Hk4Fun'
__date__ = '2018/1/30 17:11'

'''题目描述：
合并两个单调递增的链表，使得合并后的链表仍然单调递增
'''
'''主要思路：
递归实现原地合并，将两个链表中值较小的头结点链接到已经合并的链表之后，
两个链表剩余的结点依然是排序的，因此合并的步骤和之前的步骤一致，可以递归实现，
注意，合并到最后，必有一个链表不为None，此时将头结点直接链接到最后即可       
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2  # 此时如果pHead2也为None也正好直接返回
        elif not pHead2:
            return pHead1

        pMergedHead = None
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)

        return pMergedHead

    # ================================测试代码================================


import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def linkNodes(values):  # 根据给的值创建链表
    head = ListNode(None)
    lastNode = head
    for val in values:
        newNode = ListNode(val)
        lastNode.next = newNode
        lastNode = newNode
    return head.next


def listNodes(pHead):  # 将链表的值按顺序放进列表中
    l = []
    while pHead:
        l.append(pHead.val)
        pHead = pHead.next
    return l


def Test(testName, listNode1, listNode2, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = listNodes(test.Merge(listNode1, listNode2))
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


Test('Test1', linkNodes([1, 3, 5]), linkNodes([2, 4, 6]), [1, 2, 3, 4, 5, 6]) # 两个链表交叉递增
Test('Test2', linkNodes([1, 3, 5]), linkNodes([1, 3, 5]), [1, 1, 3, 3, 5, 5]) # 两个链表中有重复的数字
Test('Test3', linkNodes([1, 2, 3]), linkNodes([4, 5, 6]), [1, 2, 3, 4, 5, 6]) # 两个链表不交叉
Test('Test4', linkNodes([1]), linkNodes([2]), [1, 2]) # 两个链表都只有一个数字
Test('Test5', linkNodes([1, 2, 3]), linkNodes([]), [1, 2, 3]) # 一个链表为空链表
Test('Test6', linkNodes([]), linkNodes([]), []) #  两个链表都为空链表



print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
