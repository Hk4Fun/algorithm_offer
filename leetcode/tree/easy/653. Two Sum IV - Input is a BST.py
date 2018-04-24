__author__ = 'Hk4Fun'
__date__ = '2018/4/25 0:42'
'''题目描述：
Given a Binary Search Tree and a target number, 
return true if there exist two elements in the BST 
such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
'''主要思路：
思路1：时间O（n），空间O（n）
in order + tow pointers
中序遍历得到递增数组，然后双指针

思路2：时间O（n），空间O（n）
bfs + two sum
上一思路要遍历两遍，可以压缩到只遍历一遍，
但要多借助点空间，不过还是维持在O(n)，
'''


class Solution:
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """

    def findTarget1(self, root, k):
        def dfs(root):
            if not root: return
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)

        self.arr = []
        dfs(root)
        l, r = 0, len(self.arr) - 1
        while l < r:
            s = self.arr[l] + self.arr[r]
            if s > k:
                r -= 1
            elif s < k:
                l += 1
            else:
                return True
        return False

    def findTarget2(self, root, k):
        queue, s = [root], set()  # 使用set可以在用in时达到O(1)，因为set相当于hash表
        for cur in queue:  # 这里的bfs相当微妙，一边往后遍历一边在末尾添加结点
            if cur:
                if cur.val in s: return True
                s.add(k - cur.val)  # 借助Two Sum的思路
                queue.append(cur.left)
                queue.append(cur.right)
        return False


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
