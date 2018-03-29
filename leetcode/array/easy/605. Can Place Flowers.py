__author__ = 'Hk4Fun'
__date__ = '2018/3/29 17:24'
'''题目描述：
Suppose you have a long flowerbed in which 
some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots 
- they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, 
where 0 means empty and 1 means not empty), and a number n, 
return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''
'''主要思路：
思路1（时间O（n），空间O（1））：
从左到右遍历每个0，看左右两边是否也为0，则该位置可以种花，置1
最左边只看右边，最右边只看左边

思路2（时间O（n），空间O（1））：
上面的算法改变了数组内容，这在某些场合下是不允许的，下面的算法不会改变原数组中的元素：
设置一个空位置计数器，当空位置为3时n--，计数器置为1，而不是0，因为把花种在中间，
右边一定是空位。如果遇到1就把计数器置0，从头开始计数。
'''


class Solution:
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """

    def canPlaceFlowers_change(self, flowerbed, n):
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) \
                    and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                i += 1  # 当前位置被填充，下个位置肯定不行，直接跳过需要
            if n <= 0: return True  # 只要满足条件就返回，提前结束
            i += 1
        return False

    def canPlaceFlowers_nochange(self, flowerbed, n):
        empty_count = 1
        for is_planted in flowerbed:
            if is_planted:
                empty_count = 0
            else:
                empty_count += 1
                if empty_count == 3:
                    n -= 1
                    empty_count = 1
            if n <= 0: # 提前结束
                return True
        if empty_count == 2: # 最后记得再次检查empty_count是否为2，是则可以再种1棵
            n -= 1
        return n <= 0


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
