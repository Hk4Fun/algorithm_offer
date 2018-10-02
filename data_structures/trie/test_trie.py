__author__ = 'Hk4Fun'
__date__ = '2018/10/2 18:15'

from trie import Trie


class TestTrie:
    def test(self):
        trie = Trie()
        assert trie.size == 0
        assert repr(trie) == "Trie({})"
        assert trie.words == []

        trie.add('cat')
        assert trie.size == 1
        assert repr(trie) == "Trie({'c': {'a': {'t': {'end': True}}}})"
        assert trie.words == ['cat']

        trie.add('cat')
        assert trie.size == 1
        assert trie.words == ['cat']

        assert 'cat' in trie
        assert 'ca' not in trie
        assert 'catalog' not in trie

        trie.add('dog')
        assert trie.size == 2
        assert trie.words == ['cat', 'dog']

        assert 'dog' in trie
        assert trie.is_prefix('ca') is True

        trie.add('deer')
        trie.add('pan')
        trie.add('panda')
        assert trie.size == 5
        assert trie.words == ['cat', 'dog', 'deer', 'pan', 'panda']
        assert 'd' not in trie
        assert 'pan' in trie
        assert 'pand' not in trie

        assert trie.is_prefix('d') is True
        assert trie.is_prefix('do') is True
        assert trie.is_prefix('pa') is True
        assert trie.is_prefix('pan') is True
        assert trie.is_prefix('pand') is True
        assert trie.is_prefix('panda') is True
        assert trie.is_prefix('da') is False
        assert trie.is_prefix('pana') is False


        trie.add('do')
        assert trie.prefix_words('pa') == ['pan', 'panda']
        assert trie.prefix_words('d') == ['do', 'dog', 'deer']
        assert trie.prefix_words('do') == ['do', 'dog']
        assert trie.prefix_words('cat') == ['cat']
        assert trie.prefix_words('pap') == []


        trie = Trie(['cat', 'dog', 'do', 'deer', 'pan', 'panda'])
        print('\n', trie)
