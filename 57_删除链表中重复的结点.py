__author__ = 'Hk4Fun'
__date__ = '2018/2/23 11:39'

'''题目描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
'''主要思路：
思路1：非递归。一前一后两个指针pre和cur，cur负责在前面‘探路’，遇到重复结点就一直往后删除，
       确认是唯一结点就让pre后移，这样pre其实一直指向唯一结点的尾部。
       注意头结点可能和后面的结点重复，所以头结点可能被删除
思路2：递归实现
思路3：递归实现。是思路2的简化，将思路2中的两处递归改成一处。
       将该思路改成循环版那就是思路1的简化版了
思路4：先建立一个键为结点指针而值为对应的结点值的字典，
       然后根据结点值从中筛选出值不重复的结点指针，
       最后把这些筛选出来的唯一值的结点链接起来
       这种算法多使用了O(n)的空间
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication1(self, pHead):
        if not pHead:
            return
        pre = None  # pre一开始初始化为None，因为还没有开始确定唯一结点
        cur = pHead
        while cur:
            if cur.next and cur.next.val == cur.val:  # 找到重复的结点
                val = cur.val
                delNode = cur  # 从重复结点的第一个开始删除
                while delNode and delNode.val == val:  # 连续删除与当前结点重复的结点
                    delNode = delNode.next  # python有垃圾回收，所以直接把删除指针后移即可
                if not pre:  # 如果pre始终为None，说明从头结点开始就重复了，直接把头结点改掉
                    pHead = delNode  # 连续删除重复结点后的删除指针指向第一个与当前结点不同的结点
                else:
                    pre.next = delNode  # 将第一个与当前结点不同的结点链接到pre后面
                cur = delNode  # 更新cur指向第一个与当前结点不同的结点
            else:  # 没有找到重复结点，确定是唯一结点
                pre = cur  # 把pre往后移
                cur = cur.next  # cur也后移
        return pHead

    def deleteDuplication2(self, pHead):
        if not pHead or not pHead.next:  # 只有0个或1个结点时直接返回
            return pHead
        if pHead.val == pHead.next.val:  # 当前结点是重复结点
            cur = pHead.next.next
            while cur and cur.val == pHead.val:
                # 跳过那些值与当前结点相同的全部结点，找到第一个与当前结点不同的结点
                cur = cur.next
            return self.deleteDuplication2(cur)  # 从第一个与当前结点不同的结点开始递归
        else:  # 当前结点不是不是重复结点
            # 从下一个结点开始递归，并把递归结果返回的头结点链接到当前结点后面
            pHead.next = self.deleteDuplication2(pHead.next)
            return pHead

    def deleteDuplication3(self, pHead):
        if not pHead or not pHead.next:  # 只有0个或1个结点时直接返回
            return pHead
        # 用两层循环来跳过重复的结点，直到pHead.val ！= pHead.next.val
        # 用来应付‘1-1-2-2-3-3-4-5-...’的情况
        while pHead and pHead.next and pHead.val == pHead.next.val:
            while pHead and pHead.next and pHead.val == pHead.next.val:
                pHead = pHead.next
            pHead = pHead.next
        if pHead:
            # 此时pHead后面那个结点值一定与pHead不同，可以从后面那个结点开始递归
            pHead.next = self.deleteDuplication3(pHead.next)
        return pHead

    def deleteDuplication4(self, pHead):
        if not pHead:
            return
        dic = {}
        cur = pHead
        while cur:
            dic[cur] = cur.val
            cur = cur.next
        onlyOne = list(filter(lambda pNode: list(dic.values()).count(pNode.val) == 1, dic.keys()))
        tmpHead = ListNode(0)
        cur = tmpHead
        for pNode in onlyOne:
            cur.next = pNode
            cur = cur.next
        cur.next = None  # 记得要把尾结点的next指向None
        return tmpHead.next


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

        testArgs.append([linkNodes([1, 2, 3, 3, 4, 4, 5]), [1, 2, 5]])
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7]])
        testArgs.append([linkNodes([1, 1, 1, 1, 1, 1, 2]), [2]])
        testArgs.append([linkNodes([1, 1, 1, 1, 1, 1, 1]), []])
        testArgs.append([linkNodes([1, 1, 2, 2, 3, 3, 4, 4]), []])
        testArgs.append([linkNodes([1, 1, 2, 3, 3, 4, 5, 5]), [2, 4]])
        testArgs.append([linkNodes([1, 2]), [1, 2]])
        testArgs.append([linkNodes([1]), [1]])
        testArgs.append([linkNodes([1, 1]), []])
        testArgs.append([None, []])

        return testArgs

    def convert(self, result, *func_arg):
        cur = result
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
