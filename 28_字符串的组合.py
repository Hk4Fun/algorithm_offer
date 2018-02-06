__author__ = 'Hk4Fun'
__date__ = '2018/2/6 1:31'

'''题目描述：
输入一个字符串,按照字典序打印出该字符串中字符的所有组合
例如输入字符串abc,则打印出由字符a,b,c所能组合出来的所有字符串'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
'''主要思路：
思路： 根据组合公式：C(m,n)=C(m-1,n-1)+C(m,n-1),即
       从头扫描字符串得到第一个字符，针对第一个字符，有两种选择  
       把这个字符放到组合中去，接下来我们需要在剩下的n-1个字符中选取m-1个字符；  
       如果不把这个字符放到组合中去，则需要在剩下的n-1个字符中选取m个字符   
'''


class Solution:
    def Combination(self, string):
        def combination(string, number, ss):
            if number == 0:  # 从字符串中选取0个字符，意味着不用选取，结束组合，直接把单次组合结果放进全部组合结果并返回
                result.append(ss[:])
                return
            if not string:  # 一定要先判断number再判断string，否则string为空时ss中的组合结果没来得及放入全部组合结果就返回了
                return
            ss.append(string[0])  # 把这个字符放到组合中去
            combination(string[1:], number - 1, ss)  # 接下来我们需要在剩下的n-1个字符中选取m-1个字符

            ss.pop(-1)  # 不把这个字符放到组合中去
            combination(string[1:], number, ss)  # 则需要在剩下的n-1个字符中选取m个字符

        if not string:
            return
        result = []  # 全部组合结果
        ss = []  # 单次组合结果
        for i in range(1, len(string) + 1):  # 每次选取不同的字符长度
            combination(string, i, ss)
        return sorted(list(set(map(''.join, result))))


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append(['', None])
        testArgs.append(['a', ['a']])
        testArgs.append(['ab', ['a', 'ab', 'b']])
        testArgs.append(['aa', ['a', 'aa']])
        testArgs.append(['abc', ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']])
        testArgs.append(
            ['abcd', ['a', 'ab', 'abc', 'abcd', 'abd', 'ac', 'acd', 'ad', 'b', 'bc', 'bcd', 'bd', 'c', 'cd', 'd']])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
