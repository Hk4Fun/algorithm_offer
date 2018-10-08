__author__ = 'Hk4Fun'
__date__ = '2018/3/6 21:36'

'''题目描述：
在一个排序矩阵m*n中找从小到大的第 k 个整数。
排序矩阵的定义为：每一行递增，每一列也递增。
'''
'''主要思路：
思路1（时间O(k*(m+n)), 空间O(1)）：
利用类似于小顶堆的方法，将排序矩阵 matrix 看作小顶堆，即 matrix[0][0] 为矩阵中最小元素，
在取出堆顶元素后，将堆顶元素设置为最大值float('inf')，然后调整矩阵，使其符合排序矩阵的定义。
如此一来，取出的第 k 个元素即排序矩阵中的从小到大第k个数。
关键在于如何调整矩阵：比较inf右边的数和下边的数，小的那个和inf交换，一直下去，
直到inf来到右边界或下边界，此时只需把inf向下移到最底部或右移到最右端，即把inf移到右下角

思路2（时间O(k*min(m,n)), 空间O(min(m,n)）：
如果行数小于等于列数，则行优先遍历，反之列优先遍历，这里解释如何进行行优先遍历（列优先同理）：
k次扫描，每次扫描都把每一行的最小元素进行比较，找出这次比较中的最小值 min，
如果这次找出的元素在第i行第j列，那么第i行下一次比较就从j+1列开始 
比如第一次扫描的最小值是0行的0列元素，那么第二次扫描第0行第0列元素就会被排除，第0行从第1列开始比较

思路3（时间O(k*log(max(m,n))), 空间O(m*n）：
通过思路2发现，每筛选出一个最小值，下一次可能会成为最小值的位置只可能位于该最小值的右边和下边，
所以可以用最小堆，每次从最小堆堆顶筛选出最小值后就把该最小值的右边元素和下边元素加入最小堆，
定义最小堆的数据单元结构为(值，纵坐标，横坐标)。注意每入堆一个元素就要把该元素标记为已访问，
避免同一元素重复入堆。标记数组消耗空间O(m*n），而每次堆排在最坏情况下消耗log(max(m,n))，共进行k次
'''
import heapq


class Solution:
    def kthSmallest1(self, matrix, k):
        def adjust(matrix, rows, cols):
            row, col = 0, 0
            while row < rows - 1 and col < cols - 1:  # 把inf移到右边界或下边界
                if matrix[row][col + 1] < matrix[row + 1][col]:  # 右元素小于下元素
                    matrix[row][col], matrix[row][col + 1] = matrix[row][col + 1], matrix[row][col]
                    col += 1  # 右移
                else:
                    matrix[row][col], matrix[row + 1][col] = matrix[row + 1][col], matrix[row][col]
                    row += 1  # 下移
            # 把inf移到右下角
            while row == rows - 1 and col < cols - 1:  # 来到下边界，一直往右移
                matrix[row][col], matrix[row][col + 1] = matrix[row][col + 1], matrix[row][col]
                col += 1
            while col == cols - 1 and row < rows - 1:  # 来到右边界，一直往下移
                matrix[row][col], matrix[row + 1][col] = matrix[row + 1][col], matrix[row][col]
                row += 1

        if not matrix or not k:
            return
        rows, cols = len(matrix), len(matrix[0])
        if rows * cols < k or k < 1:
            return
        for i in range(k - 1):
            matrix[0][0] = float('inf')
            adjust(matrix, rows, cols)
        return matrix[0][0]

    def kthSmallest2(self, matrix, k):
        if not matrix or not k:
            return
        rows, cols = len(matrix), len(matrix[0])
        if rows * cols < k or k < 1:
            return
        min = matrix[0][0]  # 左上角是整个数组的最小数
        if rows <= cols:  # 行优先遍历
            minIndex = [0] * rows  # minIndex存放每一行最小元素的下标
            minIndex[0] = 1  # 由于(0，0)已经排除，则第一行下次取第二列进行比较
            for i in range(1, k):
                min = float('inf')
                for j in range(rows):  # 扫描每一行的最小元素
                    if minIndex[j] < cols and matrix[j][minIndex[j]] < min:
                        min = matrix[j][minIndex[j]]
                        tmp = j
                minIndex[tmp] += 1  # 排除最小元素的那一行下次取最小元素后面的数进行比较
        else:  # 行优先遍历同理
            minIndex = [0] * cols
            minIndex[0] = 1
            for i in range(1, k):
                min = float('inf')
                for j in range(cols):
                    if minIndex[j] < rows and matrix[minIndex[j]][j] < min:
                        min = matrix[minIndex[j]][j]
                        tmp = j
                minIndex[tmp] += 1
        return min

    def kthSmallest3(self, matrix, k):
        if not matrix or not k:
            return
        rows, cols = len(matrix), len(matrix[0])
        if rows * cols < k or k < 1:
            return
        minHeap = []
        visited = [[False] * cols for _ in range(rows)]  # python创建二维数组不能用[[False] * cols] * rows
        heapq.heappush(minHeap, (matrix[0][0], 0, 0))
        visited[0][0] = True
        for _ in range(k - 1):
            min = heapq.heappop(minHeap)
            i, j = min[1], min[2]
            if i + 1 < rows and not visited[i + 1][j]:
                heapq.heappush(minHeap, (matrix[i + 1][j], i + 1, j))
                visited[i + 1][j] = True
            if j + 1 < cols and not visited[i][j + 1]:
                heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))
                visited[i][j + 1] = True
        return heapq.heappop(minHeap)[0]


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[[1, 5, 7], [3, 7, 8], [4, 8, 9], [5, 10, 11]], 4, 5])
        testArgs.append([[[1, 5, 7], [3, 7, 8], [4, 8, 9], [5, 10, 11]], 6, 7])
        testArgs.append([[[1, 5, 7], [3, 7, 8], [4, 8, 9], [5, 10, 11]], 7, 7])
        testArgs.append([[[1, 5, 7], [3, 7, 8], [4, 8, 9], [5, 10, 11]], 1, 1])
        testArgs.append([[[1, 5, 7], [3, 7, 8], [4, 8, 9], [5, 10, 11]], 12, 11])
        testArgs.append([[[1, 5, 7], [3, 7, 8], [4, 8, 9], [5, 10, 11]], 0, None])
        testArgs.append([None, None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
