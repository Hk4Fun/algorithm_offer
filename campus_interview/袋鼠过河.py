__author__ = 'Hk4Fun'
__date__ = '2018/10/12 21:00'
'''题目来源:
2017校招真题
'''
'''题目描述：
一只袋鼠要从河这边跳到河对岸，河很宽，但是河中间打了很多桩子，
每隔一米就有一个，每个桩子上都有一个弹簧，袋鼠跳到弹簧上就可以跳的更远。
每个弹簧力量不同，用一个数字代表它的力量，如果弹簧力量为5，
就代表袋鼠下一跳最多能够跳5米，如果为0，就会陷进去无法继续跳跃。
河流一共N米宽，袋鼠初始位置就在第一个弹簧上面，要跳到最后一个弹簧之后就算过河了，
给定每个弹簧的力量，求袋鼠最少需要多少跳能够到达对岸。如果无法到达输出-1

相似题目：leetcode/Top 100 Liked Questions/55. Jump Game.py
'''
'''主要思路：
思路1：dp

思路2：greedy：
1、先遍历一遍数组，找出有价值的弹簧，并将无价值的弹簧置为None。
所谓有价值是指从该弹簧跳向的最远弹簧比在它之前的弹簧跳向的最远弹簧都要远，
即对于第i个弹簧，i+arr[i]比小于i的弹簧都要大。
为此需要一个last来记录当前最远可到达的下标

2、再次遍历数组，贪心策略。
每次从当前的有价值的弹簧跳向最远的有价值的弹簧，直到跳到最后一个弹簧为止。
若某次跳跃无法跳到下个弹簧，则失败。
可是如何知道最远的有价值的弹簧下标是多少？直接 last += arr[last] 可能会遇到None
需要往前找到第一个不为None的下标作为last，可是往前遍历复杂度就会增加，如何是好？
空间换时间，可以在第一次遍历的时候记录每个last对应的i，记为last_i
比如目前最远可到达的下标last为10，是由i=6的位置跳过来的，因此last_i=6
当第一次遍历时，标记None的同时也把last_i记录到一个辅助数组里，
该辅助数组相当于用来记录距离无效值最近的有效值下标
这样在第二次遍历时遇到None就可以从辅助数组里找到这个last_i，即为最远的有价值的弹簧下标

若某次跳跃无法跳到下个弹簧，意味着从辅助数组里拿出来的最远的下标不变，此时原地打转，失败
'''


class Solution:
    def jump_dp(self, arr):
        dp = [0] + [float('inf')] * len(arr)
        for i in range(1, len(arr) + 1):
            for j in range(i):  # 看之前是否存在可以跳到i的位置j
                if arr[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

    def jump_greedy(self, arr):
        aux = [0] * len(arr)  # 辅助数组，用于记录距离无效值最近的有效值下标
        last = last_i = 0  # last记录记录当前最远可到达的下标，last_i记录达到last的i
        for i in range(len(arr)):
            if arr[i] + i > last:  # 更新last
                last = arr[i] + i
                last_i = i  # 记录跳到last的i
            else:
                arr[i] = None  # 标记无效值
                aux[i] = last_i  # 记录离无效值最近的有效值下标
        last = count = 0
        last_last = last  # 标记last是否更新，防止原地打转
        while last + arr[last] < len(arr):
            if arr[last + arr[last]] is None:
                last = aux[last + arr[last]]  # 从辅助数组里取最远有效值下标（贪婪）
            else:
                last += arr[last]  # 否则直接跳到最远（贪婪）
            if last == last_last:  # last不变，说明跳不出去，原地打转
                return -1
            else:
                last_last = last  # 更新（记录）最近的last
            count += 1
        return count + 1


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

        testArgs.append([[2, 0, 1, 1, 1], 4])
        testArgs.append([[2, 0, 1, 0, 1], -1])
        testArgs.append([[3, 6, 6, 6, 3, 8, 9, 8, 5, 2, 9,
                          7, 3, 6, 5, 4, 2, 3, 6, 9, 9, 8,
                          6, 4, 1, 0, 4, 4, 8, 9, 3, 6, 0,
                          7, 8, 1, 1, 8, 4], 7])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
