__author__ = 'Hk4Fun'
__date__ = '2018/10/2 23:16'
'''题目描述：
Given a list of strings words representing an English Dictionary, 
find the longest word in words 
that can be built one character at a time by other words in words. 
If there is more than one possible answer, 
return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. 
However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''
'''主要思路：
思路1：时间O（nlogn），空间O（n），n表示单词个数
先将所有单词排序（字典序），然后从左到右检查每个单词的前缀（word[:-1]）是否已经在valid_words中，
在的话就把该单词加入valid_words，同时更新longest_word，注意valid_words初始化时需包含一个空串
以此作为只有一个字母单词的前缀

思路2：时间O(N)，空间O(M)，N表示所有单词长度的和, M为最终字典树的结点个数
Trie + DFS
先用trie建立字典树，然后bfs遍历找到最长单词
'''
from collections import defaultdict, deque


class TrieNode:
    __slots__ = ['children', 'is_word', 'word']

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        self.word = ''  # 只有当 self.is_word 为 True 时，self.word 才有意义


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.is_word = True
        cur.word = word

    def bfs(self):
        queue, res = deque([self.root]), ''
        while queue:
            cur = queue.popleft()  # bfs保证了queue的单词长度由短到长
            for child in cur.children.values():
                if child.is_word:  # 关键之处，只将孩子结点为单词的结点入队
                    queue.append(child)
                    # 下面的条件在bfs下可以保证在长度相等时，res为字典序靠前的单词
                    if len(child.word) > len(res) or child.word < res:
                        res = child.word
        return res


class Solution:
    def longestWord1(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        valid_words, longest_word = {''}, ''
        for word in words:
            if word[:-1] in valid_words:
                valid_words.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

    def longestWord2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.add(word)
        return trie.bfs()


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

        testArgs.append([["w", "wo", "wor", "worl", "world"], 'world'])
        testArgs.append([["a", "banana", "app", "appl", "ap", "apply", "apple"], 'apple'])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
