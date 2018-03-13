__author__ = 'Hk4Fun'
__date__ = '2018/1/7 0:11'

'''题目描述：
输入一个单向链表，输出该链表中倒数第k个结点。
'''
'''主要思路：
思路1：遍历两次链表，第一次统计链表结点个数，
       第二次就能找到倒数第k个结点，在（n-k+1）的位置
思路2：定义两个指针，第一个先从头开始走k-1步，第二个保持不动；
       从第k步开始，第二个指针也开始从头遍历。
       由于两个指针的距离保持在k-1，
       所以当第一个指针来到链表尾结点时第二个指针正好来到倒数第k个结点: n-(k-1)，
       该方法只需遍历一遍链表。
考虑特殊情况：
       1、传入的头指针为空指针。返回None即可；
       2、传入的k<=0。k-1将得到负数，而倒数第0个结点没有意义，返回None即可；
       3、传入的k大于链表结点总数。很明显不能完成向前走k-1步，
          所以第一个指针在向前走k-1步时for循环中加上if判断next是否为None
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail1(self, head, k):
        if not head or k <= 0:
            return

        count = 0
        pNode = head
        while pNode:  # 第一次遍历链表以获取结点总数
            pNode = pNode.next
            count += 1
        if k > count:  # k大于链表结点总数
            return

        pNode = head
        for i in range(count - k):  # 第二次从头走(count-k)步就可以来到倒数第k个结点
            pNode = pNode.next
        return pNode

    def FindKthToTail2(self, head, k):
        if not head or k <= 0:
            return

        pAHead = head

        for i in range(k - 1):  # 第一个指针先走k-1步
            if pAHead.next:  # 边走边判断，防止k大于链表结点总数
                pAHead = pAHead.next
            else:  # k大于链表结点总数
                return
        pBehind = head
        while pAHead.next:  # 第一个指针到尾结点就结束遍历
            pAHead = pAHead.next
            pBehind = pBehind.next  # 第二个指针开始与第一个同时遍历
        return pBehind  # 返回此时第二个结点


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

        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), 3, 4])  # 要找的结点在链表中间
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), 1, 6])  # 要找的结点是链表的尾结点
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), 6, 1])  # 要找的结点是链表的头结点
        testArgs.append([linkNodes([]), 100, None])  # 测试空链表
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), 100, None])  # k大于链表的结点总数
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), 0, None])  # k=0
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6]), -100, None])  # k<0

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result.val if result else result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
