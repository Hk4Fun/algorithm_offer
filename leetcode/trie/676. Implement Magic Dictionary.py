__author__ = 'Hk4Fun'
__date__ = '2018/10/3 12:44'
'''题目描述：
Implement a magic directory with buildDict, and search methods.
For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
For the method search, you'll be given a word, 
and judge whether if you modify exactly one character into another character in this word, 
the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. 
You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, 
as static/class variables are persisted across multiple test cases. 
Please see here for more details.
'''
'''主要思路：
思路1：Trie
思路2：hash table    key:len(word)  val:list:word  
思路3：pythonic 在思路2的基础上使用zip简化search操作
'''

from collections import defaultdict


class MagicDictionary1:

    def __init__(self):
        self.root = {}

    def buildDict(self, dict):
        for word in dict:
            cur = self.root
            for ch in word:
                cur = cur.setdefault(ch, {})
            cur['end'] = True

    def search(self, word):
        return self._search(self.root, word, 0, True)

    def _search(self, node, word, i, mistake_allowed):
        # mistake_allowed 表示一次修改机会，
        # 一旦发生修改，后面一直为false，且该修改机会必须消耗掉
        if i == len(word):  # word匹配到最后
            if 'end' in node and not mistake_allowed:  # 该位置为单词且必须消耗掉一次修改机会
                return True
            return False
        if word[i] not in node:  # 匹配不到
            if mistake_allowed:  # 还有修改机会
                return any(self._search(node[ch], word, i + 1, False)  # 从node中其他字母出发继续往下匹配，但修改机会已经没了
                           for ch in node if ch != 'end')  # 注意忽略ch='end'
            return False  # 匹配不到有没有修改的机会
        # 匹配到了
        if mistake_allowed:  # 还有修改机会
            # 要么继续往下匹配保留这个修改机会，要么将这次修改机会消耗掉，匹配node中其他字母
            return self._search(node[word[i]], word, i + 1, True) or \
                   any(self._search(node[ch], word, i + 1, False)
                       for ch in node if ch != 'end' and ch != word[i])  # 注意忽略ch='end'
        return self._search(node[word[i]], word, i + 1, False)  # 匹配到且没有修改机会了，只能接着往下匹配


class MagicDictionary2:

    def __init__(self):
        self.word_dict = defaultdict(list)

    def buildDict(self, dict):
        for w in dict:
            self.word_dict[len(w)].append(w)

    def search(self, word):
        for w in self.word_dict[len(word)]:
            diff_count = 0
            for i in range(len(w)):
                if word[i] != w[i]:
                    if diff_count == 0:
                        diff_count += 1
                    else:
                        diff_count += 1
                        break
            if diff_count == 1:
                return True
        return False


class MagicDictionary3:

    def __init__(self):
        self.buckets = defaultdict(list)

    def buildDict(self, dict):
        for word in dict:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a != b for a, b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])


def test(dic):
    dic.buildDict(["hello", "leetcode", 'hhllo'])
    assert dic.search("hello") is True
    assert dic.search("hhllo") is True
    assert dic.search("hell") is False
    assert dic.search("leetcoded") is False
    assert dic.search("hhlll") is True
    assert dic.search("llhho") is False


if __name__ == '__main__':
    dic = MagicDictionary1()
    test(dic)

    dic = MagicDictionary2()
    test(dic)

    dic = MagicDictionary3()
    test(dic)
