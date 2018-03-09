__author__ = 'Hk4Fun'
__date__ = '2018/1/30 17:11'

'''题目描述：
合并两个单调递增的链表，使得合并后的链表仍然单调递增
'''
'''主要思路：
思路1：递归实现原地合并，将两个链表中值较小的头结点链接到已经合并的链表之后，
       两个链表剩余的结点依然是排序的，因此合并的步骤和之前的步骤一致，可以递归实现，
       注意，合并到最后，必有一个链表不为None，此时将头结点直接链接到最后即可       
思路2：非递归，循环实现，记得最后将剩余的链表链接到新链表中
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge1(self, pHead1, pHead2):
        if not pHead1:
            return pHead2  # 此时如果pHead2也为None也正好直接返回
        elif not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge1(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge1(pHead1, pHead2.next)
            return pHead2

    def Merge2(self, pHead1, pHead2):
        mergeHead = mergeTail = ListNode(0)  # 这个头结点只是用来创建新的链表，真正的合并链表头结点是它的下一个
        while pHead1 and pHead2:  # 只要有一个链表合并结束就结束整个合并
            if pHead1.val >= pHead2.val:
                mergeTail.next = pHead2  # 将较小的结点合并到新链表中
                pHead2 = pHead2.next  # 已合并的链表指针往后移动
            else:
                mergeTail.next = pHead1
                pHead1 = pHead1.next
            mergeTail = mergeTail.next
        # 将剩下的不为空的链表直接链接到新链表后面
        mergeTail.next = pHead1 or pHead2 # 利用短路原则
        return mergeHead.next  # 返回真正的头结点


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

        self.debug = True
        testArgs = []

        testArgs.append([linkNodes([1, 3, 5]), linkNodes([2, 4, 6]), [1, 2, 3, 4, 5, 6]])  # 两个链表交叉递增
        testArgs.append([linkNodes([1, 3, 5]), linkNodes([1, 3, 5]), [1, 1, 3, 3, 5, 5]])  # 两个链表中有重复的数字
        testArgs.append([linkNodes([1, 2, 3]), linkNodes([4, 5, 6]), [1, 2, 3, 4, 5, 6]])  # 两个链表不交叉
        testArgs.append([linkNodes([1]), linkNodes([2]), [1, 2]])  # 两个链表都只有一个数字
        testArgs.append([linkNodes([1, 2, 3]), linkNodes([]), [1, 2, 3]])  # 一个链表为空链表
        testArgs.append([linkNodes([]), linkNodes([]), []])  # 两个链表都为空链表

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
