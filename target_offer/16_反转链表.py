__author__ = 'Hk4Fun'
__date__ = '2018/1/30 15:24'

'''题目描述：
输入一个链表的头结点，反转该链表并输出反转后链表的头结点
'''
'''主要思路：
思路1：定义三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点
       指向后一个结点的指针是为了防止链表断裂，因为需要把当前结点的下一个指针指向前一个结点
思路2：递归实现
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList1(self, pHead):  # 4行代码搞定
        pre, cur = None, pHead
        while cur:
            # pre, cur.next, cur, = cur, pre, cur.next
            # 不能 pre, cur, cur.right = cur, cur.right, pre，否则后面cur.right中的cur是已经更新的cur
            # 因此必须先保存cur.right，至于pre在哪个位置都行，因为它没引用cur
            # 所以为了代码更加容易理解，可以重新调整一下顺序：从后往前
            cur.next, cur, pre = pre, cur.next, cur
            # 上面的一行等于下面四行
            # next = cur.next  # 先保存下一个结点防止断裂
            # cur.next = pre
            # pre = cur
            # cur = next
        return pre

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


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效

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

        self.debug = False
        testArgs = []

        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1]])  # 1->2->3->4->5->6
        testArgs.append([linkNodes([1]), [1]])  # 只有一个结点的链表: 1
        testArgs.append([[], []])  # 空链表

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        def listNodes(pHead):  # 将链表的值按顺序放进列表中
            l = []
            while pHead:
                l.append(pHead.val)
                pHead = pHead.next
            return l

        return listNodes(result)


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
