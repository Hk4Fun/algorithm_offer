__author__ = 'Hk4Fun'
__date__ = '2018/2/22 10:22'

'''题目描述：
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
'''
'''主要思路：
哈希表法，哈希表定长256，健表示字符阿斯克码，值在不同的算法实现中表示不同
思路1（时间O(n), 空间O(n)）：
哈希表值表示该字符目前在字符流中出现的次数，另外用一个strStream来记录目前读取到的所有字符
读取字符时把读取到的字符添加到strStream后面，然后在相应的哈希表位置中次数+1
找出当前第一个出现一次的字符时只需从头遍历strStream中的字符，则第一个出现次数为1的字符直接返回
思路2（时间O(1), 空间O(1)）：
哈希表值表示该字符在字符流中首次出现的位置，另外用index来记录目前读取的字符流的位置
读取字符时在相应的哈希表位置上看一下是否>=0(哈希表初始化为-1)，如果是说明该字符之前出现过，
则把值更新为-2，表示该字符重复出现；否则说明是第一次出现，把值更新为该字符的出现的位置index
找出当前第一个出现一次的字符时只需扫描整个哈希表，找出最小的大于等于0的值（在字符流中首次出现的位置）
对应字符返回即可
思路3（时间O(1), 空间O(1)）：
哈希表值表示该字符目前在字符流中出现的次数，另外用一个队列onlyOnce来记录在读取字符时该字符还是首次出现的字符
读取字符时在相应的哈希表位置中次数+1，然后判断一下该字符是否首次出现，是的话就放入队列onlyOnce中
找出当前第一个出现一次的字符时只需从队首中取出字符，由于该字符可能在读取之后又出现，所以还要在哈希表中查一下
是否真的只出现一次，超过一次的出队丢弃，则当遇到的第一个出现次数为1的字符时返回即可
'''


class Solution1:
    def __init__(self):
        self.hashList = [0] * 256
        self.strStream = ''

    def Insert(self, char):
        self.strStream += char
        self.hashList[ord(char)] += 1

    def FirstAppearingOnce(self):
        for i in range(len(self.strStream)):
            if self.hashList[ord(self.strStream[i])] == 1:
                return self.strStream[i]
        return '#'


class Solution2:
    def __init__(self):
        self.hashList = [-1] * 256
        self.index = 0

    def Insert(self, char):
        asc = ord(char)
        if self.hashList[asc] == -1:
            self.hashList[asc] = self.index
        elif self.hashList[asc] >= 0:
            self.hashList[asc] = -2
        self.index += 1

    def FirstAppearingOnce(self):
        ch = '#'
        minIndex = float("inf")
        for i in range(256):
            if 0 <= self.hashList[i] < minIndex:
                ch = chr(i)
                minIndex = self.hashList[i]
        return ch


class Solution3:
    def __init__(self):
        self.hashList = [0] * 256
        self.onlyOnce = []

    def Insert(self, char):
        asc = ord(char)
        self.hashList[asc] += 1
        if self.hashList[asc] == 1:
            self.onlyOnce.append(char)

    def FirstAppearingOnce(self):
        while self.onlyOnce and self.hashList[ord(self.onlyOnce[0])] > 1:
            self.onlyOnce.pop(0)
        return self.onlyOnce[0] if self.onlyOnce else '#'


# ================================测试代码================================


import traceback

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量


def Test(testName, chars, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    try:
        result = chars.FirstAppearingOnce()
    except Exception:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
    else:
        print('Failed:测试不通过！\n')


chars = Solution1()
Test('Test1_1', chars, '#')
chars.Insert('g')
Test('Test1_2', chars, 'g')
chars.Insert('o')
Test('Test1_3', chars, 'g')
chars.Insert('o')
Test('Test1_4', chars, 'g')
chars.Insert('g')
Test('Test1_5', chars, '#')
chars.Insert('l')
Test('Test1_6', chars, 'l')
chars.Insert('e')
Test('Test1_7', chars, 'l')

chars = Solution2()
Test('Test2_1', chars, '#')
chars.Insert('g')
Test('Test2_2', chars, 'g')
chars.Insert('o')
Test('Test2_3', chars, 'g')
chars.Insert('o')
Test('Test2_4', chars, 'g')
chars.Insert('g')
Test('Test2_5', chars, '#')
chars.Insert('l')
Test('Test2_6', chars, 'l')
chars.Insert('e')
Test('Test2_7', chars, 'l')

chars = Solution3()
Test('Test3_1', chars, '#')
chars.Insert('g')
Test('Test3_2', chars, 'g')
chars.Insert('o')
Test('Test3_3', chars, 'g')
chars.Insert('o')
Test('Test3_4', chars, 'g')
chars.Insert('g')
Test('Test3_5', chars, '#')
chars.Insert('l')
Test('Test3_6', chars, 'l')
chars.Insert('e')
Test('Test3_7', chars, 'l')

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
