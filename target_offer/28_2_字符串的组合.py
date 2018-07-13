__author__ = 'Hk4Fun'
__date__ = '2018/2/6 1:31'

'''题目描述：
输入一个字符串,按照字典序打印出该字符串中字符的所有组合
例如输入字符串abc,则打印出由字符a,b,c所能组合出来的所有字符串'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
'''主要思路：
思路1：根据组合公式：C(m,n)=C(m-1,n-1)+C(m,n-1),即
       从头扫描字符串得到第一个字符，针对第一个字符，有两种选择  
       把这个字符放到组合中去，接下来我们需要在剩下的n-1个字符中选取m-1个字符；  
       如果不把这个字符放到组合中去，则需要在剩下的n-1个字符中选取m个字符   
思路2：注意观察['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'],
        前一部分['a', 'ab', 'abc', 'ac']除了'a',去掉首字符'a'后，剩下
        ['b', 'bc', 'c']恰好与后一部分相同；同理，['b', 'bc', 'c']中前一部分
        ['b', 'bc']除了'b',去掉首字符'b'后,恰好与后一部分'c'相同，很明显用递归完成：
        遍历string的每一个字符，先添加该字符到组合结果中，然后再把该字符与后面部分的组合结果
        中的每一项拼接并返回即可，注意比较与‘字符串的排列’中思路2的解法的异同点
思路3：pythonic，使用itertools.combinations()
'''
import itertools


class Solution:
    def Combination1(self, string):
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

    def Combination2(self, string):
        def combination(string):
            if len(string) == 1:  # 只剩下一个字符时直接返回该字符
                return [string]
            result = []
            for i in range(len(string)):  # 遍历string的每一个字符
                result.append(string[i])  # 先添加该字符到组合结果中
                for j in combination(string[i + 1:]): # 与前面的字符无关了
                    result.append(string[i] + j)  # 再把该字符与后面部分的组合结果中的每一项拼接
            return result

        if not string:
            return
        return sorted(list(set(combination(string))))

    def Combination3(self, string):
        if not string:
            return None
        result = []
        for i in range(1, len(string) + 1):
            iter = itertools.combinations(string, i)
            result += list(map(''.join, list(iter)))
        return sorted(list(set(result)))


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
