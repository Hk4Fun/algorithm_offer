__author__ = 'Hk4Fun'
__date__ = '2018/1/7 1:28'

'''题目描述：
输入一个单向链表，输出该链表的中间结点。
如果结点总数为奇数，返回中间结点；如果为偶数则返回中间两个结点的任意一个。
'''
'''主要思路：
定义两个指针，同时从头结点出发，一个指针一次走一步，另一个一次走两步。
当走得快的指针走到链表末尾时，走得慢的指针正好在链表的中间。
注意：快指针每次想往后走时要向后看两步，看是否能一次性走两步，
只能走一步或者来到尾结点不能往后走则放弃遍历，循环结束
这样如果结点数为偶数时，中间结点总是偏左的那个
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindMiddleNode(self, head):
        if not head: return
        slow = fast = head
        while fast.next and fast.next.next:  # 往后看两步
            slow = slow.next
            fast = fast.next.next
        return slow


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

        testArgs.append([linkNodes([1, 2, 3, 4, 5, 6, 7, 8]), [4, 5]])  # 链表个数为偶数
        testArgs.append([linkNodes([1, 2, 3, 4, 5]), [3]])  # 链表个数为奇数
        testArgs.append([linkNodes([1]), [1]])  # 只有一个结点的链表
        testArgs.append([linkNodes([]), [None]])  # 空链表

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result.val if result else result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected[0] or result == expected[1]


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
