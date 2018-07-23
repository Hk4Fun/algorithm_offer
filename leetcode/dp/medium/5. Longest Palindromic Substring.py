__author__ = 'Hk4Fun'
__date__ = '2018/4/2 19:08'
'''题目描述：
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
 
Example:
Input: "cbbd"
Output: "bb"
'''
'''主要思路：
注意这里要求返回最长回文子串而不是最长回文子串的长度

思路1（时间O（n^2），空间O（n^2））：
动态规划
              True,  如果子串s(i,j)为回文串
设 dp(i,j) =  
              False, 如果子串s(i,j)不为回文串
则 dp(i,j) = dp(i+1,j-1) and s[i] == s[j]
base case: dp(i,i) = True, dp(i, i+1) = (s[i] == s[i+1])

空间可以优化成O(n)，需要记录两行

思路2（时间O（n^2），空间O（n））：
遍历每个中心，由中心向两边扩展
注意这里2n-1个中心，因为偶数回文时中心不在数组中，隐藏在两个数中间

思路3（时间O（n^2），空间O（1））：
上一思路的优化而已

思路4（时间O（n），空间O（n））：
Manacher算法
'''


class Solution:
    """
    :type s: str
    :rtype: str
    """

    def longestPalindrome_dp(self, s):
        start, maxLen = 0, 1
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):  # 从下往上，从左往右填充dp
            dp[i][i] = True
            for j in range(i + 1, len(s)):
                if (j == i + 1 and s[i] == s[i + 1]) or (dp[i + 1][j - 1] and s[i] == s[j]):
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        start = i
        return s[start:start + maxLen]

    def longestPalindrome_center(self, s):
        def help(l, r):  # 由中心向两边扩展
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ''
        for i in range(len(s)):
            res = max(help(i, i), help(i, i + 1), res, key=len)
        return res

    def longestPalindrome_center_opt(self, s):
        # 上一思路的优化：如果r已经来到最右边，就没有必要接着遍历下一个中心了
        # 下一个回文子串再长也不会超过之前已经到达最右边界的回文子串
        def help(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = help(i, i)
            l2, r2 = help(i, i + 1)
            len1, len2 = r1 - l1 + 1, r2 - l2 + 1
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2
            if r1 == len(s) - 1 or r2 == len(s) - 1: break
        return s[start:end + 1]

    def Manacher(self, s):
        T = '#'.join('^{}$'.format(s))  # ^和$是哨兵，可以避免边界检查，且防止后面在分片时溢出
        P = [0] * len(T)
        C = R = 0
        maxLen, center = -float('inf'), 0
        for i in range(1, len(T) - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # 求出起始扩充半径
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]: P[i] += 1  # 尝试扩充，失败自动退出，边界有哨兵不用检查越界
            if i + P[i] > R: C, R = i, i + P[i]  # 更新最右边界和最右边界的中心
            if P[i] > maxLen: maxLen, center = P[i], i  # 更新最大回文半径和中心
        return s[(center - maxLen) // 2:(center + maxLen) // 2]  # 别忘了这些都是填充字符后的索引和半径，所以最后都要//2


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
