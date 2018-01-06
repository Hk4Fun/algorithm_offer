__author__ = 'Hk4Fun'
__date__ = '2018/1/6 16:41'

'''题目描述：
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
'''主要思路：
不必顺序查找到结点i的前一个节点再删除，这样是O(n)；
要删除结点i，可以先把i的下一个结点j的内容复制到i，然后把i的指针指向j的下一个结点，
最后再删除结点j，其效果刚好是把结点i给删除了
即：当我们想删除一个结点时，并不一定要删除这个结点本身，
可以先把下一个结点的内容复制出来覆盖被删除结点的内容，然后把下一个结点删除
考虑两种特殊情况：
1、如果要删除的是尾结点，它没有下一个结点，此时只能从头开始顺序遍历得到该节点的前序结点，并完成删除
2、如果链表中只有一个结点，即要删除的节点是头结点（它连前序结点都没有），需要单独处理（删除后设为NULL）
'''


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def delete(self):
        self.val = None
        self.next = None


class Solution:
    def DeleteNode(self, ListHead, ToBeDeleted):
        if not ListHead or not ToBeDeleted:  # 头结点和要删除结点都为空返回None
            return

        if ToBeDeleted.next != None:  # 要删除的结点不是尾结点
            Next = ToBeDeleted.next
            ToBeDeleted.val = Next.val
            ToBeDeleted.next = Next.next
            Next.delete()
        elif ListHead == ToBeDeleted:  # 要删除的结点是头结点
            ListHead.delete()
            ToBeDeleted.delete()

        else:
            Node = ListHead
            while Node.next != ToBeDeleted:
                Node = Node.next
            Node.next = None
            ToBeDeleted.delete()


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def getNodes(ListHead):
    l = []
    Node = ListHead
    while Node:
        l.append(Node.val)
        Node = Node.next
    return l


def Test(testName, ListHead, ToBeDeleted, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        test.DeleteNode(ListHead, ToBeDeleted)
        end = timeit.default_timer()
        result = getNodes(ListHead)

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


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
Test('Test1', node1, node3, [1, 2, 4])  # 从多个结点的链表中间删除一个结点

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
Test('Test2', node1, node1, [2,3,4])  # 从多个结点的链表中删除头结点

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
Test('Test3', node1, node4, [1,2,3])  # 从多个结点的链表中删除尾结点

node1 = ListNode(1)
Test('Test4', node1, node1, [None])  # 从只有一个结点的链表中删除唯一结点

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
