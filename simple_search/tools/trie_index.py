
from typing import Tuple
from collections import namedtuple

from simple_search.tools.index import Index


MatchResult = namedtuple('MatchResult', ['has_matches', 'location'])


class TrieIndex(Index):

    def __init__(self, config: dict):
        super(TrieIndex, self).__init__(config)
        self._trie = TrieNode('*')

    def add(self, key: str, value: "value, any type") -> bool:
        """Add to index."""
        return self._trie.add(key, value)

    def get_by_key(self, key: str) -> "value, any type":
        """Get indexed value"""
        return self._trie.get_by_key(key)


class TrieNode:

    def __init__(self, char):
        self._char = char
        self._children = []
        self._is_finished = False
        self._counter = 1
        self._location = []

    def add(self, word: str, location: tuple) -> bool:
        word = word.lower()
        node = self
        for char in word:
            found_in_child = False
            for child in node._children:
                if child._char == char:
                    child._counter += 1
                    child._location.append(location)
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node._children.append(new_node)
                new_node._location.append(location)
                node = new_node
        node._is_finished = True
        return True

    def get_by_key(self, prefix: str) -> MatchResult:
        prefix = prefix.lower()
        node = self
        if not node._children:
            return MatchResult(False, [])
        for char in prefix:
            char_not_found = True
            for child in node._children:
                if child._char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return MatchResult(False, [])
        return MatchResult(True, node._location)
