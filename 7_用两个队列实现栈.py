__author__ = 'Hk4Fun'
__date__ = '2018/1/2 14:22'

'''题目描述：
用两个队列来实现一个栈，完成栈的Push和Pop操作
'''
'''主要思路：
Push时如果queue1和queue2都为空，随便压入哪个都行，这里压入queue1
如果有一个非空，就压入那个非空队列
Pop时如果queue1和queue2都为空则直接返回（栈空），否则必有一个非空，
则把那个非空队列中除了最后一个的元素全部出队并入队另一个空队列，然后弹出那个最后的元素
'''


class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def Push(self, x):
        if not self.queue2:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def Pop(self):
        if not self.queue1 and not self.queue2:
            return
        if not self.queue1:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()
        if not self.queue2:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()


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
    stack = Solution()
    start = end = 0
    try:
        i = 0
        for oper in operations:
            if oper == 'push':
                start = timeit.default_timer()
                stack.Push(l[i])
                end = timeit.default_timer()
                i += 1
            elif oper == 'pop':
                start = timeit.default_timer()
                stack.Pop()
                end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (expected.get('queue1') == stack.queue1 and expected.get('queue2') == stack.queue2):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


Test('Test1', ['push', 'push', 'push'], [1, 2, 3], queue1=[1, 2, 3], queue2=[])  # 连续压栈
Test('Test2', ['push', 'push', 'pop', 'push'], [1, 2, 3], queue1=[], queue2=[1, 3])  # 在非空栈中压栈弹栈
Test('Test3', ['push', 'push', 'pop', 'push', 'pop', 'pop'], [1, 2, 3], queue1=[], queue2=[])  # 压栈数等于弹栈数
Test('Test4', ['pop'], [], queue1=[], queue2=[])  # 在空栈弹栈

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
