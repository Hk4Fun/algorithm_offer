__author__ = 'Hk4Fun'
__date__ = '2018/1/7 17:20'

'''题目描述：
给一个链表，判断该链表是否含环，若含环则返回环的入口点的索引(从0开始)，否则返回False
'''
'''主要思路：
紧接着上一题的思路，首先明白一点：二者相遇的时候slow一定还没走完环的一周
很好证明：当slow到达入口点时若fast也刚好到达，此时已经发生相遇，slow还没走完环的一周；
当slow到达入口点时若fast在环上除了入口点的位置，那么此时fast到slow的距离是小于一周的，
fast每走两步缩短距离一步，最后slow还没走完环的一周就被fast赶上
知道这一点后，当fast和slow相遇时，假设fast已经在环内循环了n(1<= n)圈（从相遇位置计起，不是入口点计起）。
假设slow走了s步，则fast走了2s步，又由于fast走过的步数 = s + n*r（即 s + 在环上多走的n圈，r为环的长度），则有：
2s = s + n*r  =>  s = n*r；
如果假设整个链表的长度是L，入口到相遇点的距离是x，起点到入口点的距离是a，则有：
a + x = s = n * r  =>  a + x = (n - 1) * r + r  = (n - 1) * r + (L - a)  =>  a = (n - 1) * r + (L -a -x)
设 b = L -a -x ，表示相遇点到入口点的距离，即：a = (n - 1) * r + b
这个等式表明，若在相遇点设一个指针pMeet，在head设一个指针pHead，两者同时走b步后，pMeet将到达入口点，
而此时pHead将距离入口点(n - 1) * r步，是环长的整数倍距离，所以接下去二者一直走，一定能在入口点第一次相遇，
这样不就找到入口点的位置了吗？
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def CircleEntry(self, head):
        if not head: return
        fast = slow = head
        # 先判断是否含环
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast: break
        else: # 正常退出循环说明不含环
            return False
        # 寻找入口点
        index = 0
        pHead = head  # 指向头结点
        pMeet = fast  # 指向相遇点
        while pHead is not pMeet:  # 二者还没相遇之前一直走下去
            pHead = pHead.next
            pMeet = pMeet.next
            index += 1
        return index  # 若要求返回入口点则 return pHead 或 return pMeet


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
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

        testArgs = []

        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], False, 0), False])  # 单向链表，多个结点
        testArgs.append([linkNodes([1], False, 0), False])  # 单向链表，单个结点
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 0), 0])  # 循环链表，多个结点， 尾结点与头结点连接
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 3), 3])  # 循环链表，多个结点， 尾结点与中间某个结点连接
        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8], True, 7), 7])  # 循环链表，多个结点， 尾结点与尾结点连接
        testArgs.append([linkNodes([1], True, 0), 0])  # 循环链表，单个结点
        testArgs.append([linkNodes([], False, 0), None])  # 空链表

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
