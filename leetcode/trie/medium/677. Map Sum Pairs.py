__author__ = 'Hk4Fun'
__date__ = '2018/10/3 1:08'
'''题目描述：
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). 
The string represents the key and the integer represents the value. 
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, 
and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
'''
'''主要思路：
思路1：
Trie存储，在insert时一路上累加val，这样前缀的val可以在sum时直接返回而不必深入底层求和
由于要支持更新操作，因此需要一个额外的map存储上一次的val，然后累加差值即可
思路2：
pythonic，使用字符串内置方法startswith
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0


class MapSum1:
    def __init__(self):
        self.map = {}  # 为更新值做准备，存放上次插入的键值对
        self.root = TrieNode()

    def insert(self, key, val):  # 时间O（k），k为key的长度
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.val += delta  # 从根节点开始累加差值
        for ch in key:
            cur = cur.children.setdefault(ch, TrieNode())
            cur.val += delta

    def sum(self, prefix):  # 时间O（p），p为prefix的长度
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.val  # 直接返回val，不用深入底层求和，得益于insert的策略


class MapSum2:
    def __init__(self):
        self.data = {}

    def insert(self, key, val):  # 时间O（1）
        self.data[key] = val

    def sum(self, prefix):  # 时间O（nk），n为data元素个数，k为prefix长度
        return sum(self.data[key] for key in self.data if key.startswith(prefix))


if __name__ == '__main__':
    map = MapSum1()
    map.insert("apple", 3)
    assert map.sum("ap") == 3
    map.insert("app", 2)
    assert map.sum("ap") == 5

    map = MapSum2()
    map.insert("apple", 3)
    assert map.sum("ap") == 3
    map.insert("app", 2)
    assert map.sum("ap") == 5
