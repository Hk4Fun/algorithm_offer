__author__ = 'Hk4Fun'
__date__ = '2018/7/16 9:21'
'''题目来源:
小米三面
'''
'''题目描述：
一副从1到n的牌，每次从手里牌堆顶取一张放桌子上，再从手里牌堆顶取一张放手里牌堆底，
重复以上两步直到手里没牌，最后桌子上的牌从顶到底是从1到n有序，
设计程序，输入n，输出一开始手里牌堆的从顶到底的顺序数组，比如：
n = 5 时, 牌堆的顺序数组为[5,1,4,2,3]，则有：
手中s(顶->底)：[5,1,4,2,3] ->  [4,2,3,1] -> [3,1,2] -> [2,1] ---> [1] -------> []
桌子a(顶->底)：[]------------> [5]  ------> [4,5] ---> [3,4,5] -> [2,3,4,5] -> [1,2,3,4,5]
'''
'''主要思路：
时间O（n），空间O（n）：
s = [1,2,3,4,5] 先按照题目规则得到 a = [2,4,5,3,1]，
可以把s中的值看作下标，则有：
s中1号位置的牌最终会被放到a中5号位置
s中2号位置的牌最终会被放到a中1号位置
s中3号位置的牌最终会被放到a中4号位置
s中4号位置的牌最终会被放到a中2号位置
s中5号位置的牌最终会被放到a中3号位置
因此，我们只需把
s中1号位置的牌放5，这样它最终会被放到a中5号位置
s中2号位置的牌放1，这样它最终会被放到a中1号位置
s中3号位置的牌放4，这样它最终会被放到a中4号位置
s中4号位置的牌放2，这样它最终会被放到a中2号位置
s中5号位置的牌放3，这样它最终会被放到a中3号位置
即按下标排序（重新映射，可逆）：
s[2] = 1
s[4] = 2
s[5] = 3
s[3] = 4
s[1] = 5
最终得到手中牌堆 s = [5,1,4,2,3]
'''

from collections import deque


class Solution:
    def MiTest(self, n):
        if not n: return []
        s = deque([i + 1 for i in range(n)])  # 手中牌堆
        a = deque([])  # 桌子牌堆
        for i in range(n):
            a.appendleft(s.popleft())
            if s: s.append(s.popleft())
        s = [0] * n
        for i, v in enumerate(a):
            s[v - 1] = i + 1
        return s


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        test_num = 10
        for i in range(test_num):
            testArgs.append([i, i])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        n, = func_arg
        s = deque(result)
        a = deque([])
        for i in range(n):
            a.appendleft(s.popleft())
            if s: s.append(s.popleft())
        return a == deque([i + 1 for i in range(n)])


if __name__ == '__main__':
    MyTest(Solution()).start_test()
