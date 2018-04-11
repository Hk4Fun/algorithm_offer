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
时间O（n），空间O（1）（字母种类有限，所以空间为常数）
the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values, 
and keep two pointers which define the max substring. 
move the right pointer to scan through the string , 
and meanwhile update the hashmap. If the character is already in the hashmap, 
then move the left pointer to the right of the same character last found. 
Note that the two pointers can only move forward.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = start = 0
        used = {}  # 记录每个字母最近出现的位置
        for i, v in enumerate(s):  # i一直往右遍历
            if v in used and start <= used[v]:  # 之前出现过该字母并且最近出现的位置在start到i之间
                start = used[v] + 1  # 将start移到上次出现位置的右边
            else:
                maxLen = max(maxLen, i - start + 1)
            used[v] = i  # 新增或更新每个字母最近出现的位置
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
