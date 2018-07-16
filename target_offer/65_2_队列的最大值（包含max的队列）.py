__author__ = 'Hk4Fun'
__date__ = '2018/3/6 13:47'

'''题目描述：
请定义一个队列并实现函数max得到队列里的最大值，
要求函数max、push_back和pop_front的时间复杂度都为O(1)
'''
'''主要思路：
借助21题和65_1题，可以使用两个队列，一个为普通队列用来存放原始数据，
另一个为双端队列用来维护当前队列的最大值。
维护最大值借助65_1的‘后浪推前浪’的思路（推即淘汰）
入队时，普通队列正常入队，但最大队列要先把前面小于等于它的数从队尾移出再入队；
出队时，普通队列正常出队，但最大队列要看普通队列出队的那个数是否是自己当前队首元素，
是的话最大队列也要把队首出队。如何知道这两个数是否为同一个（重复数字不是同一个）？
这就要求在入队时保存当前元素的入队次序。这里设置为（元素，次序）
取最大值时，最大队列的队首就是当前队列的最大值
'''
from collections import deque

class Solution:
    def __init__(self):
        self.queue = []
        self.maxQueue = deque([])
        self.currentIndex = 0  # 当前元素的入队次序

    def push_back(self, num):
        self.queue.append((num, self.currentIndex))
        while self.maxQueue and num >= self.maxQueue[-1][0]:
            self.maxQueue.pop()
        self.maxQueue.append((num, self.currentIndex))
        self.currentIndex += 1

    def pop_front(self):
        if not self.queue or not self.maxQueue:
            return
        if self.maxQueue[0][1] == self.queue[0][1]:
            self.maxQueue.popleft()
        self.queue.pop(0)

    def max(self):
        if not self.maxQueue:
            return
        return self.maxQueue[0][0]


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, queue, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    try:
        start = timeit.default_timer()
        result = queue.max()
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


queue = Solution()

# [2]
queue.push_back(2)
Test("Test1", queue, 2)

# [2, 3]
queue.push_back(3)
Test("Test2", queue, 3)

# [2, 3, 4]
queue.push_back(4)
Test("Test3", queue, 4)

# [2, 3, 4, 2]
queue.push_back(2)
Test("Test4", queue, 4)

# [3, 4, 2]
queue.pop_front()
Test("Test5", queue, 4)

# [4, 2]
queue.pop_front()
Test("Test6", queue, 4)

# [2]
queue.pop_front()
Test("Test7", queue, 2)

# [2, 6]
queue.push_back(6)
Test("Test8", queue, 6)

# [2, 6, 2]
queue.push_back(2)
Test("Test9", queue, 6)

# [2, 6, 2, 5]
queue.push_back(5)
Test("Test9", queue, 6)

# [6, 2, 5]
queue.pop_front()
Test("Test10", queue, 6)

# [2, 5]
queue.pop_front()
Test("Test11", queue, 5)

# [5]
queue.pop_front()
Test("Test12", queue, 5)

# []
queue.pop_front()
Test("Test13", queue, None)

# []
queue.pop_front()
Test("Test14", queue, None)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
