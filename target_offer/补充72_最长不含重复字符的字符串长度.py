__author__ = 'Hk4Fun'
__date__ = '2018/3/5 14:57'

'''题目描述：
输入一个字符串（只包含a~z的字符），求其最长不含重复字符的子字符串的长度。
例如对于arabcacfr，最长不含重复字符的子字符串为acfr，长度为4。
'''
'''主要思路：
思路1： 暴力枚举（时间O(n^3),空间O(1)）
        找出所有子字符串，然后判断每个子字符串中是否包含重复的字符（哈希表法判断）。
        
思路2： 动态规划（时间O(n),空间O(1)）
        定义以第i个字符结尾的不包含重复字符的子字符串的最大长度为f(i)，
        则状态转移方程为：
        如果第i个字符之前没出现过，则f(i)=f(i-1)+1
        如果第i个字符之前出现过，分两种情况讨论：
        先设第i个字符和它上次（最近一次）出现在字符串中的位置的距离为d
        1、d<=f(i-1)。此时第i个字符上次出现在f(i-1)对应的最长子字符串中，因此f(i)=d
           同时也意味着在第i个字符出现两次所夹的子字符串中再也没有其他重复的字符串
        2、d>f(i-1)。此时第i个字符上次出现在f(i-1)对应的最长子字符串之前，
           因此仍然有f(i)=f(i-1)+1
        最终取max(f(i))
        在这里f(i)只与前一个结果f(i-1)有关，所以连数组都可以不用，
        直接用一个变量来记录即可 
'''


class Solution:
    def LSWD1(self, string):
        def hasDup(string):
            hasTable = [-1] * 26
            for i, v in enumerate(string):
                index = ord(v) - ord('a')
                if hasTable[index] >= 0:
                    return True
                hasTable[index] = i
            return False

        if not string:
            return 0
        longest = 0
        length = len(string)
        for start in range(0, length):
            for end in range(start, length):
                count = end - start + 1
                if not hasDup(string[start:end + 1]):
                    if count > longest:
                        longest = count
                else:
                    break  # 发现重复子串，则end没必要往后移动了
        return longest

    def LSWD2(self, string):
        if not string:
            return 0
        hashTable = [-1] * 26
        curLength = 0
        maxLength = 0
        for i, v in enumerate(string):
            index = ord(v) - ord('a')
            preIndex = hashTable[index]
            if preIndex < 0 or i - preIndex > curLength:
                curLength += 1
            else:
                curLength = i - preIndex
            hashTable[index] = i  # 总是更新字符最新出现的位置
            if curLength > maxLength:
                maxLength = curLength
        return maxLength


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append(['abcacfrar', 4])
        testArgs.append(['acfrarabc', 4])
        testArgs.append(['arabcacfr', 4])
        testArgs.append(['aaaa', 1])
        testArgs.append(['abcdefg', 7])
        testArgs.append(['aaabbbccc', 2])
        testArgs.append(['abcdcba', 4])
        testArgs.append(['abcdaef', 6])
        testArgs.append(['a', 1])
        testArgs.append(['', 0])
        testArgs.append([None, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
