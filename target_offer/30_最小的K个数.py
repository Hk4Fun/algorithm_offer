__author__ = 'Hk4Fun'
__date__ = '2018/2/9 16:41'

'''题目描述：
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''
'''主要思路：
思路1（时间O(nlogk)，空间O(1)）：
基于Partition的算法, 只有当我们可以修改输入的数组时可用。
利用Partition找到第(k-1)小的数(从0开始)，则数组左边的k个数字就是最小的k个数字
（这k个数字不一定是排序的）

思路2（时间O(nlogk)，空间O(k)）：
不必修改数组，适合海量数据，利用一个k容量的容器存放数组, 构造最大堆, 
当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数，
使得容器中的k个数保持是最小的k个数。其实可以用max()取得容器中的最大值，
但时间复杂度为O(k)，没有最大堆快，其只有O(1)，但插入需O(logk)。
使用python内置模块heapq：https://docs.python.org/3/library/heapq.html

思路3（时间O(nlogn)，空间O(1)）：
直接排序，然后取前面k个数
'''


class Solution:
    def KLeastNumbers1(self, numbers, k):
        def partition(numbers, start, end):
            last_small = start - 1  # 小于区域的右边界
            for i in range(start, end):  # 遍历start~end-1范围内的元素
                if numbers[i] < numbers[end]:  # 找到比标杆还小的数
                    last_small += 1  # 扩大小于区域的右边界
                    if last_small != i:  # 不必自己和自己交换
                        # 把那个比标杆还小的数和刚刚扩大的小于区域右边界处交换
                        numbers[last_small], numbers[i] = numbers[i], numbers[last_small]
            last_small += 1  # 右移一格指向大于等于区域的左边界，即标杆实际上的正确位置
            numbers[last_small], numbers[end] = numbers[end], numbers[last_small]  # 现在可以把标杆交换过来了
            return last_small  # 返回分界线

        if not numbers or k < 1 or k > len(numbers):
            return []
        start, end = 0, len(numbers) - 1
        # 以下为二分， 只不过分界线不再是mid，而是通过partition求得
        while start <= end:
            index = partition(numbers, start, end)
            if index > k - 1:  # 最小的k个数，则第k小的数下标为k-1
                end = index - 1
            elif index < k - 1:
                start = index + 1
            else:
                return numbers[:k]

    def KLeastNumbers2(self, numbers, k):
        import heapq
        if not numbers or len(numbers) < k or k <= 0:
            return []
        output = []
        for number in numbers:
            if len(output) < k:  # 容器没填满，不比较直接放进去
                output.append(number)
            else:
                output = heapq.nlargest(k, output)  # 使用最大堆排序
                if number < output[0]:  # output[0]为堆顶，最大值
                    output[0] = number  # 替换掉最大值，相当于删除堆顶，新数入堆
        return output  # 容器中的k个数始终是最小的k个数

    def KLeastNumbers3(self, numbers, k):
        length = len(numbers)
        if not numbers or length < k or k <= 0:
            return []
        return sorted(numbers)[:k]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        self.debug = True
        testArgs = []

        # k小于数组的长度
        testArgs.append([[4, 5, 1, 6, 2, 7, 3, 8], 4, [1, 2, 3, 4]])

        # k等于数组的长度
        testArgs.append([[4, 5, 1, 6, 2, 7, 3, 8], 8, [1, 2, 3, 4, 5, 6, 7, 8]])

        # k大于数组的长度
        testArgs.append([[4, 5, 1, 6, 2, 7, 3, 8], 10, []])

        # k等于1
        testArgs.append([[4, 5, 1, 6, 2, 7, 3, 8], 1, [1]])

        # k等于0
        testArgs.append([[4, 5, 1, 6, 2, 7, 3, 8], 0, []])

        # 数组中有相同的数字
        testArgs.append([[4, 5, 1, 6, 2, 7, 2, 8], 2, [1, 2]])

        # 空数组
        testArgs.append([[], 2, []])

        return testArgs

    def convert(self, result, *func_arg):
        return sorted(result)


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
