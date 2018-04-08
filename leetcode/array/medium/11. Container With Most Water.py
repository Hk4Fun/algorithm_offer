__author__ = 'Hk4Fun'
__date__ = '2018/4/8 15:31'
'''题目描述：
Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
'''主要思路：
时间O（n），空间O（1）
首尾两个指针r，l相向移动
由于高由最短的决定，所以短的指针移动就行了，高的不动（移动高的指针只会得到更小的面积）
移动短的指针虽然宽度变小了，但是也许高度会增加，可能使面积反而增大
'''


class Solution:
    def maxArea1(self, height):  # Runtime：68 ms
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

    def maxArea2(self, height):  # 改进， Runtime：56 ms
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            h = min(height[l], height[r])
            maxArea = max(maxArea, h * (r - l))
            while height[l] <= h and l < r: l += 1  # 直到遇到比原来还高的高度
            while height[r] <= h and l < r: r -= 1
        return maxArea


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

        testArgs.append([[1, 8, 6, 2, 5, 4, 8, 3, 7], 49])

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
