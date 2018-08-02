__author__ = 'Hk4Fun'
__date__ = '2018/8/2 11:02'
'''题目描述：
Design and implement a data structure for Least Frequently Used (LFU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key 
if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. 
For the purpose of this problem, when there is a tie 
(i.e., two or more keys that have the same frequency), 
the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
'''主要思路：
LFU包含了LRU的思想，因此需在LRU的基础上多一个map来辅助

思路1：two dict + circular double linked list
keymap = { key : node }，相当于cache
freqmap = { fre : root }，每个freq对应一个循环双端链表
root 为循环双端链表的代表结点，root.next表示最近最长时间未访问的结点

思路2：dict + OrderedDict
keymap = { key : (val, freq) }
freqmap = defaultdict(OrderedDict) = { freq : { key : 0 } }
'''


class Node:  # 循环双端链表结点
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = self.next = self
        self.freq = 1


class LFUCache1:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.freqmap = {}
        self.keymap = {}
        self.minfreq = 1  # 记录最小freq

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keymap:
            node = self.keymap[key]
            node.freq += 1
            self._remove(node)
            if self.freqmap[self.minfreq].next is self.freqmap[self.minfreq]:  # 最小频率对应的链表为空
                self.minfreq += 1
            root = self.freqmap.setdefault(node.freq, Node(0, 0))
            self._add(node, root)
            return node.val
        return -1

    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0: return
        if key in self.keymap:
            self.keymap[key].val = val
            self.get(key)
        else:
            if len(self.keymap) == self.cap:
                node = self.freqmap[self.minfreq].next
                self._remove(node)
                del self.keymap[node.key]
            self.minfreq = 1
            node = Node(key, val)
            self._add(node, self.freqmap.setdefault(1, Node(0, 0)))
            self.keymap[key] = node

    def _add(self, node, root):
        # 把 node 放到 root 的前面
        p = root.pre
        p.next = root.pre = node
        node.next = root
        node.pre = p

    def _remove(self, node):
        # 从链表中删除 node
        p, n = node.pre, node.next
        p.next, n.pre = n, p


from collections import OrderedDict, defaultdict


class LFUCache2:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keymap = {}
        self.freqmap = defaultdict(OrderedDict)
        self.cap = capacity
        self.minfreq = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keymap: return -1
        val, freq = self.keymap[key]
        del self.freqmap[freq][key]
        self.keymap[key] = (val, freq + 1)
        self.freqmap[freq + 1][key] = 0
        if not self.freqmap[self.minfreq]: self.minfreq += 1
        return val

    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0: return
        if key in self.keymap:
            self.keymap[key] = (val, self.keymap[key][1])
            self.get(key)
        else:
            if len(self.keymap) == self.cap:
                del self.keymap[self.freqmap[self.minfreq].popitem(False)[0]]
            self.minfreq = 1
            self.keymap[key] = (val, 1)
            self.freqmap[1][key] = 0
