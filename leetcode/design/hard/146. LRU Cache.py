__author__ = 'Hk4Fun'
__date__ = '2018/7/31 3:55'
'''题目描述：
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key 
            if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
            When the cache reached its capacity, 
            it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
'''主要思路：
思路1：cache + double linked list

思路2：cache + double circle linked list
       思路1的优化，不必使用 dummy head 和 dummy tail，直接使用self作为dummy
       然后首尾相连，构成双向环形链表
      
思路3：collections.OrderedDict
'''
from collections import OrderedDict


class Node:  # 双向链表结点
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.cache:
            # 命中cache，把该node移到链表尾部并返回node的val
            # 这样链表头结点（head.next）就是最近最长时间未访问的结点
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, val):
        if key in self.cache:
            # key已经在cache中，先从链表中删除，后面再放到尾部
            self._remove(self.cache[key])
        node = Node(key, val)  # 创建新的node
        self.cache[key] = node  # 放入cache中
        self._add(node)  # 将node放到链表尾部
        if len(self.cache) > self.capacity:
            # cache空间不足，删除链表头节点（head.next），同时从cache中删除
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]

    def _add(self, node):
        # 将node添加到链表尾部
        p = self.tail.pre
        p.next = node
        self.tail.pre = node
        node.pre = p
        node.next = self.tail

    def _remove(self, node):
        # 将node从链表中删除
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.next = self.pre = self  # 双向环形链表

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, val):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, val)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.capacity:
            node = self.next
            self._remove(node)
            del self.cache[node.key]

    def _add(self, node):
        p = self.pre
        p.next = node
        self.pre = node
        node.pre = p
        node.next = self

    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p


class LRUCache3:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # 有序字典会记住键值加入的顺序，这样可以省去一个双链表

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # 把命中的node放到有序字典尾部
            return self.cache[key]
        return -1

    def put(self, key, val):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(False)  # False表示删除字典尾部结点（默认删除头结点）
        self.cache[key] = val
