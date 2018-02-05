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
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        testArgs.append([[1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True])
        testArgs.append([[1, 2, 3, 4, 5], [3, 5, 4, 2, 1], True])
        testArgs.append([[1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False])
        testArgs.append([[1, 2, 3, 4, 5], [3, 5, 4, 1, 2], False])
        testArgs.append([[1], [2], False])
        testArgs.append([[1], [1], True])
        testArgs.append([[], [], False])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
