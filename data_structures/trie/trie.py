__author__ = 'Hk4Fun'
__date__ = '2018/10/2 18:09'


class Trie:
    def __init__(self, words=None):
        self._root = {}
        self._size = 0
        self._build_trie(words)

    def __repr__(self):
        return 'Trie({!r})'.format(self._root)

    def __str__(self):
        res = []
        res.append('{')
        self._print_trie(res, self._root)
        res.append('}')
        return '\n'.join(res)

    def __contains__(self, word):
        """查看单词word是否在Trie中"""
        cur = self._root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return 'end' in cur

    @property
    def size(self):
        """获得Trie中存储的单词数量"""
        return self._size

    @property
    def words(self):
        res = []
        self._dfs(self._root, '', res)
        return res

    def add(self, word):
        """向Trie中添加一个新的单词word"""
        cur = self._root
        for c in word:
            cur = cur.setdefault(c, {})
        if 'end' not in cur:  # 该单词之前没添加过
            cur['end'] = True
            self._size += 1

    def is_prefix(self, prefix):
        """判断在Trie中是否存在以prefix为前缀的单词"""
        cur = self._root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

    def prefix_words(self, prefix):
        """返回Trie中以prefix为前缀的所有单词"""
        cur = self._root
        words = []
        for c in prefix:
            if c not in cur:
                return []
            cur = cur[c]
        self._dfs(cur, '', words)
        return [prefix + word for word in words]

    def remove_prefix_words(self, prefix):
        """在Trie中删除以prefix为前缀的所有单词"""
        if not self.is_prefix(prefix): return
        cur = self._root
        for c in prefix[:-1]:
            cur = cur[c]
        cur.pop(prefix[-1])

    def remove_word(self, word):
        """在Trie中删除单词word"""
        if word not in self: return
        self._remove_word(self._root, word)

    def _remove_word(self, node, word, idx=0):
        if idx == len(word):
            node.pop('end')
            return
        self._remove_word(node[word[idx]], word, idx + 1)
        if node[word[idx]] == {}:
            node.pop(word[idx])

    def _build_trie(self, words):
        if words:
            for word in words:
                self.add(word)

    def _dfs(self, node, word, words):
        if 'end' in node:
            words.append(word)  # 这里不能直接返回，因为该单词可能为别的单词的前缀
        for ch in node:
            if ch != 'end':
                self._dfs(node[ch], word + ch, words)

    def _print_trie(self, res, node, word='', indent=1):
        """递归打印Trie树，indent控制缩进"""
        if 'end' in node:
            res.append('{}{}'.format('\t' * indent, word))
        for ch in node:
            if ch != 'end':
                res.append('{}{}:{{'.format('\t' * indent, ch))
                self._print_trie(res, node[ch], word + ch, indent + 1)
                res.append('{}}}'.format('\t' * indent))
