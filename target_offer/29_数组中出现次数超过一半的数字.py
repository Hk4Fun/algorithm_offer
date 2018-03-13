__author__ = 'Hk4Fun'
__date__ = '2018/2/9 14:28'

'''题目描述：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''主要思路：
思路1：基于Partition函数的O(n)算法。
       若存在该数，则利用Partition划分找到中位数即为数组中出现次数超过一半的数，
       相当于找到数组中第n/2小的数，最后记得检查查找到的中位数出现次数是否真的有超过总数的一半
思路2：根据数组特点找出O(n)的算法。
       采用阵地攻守的思想：
       先让第一个数作为守阵地的士兵，HP=1；
       遇到相同元素，相当于支援兵，补血，HP+1;
       遇到不相同元素，相当于敌人，掉血，HP-1；
       当HP削减为0时，以下一个数作为守阵地的士兵；
       继续下去，到最后还留在阵地上的士兵，有可能是最强士兵（士兵个数超过一半）。
       为防止该士兵坐收渔翁之利，需再加一次循环，检查该士兵个数是否真的超过一半。
思路3：利用python的字典建立哈希表,O(n)
'''


class Solution:
    def MoreThanHalfNum1(self, numbers):
        # 检查查找到的中位数出现次数是否超过总数的一半
        def CheckMoreThanHalf(numbers, length, result):
            return True if sum(numbers[i] == result for i in range(length)) > length >> 1 else False

        # 划分算法，以numbers[end]作为标杆，使得小于它的在它左边，大于它的在它右边
        def Partition(numbers, length, start, end):
            if not numbers or length <= 0 or start < 0 or end >= length:
                return
            last_small = start - 1  # 小于区域的右边界
            for index in range(start, end):  # 遍历start~end-1范围内的元素
                if numbers[index] < numbers[end]:  # 找到比标杆还小的数
                    last_small += 1  # 扩大小于区域的右边界
                    if last_small != index:  # 不必自己和自己交换
                        # 把那个比标杆还小的数和刚刚扩大的小于区域右边界处交换
                        numbers[index], numbers[last_small] = numbers[last_small], numbers[index]
            last_small += 1  # 右移一格指向大于等于区域的左边界，即标杆实际上的正确位置
            numbers[end], numbers[last_small] = numbers[last_small], numbers[end]  # 现在可以把标杆交换过来了
            return last_small  # 返回标杆

        length = len(numbers)
        if not numbers:
            return 0

        middle = length >> 1  # 要找的数是中位数，即数组中第n/2小的数
        start = 0
        end = length - 1
        index = Partition(numbers, length, start, end)
        while index != middle:  # 直到找到中位数才停止划分
            if index > middle:  # 分界线索引大于中位数索引，说明中位数在分界线左边
                end = index - 1
                index = Partition(numbers, length, start, end)
            else:  # 分界线索引小于中位数索引，说明中位数在分界线右边
                start = index + 1
                index = Partition(numbers, length, start, end)
        result = numbers[middle]
        if not CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

    def MoreThanHalfNum2(self, numbers):
        def CheckMoreThanHalf(numbers, length, result):
            return True if sum(numbers[i] == result for i in range(length)) > length >> 1 else False

        length = len(numbers)
        if not numbers:
            return 0

        master = numbers[0]  # 先让第一个数作为守阵地的士兵，
        HP = 1  # 初始都为一滴HP
        for i in range(1, length):
            if HP == 0:  # 当HP削减为0时，以下一个数作为守阵地的士兵
                master = numbers[i]
                HP = 1
            elif numbers[i] == master:  # 遇到相同元素，相当于支援兵，补血，HP+1
                HP += 1
            else:  # 遇到不相同元素，相当于敌人，掉血，HP-1
                HP -= 1
        if not CheckMoreThanHalf(numbers, length, master):  # 防止该士兵坐收渔翁之利
            master = 0
        return master

    def MoreThanHalfNum3(self, numbers):
        if not numbers:
            return 0

        d = {}
        for i in numbers:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for k, v in d.items():
            if v > (len(numbers) >> 1):
                return k
        return 0


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 存在出现次数超过数组长度一半的数字
        testArgs.append([[1, 2, 3, 2, 2, 2, 5, 4, 2], 2])

        # 不存在出现次数超过数组长度一半的数字
        testArgs.append([[1, 2, 3, 2, 4, 2, 5, 2, 3], 0])

        # 出现次数超过数组长度一半的数字都出现在数组的前半部分
        testArgs.append([[2, 2, 2, 2, 2, 1, 3, 4, 5], 2])

        # 出现次数超过数组长度一半的数字都出现在数组的后半部分
        testArgs.append([[1, 3, 4, 5, 2, 2, 2, 2, 2], 2])

        # 只有一个数
        testArgs.append([[1], 1])

        # 空数组
        testArgs.append([[], 0])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
