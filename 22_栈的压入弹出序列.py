__author__ = 'Hk4Fun'
__date__ = '2018/1/31 21:43'

'''题目描述：
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
'''主要思路：
设置一个辅助栈，用来装压栈序列，不断压入压栈序列的数，每压入一次，
就看一下当前栈顶元素是否为当前弹出数，是的话弹出并遍历下一个弹出数，
继续检查，直到辅助栈空或者当前栈顶元素不为弹出序列第一个，
就继续压入压栈序列的数，直到压完所有的数，最终检查辅助栈是否为空，空则说明该序列为弹出序列
即：如果下一个弹出的数字刚好是栈顶数字，那么直接弹出。如果下一个弹出的数字不在栈顶，
就把压栈序列中还没入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止。
如果所有的数字都压入栈了仍然没有找到下一个弹出的数字，那么该序列就不可能是一个弹出序列
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV or len(pushV) != len(popV):
            return False
        stack = []
        j = 0
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        return False if len(stack) else True


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, pushV, popV, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.IsPopOrder(pushV, popV)
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

Test('Tset1', [1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True)
Test('Tset2', [1, 2, 3, 4, 5], [3, 5, 4, 2, 1], True)
Test('Tset3', [1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)
Test('Tset4', [1, 2, 3, 4, 5], [3, 5, 4, 1, 2], False)
Test('Tset5', [1], [2], False)
Test('Tset6', [1], [1], True)
Test('Tset7', [], [], False)


print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))