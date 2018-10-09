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
        def partition(l, r):
            last = l - 1  # 小于区的右边界
            for i in range(l, r):  # i 在前面检查
                if numbers[i] < numbers[r]:  # 发现小于标杆numbers[r]的数就把它换入小于区
                    last += 1  # 先扩大小于区的右边界
                    # 换过来的一定是大于等于标杆的，所以i可以一直前进
                    numbers[last], numbers[i] = numbers[i], numbers[last]
            last += 1  # 大于等于区的左边界
            numbers[last], numbers[r] = numbers[r], numbers[last]  # 记得把标杆换过来
            return last

        if not numbers: return 0
        m = len(numbers) // 2
        l, r = 0, len(numbers) - 1
        while l <= r:
            idx = partition(l, r) # 分界点idx
            if idx < m:
                l = idx + 1
            elif idx > m:
                r = idx - 1
            else:
                break
        isHalf = sum(num == numbers[idx] for num in numbers) > len(numbers) >> 1
        return numbers[idx] if isHalf else 0

    def MoreThanHalfNum2(self, numbers):
        if not numbers: return 0
        master = numbers[0]  # 先让第一个数作为守阵地的士兵
        hp = 1  # 初始都为一滴HP
        for num in numbers[1:]:
            if hp == 0:  # 当HP削减为0时，以下一个数作为守阵地的士兵
                master = num
                hp = 1
            elif num == master:
                hp += 1  # 遇到相同元素，相当于支援兵，补血，HP+1
            else:
                hp -= 1  # 遇到不相同元素，相当于敌人，掉血，HP-1
        # 防止该士兵坐收渔翁之利
        isHalf = sum(num == master for num in numbers) > len(numbers) >> 1
        return master if isHalf else 0

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
        self.debug = True

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
