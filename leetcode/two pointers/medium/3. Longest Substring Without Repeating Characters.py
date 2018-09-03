__author__ = 'Hk4Fun'
__date__ = '2018/4/11 21:16'
'''题目描述：
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
'''主要思路：
思路1：时间O（n），空间O（1）（字母种类有限，所以空间为常数）
用两个指针始终记录不重复字符串的头start和尾tail，tail一直往右边扫描
每当遇到重复的字符（需要一个哈希表记录每个字符曾经出现过的最右的索引），
设该重复字符之前出现的位置为i，如果 start <= i < tail，
则只需把头指针移到 i + 1 的位置即可，否则（i < start）接着往右扫描
当然循环每一步都要更新当前字符出现的最新位置，并且更新最大长度
这里可以稍微优化一下：当出现重复字符并且 start <= i < tail 时，
我们令start = i + 1，则字符串长度一定减小了，可以不用更新字符串长度
换句话说，只有start不往右移时我们才去更新最大长度

思路2：时间O（n），空间O（1）
滑动窗口实现，对比 209. Minimum Size Subarray Sum.py 思路2
注意初始值的设定和循环边界，以及程序结构的相似性
'''


class Solution:
    """
    :type s: str
    :rtype: int
    """

    def lengthOfLongestSubstring1(self, s):
        maxLen = start = 0
        used = {}  # 记录每个字母最近出现的位置
        for end, v in enumerate(s):  # i一直往右遍历
            if v in used and start <= used[v]:  # 之前出现过该字母并且最近出现的位置在start到i之间
                start = used[v] + 1  # 将start移到上次出现位置的右边
            else:  # 如果start被右移了就没必要更新maxLen了，因为肯定比原来的小
                maxLen = max(maxLen, end - start + 1)
            used[v] = end  # 新增或更新每个字母最近出现的位置
        return maxLen

    def lengthOfLongestSubstring2(self, s):
        freq = [0] * 256
        l, r = 0, -1
        maxLen = 0
        while l < len(s):
            if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
                # r+1还没到右边界且滑动窗口中没有出现过s[r + 1]
                r += 1
                freq[ord(s[r])] += 1
            else:  # r+1 到了右边界或滑动窗口出现了s[r + 1]，则让l右移
                freq[ord(s[l])] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen


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

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
