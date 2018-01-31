__author__ = 'Hk4Fun'
__date__ = '2018/1/31 18:01'

'''题目描述：
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''
'''主要思路：
设置一个辅助栈，每次入栈时把最小元素
（之前的最小值（辅助栈栈顶）和新压入栈的元素两者的较小值）保存在辅助栈中
出栈时辅助栈一起出栈，这样就可以保证辅助栈的栈顶是最小值
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())

    def pop(self):
        if not self.stack or not self.minStack:
            return
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        if not self.stack:
            return
        return self.stack[-1]

    def min(self):
        if not self.minStack:
            return
        return self.minStack[-1]


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, stack, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    try:
        start = timeit.default_timer()
        result = stack.min()
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


stack = Solution()
stack.push(3)    #[3]
Test("Test1", stack, 3)
stack.push(4)    #[3,4]
Test("Test2", stack, 3)
stack.push(2)    #[3,4,2]
Test("Test3", stack, 2)
stack.push(3)    #[3,4,2,3]
Test("Test4", stack, 2)
stack.pop()      #[3,4,2]
Test("Test5", stack, 2)
stack.pop()      #[3,4]
Test("Test6", stack, 3)
stack.pop()      #[3]
Test("Test7", stack, 3)
stack.push(0)    #[3,0]
Test("Test8", stack, 0)
stack.pop()      #[3]
Test("Test9", stack, 3)
stack.pop()      #[]
Test("Test10", stack, None)
stack.pop()      #[]
Test("Test11", stack, None)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
