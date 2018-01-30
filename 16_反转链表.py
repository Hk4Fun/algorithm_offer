__author__ = 'Hk4Fun'
__date__ = '2018/1/30 15:24'

'''题目描述：
输入一个链表的头结点，反转该链表并输出反转后链表的头结点
'''
'''主要思路：
思路1：定义三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点
       指向后一个结点的指针是为了防止链表断裂，因为需要把当前结点的下一个指针指向前一个结点
思路2：递归实现，具体见代码
思路3：头插法，将当前遍历到的结点插入（指向）链表的头部，最终链表反转，具体细节见代码注释
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList1(self, pHead):
        pReverseHead = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.next  # 先保存下一个结点，防止断裂
            if not pNext:
                pReverseHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReverseHead

    def ReverseList2(self, pHead):
        if not pHead:
            return

        def Recursive(pPrev, pNode):
            if not pNode:
                return pPrev
            pNext = pNode.next
            pNode.next = pPrev
            return Recursive(pNode, pNext)

        pReverseHead = Recursive(pHead, pHead.next)
        pHead.next = None  # 反转后记得将头指针next指向None，否则最后两个结点成环
        return pReverseHead

    def ReverseList3(self, pHead):
        if not pHead:
            return
        pReverseHead = pHead # 当前反转链表头部即为原链表头部
        pNode = pHead.next # pNode永远指向将要插入头部的结点
        while pNode:
            pHead.next = pNode.next # 先把pNode的下一个结点给pHead
            pNode.next = pReverseHead # 然后才把pNode的下一个结点指向反转链表头部pReverseHead
            pReverseHead = pNode # 更新反转链表头部为当前遍历到的结点
            pNode = pHead.next # 反转下一个结点，注意pHead不动，最终会变成尾结点
        return pReverseHead # 返回反转链表头部

    # ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
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
            result = listNodes(test.ReverseList1(listNode))
            end = timeit.default_timer()
        elif methodType == 2 or methodType == '2':
            start = timeit.default_timer()
            result = listNodes(test.ReverseList2(listNode))
            end = timeit.default_timer()
        elif methodType == 3 or methodType == '3':
            start = timeit.default_timer()
            result = listNodes(test.ReverseList3(listNode))
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


# Test('Test1_1', 1, linkNodes([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])  # 1->2->3->4->5->6
# Test('Test1_2', 1, linkNodes([1]), [1])  # 只有一个结点的链表: 1
# Test('Test1_3', 1, [], [])  # 空链表
#
# Test('Test2_1', 2, linkNodes([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])  # 1->2->3->4->5->6
# Test('Test2_2', 2, linkNodes([1]), [1])  # 只有一个结点的链表: 1
# Test('Test2_3', 2, [], [])  # 空链表

Test('Test3_1', 3, linkNodes([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])  # 1->2->3->4->5->6
Test('Test3_2', 3, linkNodes([1]), [1])  # 只有一个结点的链表: 1
Test('Test3_3', 3, [], [])  # 空链表

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
