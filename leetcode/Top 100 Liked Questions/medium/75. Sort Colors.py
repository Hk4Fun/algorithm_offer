__author__ = 'Hk4Fun'
__date__ = '2018/8/11 22:27'
'''题目描述：
Given an array with n objects colored red, white or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, 
and 2 to represent the color red, 
white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, 
then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''
'''主要思路：
思路1：时间O（n），空间O（1）
荷兰国旗三色问题
设red, white, blue三个指针，
其中[0, red) < k, [red, white) = k, [white, blue] 为未知区域，(blue, len(nums)-1] > k 
这里的k为1
 
思路2：时间O（n），空间O（1）
思路1的优化：思路1要不断交换，可以先把该数抽出来（相当于挖坑），然后根据该数推进覆盖
设i,j,k三个指针，则总是保证 [0,i)=0, [i, j)=1, [j, k)=2, [k, len(nums)-1] 为未知区域
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    def sortColors1(self, nums):
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1  # white可以直接往右移，因为刚交换过来的数一定等于1
            elif nums[white] > 1:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1  # 注意到这里white不动，因为high指向的数是未知的，换过来还得遍历
            else:
                white += 1
        return nums  # for test

    def sortColors2(self, nums):
        i = j = 0
        for k in range(len(nums)):
            # i、j、k的边界在不断往前推进
            v = nums[k]  # 先把当前数抽出来
            nums[k] = 2  # 尝试推进k边界
            if v < 2:  # v不为2，则尝试推进j边界，还原2的个数
                nums[j] = 1
                j += 1
            if v < 1:  # v不为1（为0），则只能推进i边界，还原1的个数
                nums[i] = 0
                i += 1
        return nums


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]])
        testArgs.append([[2, 0, 1], [0, 1, 2]])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
