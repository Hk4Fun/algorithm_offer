__author__ = 'Hk4Fun'
__date__ = '2018/4/3 16:16'
'''题目描述：
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
'''主要思路：
思路1（时间O（n^2），空间O（n））：
https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-dp(i-1)-*-dp(n-i)
动态规划，每个结点都有可能为根
G(n)：结点数为n的BST种数
F(i, n): 以下标为i的数为根节点，结点数为n的BST种数
所以G(n) = F(0, n) + F(1, n) + ... + F(n-1, n)
而 F(i, n) = G(i) + G(n-i-1) (即左子树为BST的种数+右子树为BST的种数)
这里有个微妙的地方就是，右子树的值都大于根节点的值，但这里定义的n只关心结点数，
因为我们分割左右子树的时候按照排好序的序列来分割就行了
最终，G(n) = G(0)*G(n-1) + G(1)*G(n-2) + G(2)*G(n-3) + ... + G(n-1)*G(0) 
其中，G(0) = G(1) = 1 (空树和只有一个结点的树都只有一种情况)
每个G(i)依赖于前面的G(0)~G(i-1)，因此需要数组dp来保存之前的值

其通项公式就是Catalan Number
这道题相当于给一个序列，问可以有多少种二叉树的中序序列为该序列

思路2：直接套公式。。。
https://www.geeksforgeeks.org/program-nth-catalan-number/
'''


class Solution:
    """
    :type n: int
    :rtype: int
    """

    def numTrees1(self, n):
        if n <= 1: return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]

    def numTrees2(self, n):
        from math import factorial
        x = factorial(n)
        return factorial(2 * n) // (x * x * (n + 1))


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([0, 1])
        testArgs.append([1, 1])
        testArgs.append([2, 2])
        testArgs.append([3, 5])
        testArgs.append([4, 14])
        testArgs.append([5, 42])
        testArgs.append([6, 132])
        testArgs.append([7, 429])
        testArgs.append([8, 1430])

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
