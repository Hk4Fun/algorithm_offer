__author__ = 'Hk4Fun'
__date__ = '2018/1/2 2:06'

'''题目描述：
用两个栈来实现一个队列，完成队列的入队和出队操作
'''
'''主要思路：
stack1用来入队，stack2用来出队，
出队时若stack2有数据直接弹出，无数据就要把stack1中的全部弹出并压入stack2，然后stack2继续出队
入队时不管stack1有没有数据，直接压入
'''


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def In(self, x):  # 入队时不管stack1有没有数据，直接压入
        self.stack1.append(x)

    def Out(self):
        if not self.stack1 and not self.stack2:
            return
        if not self.stack2:  # stack2无数据就要把stack1中的全部弹出并压入stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  # stack2继续出队


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def Test(testName, operations, l, **expected):
    # operation表示队列操作集合，'in'入队，'out'出队，l为入队列表
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    queue = Solution()
    start = end = 0
    try:
        i = 0
        for oper in operations:
            if oper == 'in':
                start = timeit.default_timer()
                queue.In(l[i])
                end = timeit.default_timer()
                i += 1
            elif oper == 'out':
                start = timeit.default_timer()
                queue.Out()
                end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (expected.get('stack1') == queue.stack1 and expected.get('stack2') == queue.stack2):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


Test('Test1', ['in', 'in', 'in'], [1, 2, 3], stack1=[1, 2, 3], stack2=[])  # 连续入队
Test('Test2', ['in', 'in', 'out', 'in'], [1, 2, 3], stack1=[3], stack2=[2])  # 在非空队列中出队入队
Test('Test3', ['in', 'in', 'out', 'in', 'out', 'out'], [1, 2, 3], stack1=[], stack2=[])  # 出队数等于入队数
Test('Test4', ['out'], [], stack1=[], stack2=[])  # 在空队列中出队

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
