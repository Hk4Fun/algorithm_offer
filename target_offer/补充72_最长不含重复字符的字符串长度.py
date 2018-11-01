__author__ = 'Hk4Fun'
__date__ = '2018/3/5 14:57'

'''题目描述：
输入一个字符串（只包含a~z的字符），求其最长不含重复字符的子字符串的长度。
例如对于arabcacfr，最长不含重复字符的子字符串为acfr，长度为4。
'''
'''主要思路：
思路1： 暴力枚举（时间O(n^3),空间O(1)）
        找出所有子字符串，然后判断每个子字符串中是否包含重复的字符（哈希表法判断）。
        
思路2： 时间O（n），空间O（1）（字母种类有限，所以空间为常数）
        用两个指针始终记录不重复字符串的头start和尾tail，tail一直往右边扫描
        每当遇到重复的字符（需要一个哈希表记录每个字符曾经出现过的最右的索引），
        设该重复字符之前出现的位置为i，如果 start <= i < tail，
        则只需把头指针移到 i + 1 的位置即可，否则（i < start）接着往右扫描
        当然循环每一步都要更新当前字符出现的最新位置，并且更新最大长度
        这里可以稍微优化一下：当出现重复字符并且 start <= i < tail 时，
        我们令start = i + 1，则字符串长度一定减小了，可以不用更新字符串长度
        换句话说，只有start不往右移时我们才去更新最大长度
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

    def LSWD2(self, s):
        if not s: return 0
        maxLen = start = 0
        last = {}  # 记录每个字母最近出现的位置
        for i, v in enumerate(s):  # i一直往右遍历
            if v in last and start <= last[v]:  # 之前出现过该字母并且最近出现的位置在start到i之间
                start = last[v] + 1  # 将start移到上次出现位置的右边
            else:  # 如果start被右移了就没必要更新maxLen了，因为肯定比原来的小
                maxLen = max(maxLen, i - start + 1)
            last[v] = i  # 新增或更新每个字母最近出现的位置
        return maxLen


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
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
